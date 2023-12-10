import vosk
import sounddevice as sd
import queue
import json

def sound_to_text(device=1, samplerate=48000):
    model_path = r"" #here you need to add path to speech recognition model
    model = vosk.Model(model_path)
    q = queue.Queue()

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    print("listening...")
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype="int16",
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())['text'].lower()
                print(f"You said: {result}")
                return result
            # else:
            #     result = result=json.loads(rec.PartialResult())['partial'].lower()
            #     print(result)

