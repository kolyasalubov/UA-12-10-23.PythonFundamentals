from sound_funcions import *
from skills import *
import words

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def recognize(result, vectorizer, clf):
    trg = words.names.intersection(result.split())
    if not trg:
        return
    result = result.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([result]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    


    if func_name == 'weather':
        if "in" in result:
            city = result.split("in", 1)[-1].strip()
            print(f"works good with parameter: {city}")
            exec(func_name + '(city)')
        else: exec(func_name + "()")
        
    else:
        read(answer.replace(func_name, ''))
        exec(func_name + '()')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    while True:
        u_input = sound_to_text()
        recognize(u_input, vectorizer, clf)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)