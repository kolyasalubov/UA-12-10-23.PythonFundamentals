import torch
import sounddevice as sd
import time
import re
from num2words import num2words


def read(text):
    language = 'en'
    model_id = 'v3_en'
    sample_rate = 48000
    speaker = 'en_112'  
    put_accent = True
    put_yo = False
    device = torch.device('cpu')

    model, _ = torch.hub.load(
        repo_or_dir='snakers4/silero-models',
        model='silero_tts',
        language=language,
        speaker=model_id
    )

    model.to(device)
    
    for match in re.findall('\d+', text):
        word = num2words(int(match), lang='en')
        text = text.replace(match, word)

    audio = model.apply_tts(
        text=text,
        speaker=speaker,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo
    )

    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop()
    


