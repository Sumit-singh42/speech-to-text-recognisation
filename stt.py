import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record_audio_cli(duration=5, filename="recorded.wav"):
    print(f"🎙️ Recording for {duration} seconds...")
    fs = 16000
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, recording)
    print(f"💾 Saved recording as {filename}")
    return filename

def transcribe_file(filepath):
    model = whisper.load_model("base")
    result = model.transcribe(filepath)
    return result.get("text", "").strip()
