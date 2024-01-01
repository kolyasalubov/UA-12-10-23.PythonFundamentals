from sqlalchemy import (Table, create_engine, Column, Integer, String,
                        ForeignKey, or_)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Створюється з'єднання з базою даних SQLite у пам'яті)
# engine = create_engine('sqlite:///:memory:', echo=True)
DATABASE_URL = "sqlite:///linguist.db"
engine = create_engine(DATABASE_URL)

# Створюємо базовий клас для оголошення моделей
Base = declarative_base()


# Визначаємо моделі User, Deck та Card
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    # Зв'язок один до багатьох (один користувач має багато карток і колод)
    cards = relationship('Card', back_populates='user')
    decks = relationship('Deck', back_populates='user')


class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Зв'язок багато до одного
    # (багато колод належать одному користувачеві)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='decks')

    # Зв'язок багато до багатьох (одна колода містить багато карток)
    cards = relationship('Card', secondary='deck_card_association',
                         back_populates='decks')


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    # Зв'язок багато до одного
    # (багато карток належать одному користувачеві)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='cards')

    # Зв'язок багато до багатьох
    # (багато карток містяться в багатьох колодах)
    deck_id = Column(Integer, ForeignKey('decks.id'))
    decks = relationship('Deck', secondary='deck_card_association', back_populates='cards')


# Асоціативна таблиця для зв'язку багато до багатьох між Deck та Card
deck_card_association = Table('deck_card_association', Base.metadata,
                              Column('deck_id', Integer, ForeignKey('decks.id')),
                              Column('card_id', Integer, ForeignKey('cards.id'))
                              )

# Створюємо таблиці в базі даних
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Створюємо сесію для взаємодії з базою даних
session = Session()


####################################################################################################################################

def user_create(name, email, password):
    """
    This function creates a new user. It accepts the user's name,
    email address and password. added to the list of users,
    and then the created user is returned.
    """

    new_user = User(name=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user


def user_get_by_id(user_id):
    """returns user's id"""

    return session.query(User).get(user_id)


def user_update_name(user_id, name):
    """
    The username is updated with the new value (name).
    The updated user is returned.
    """

    user = session.query(User).get(user_id)
    if user:
        user.name = name
        session.commit()
    return user


def user_change_password(user_id, old_password, new_password):
    """
    It checks whether the current user password matches
    the transmitted one. If the passwords match, the password
    is updated with the new value and the function returns True.
    Otherwise returns False.
    """

    user = session.query(User).get(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False


def user_delete_by_id(user_id):
    """Deletes user by his id"""

    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False


# Функції колоди:
def deck_create(name, user_id):
    """
    A new deck identifier is created, which is equal to
    the current list length +1. A new deck object is created using
    the passed parameters. The new deck is added to the deck list.
    The created deck is returned.
    """

    new_deck = Deck(name=name, user_id=user_id)
    session.add(new_deck)
    session.commit()
    return new_deck


def deck_get_by_id(deck_id):
    """returns deck's id"""

    return session.query(Deck).get(deck_id)


def deck_update(deck_id, name):
    """Deck name is updated with new value"""

    deck = session.query(Deck).get(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck


def deck_delete_by_id(deck_id):
    """delete deck"""

    deck = session.query(Deck).get(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False


# Функції картки:
def card_create(user_id, word, translation, tip):
    """
    A new card identifier is created, which is equal to
    the current list length +1. A new card object is created using
    the passed parameters. The new card is added to the card list.
    The created card is returned.
    """

    new_card = Card(user_id=user_id, word=word,
                    translation=translation, tip=tip)
    session.add(new_card)
    session.commit()
    return new_card


def card_get_by_id(card_id):
    """returns card's id"""

    return session.query(Card).get(card_id)


def card_filter(sub_word):
    """
    A new list, filtered_cards, is created, which includes all cards in
    which the substring sub_word occurs in a word (card.word),
    translation (card.translation) or tip (card.tip).
    """

    return session.query(Card).filter(
        or_(
            Card.word.contains(sub_word),
            Card.translation.contains(sub_word),
            Card.tip.contains(sub_word)
        )
    ).all()


def card_update(card_id, word=None, translation=None, tip=None):
    """
    The function card_get_by_id is called to get a card
    by its identifier.
    - If the word parameter is passed, the word of the card is updated.
    - If the translation parameter is passed, the translation
    of the card is updated.
    - If the tip parameter is passed, the card's tip is updated.
    The updated card is returned.
    """

    card = session.query(Card).get(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
        session.commit()
    return card


def card_delete_by_id(card_id):
    """delete card by id"""

    card = session.query(Card).get(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False


#######################################################################

# Приклади використання
user1 = user_create("John Doe", "john@example.com", "password123")
user2 = user_create("John_Second", "john_second@example.com",
                    "password1234")

deck1 = deck_create("Vocabulary", user1.id)
deck2 = deck_create("Phrases", user2.id)

card1 = card_create(user1.id, "apple", "яблуко", "A fruit")
card2 = card_create(user2.id, "car", "автомобіль", "A vehicle")

print("Users:", session.query(User).all())
print("Decks:", session.query(Deck).all())
print("Cards:", session.query(Card).all())
