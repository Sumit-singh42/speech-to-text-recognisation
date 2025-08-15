import argparse
import os
from stt import transcribe_file, record_audio_cli
from ed import detect_emotion_with_context
from grammer import correct_grammar
from memory import add_entry, save_memory

def run_cli(audio_path=None, record_duration=None, use_gemini=False, clear_memory=False):
    if clear_memory:
        save_memory([])  
        print("🧹 Memory cleared.")
        return

    if not audio_path and not record_duration:
        audio_path = input("Enter path to audio file (leave blank to record): ").strip()
        if not audio_path:
            try:
                record_duration = int(input("Enter record duration in seconds: ").strip())
            except ValueError:
                print("Invalid duration.")
                return

    if record_duration and not audio_path:
        audio_path = record_audio_cli(record_duration)
        if not audio_path:
            print("Recording failed.")
            return

    if not audio_path or not os.path.exists(audio_path):
        print(f"File not found: {audio_path}")
        return

    print("Transcribing")
    transcript = transcribe_file(audio_path)
    print("Transcript:", transcript)

    print("Detecting emotion with context")
    emotion = detect_emotion_with_context(transcript, use_gemini)
    print("Emotion:", emotion)

    print("Correcting grammar")
    corrected = correct_grammar(transcript, use_gemini)
    print("Corrected:", corrected)
    add_entry(transcript, emotion)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", type=str, help="Path to audio file")
    parser.add_argument("--record", type=int, help="Record duration in seconds")
    parser.add_argument("--use-gemini", action="store_true", help="Use Gemini API instead of local model")
    parser.add_argument("--clear-memory", action="store_true", help="Clear stored conversation memory")
    args = parser.parse_args()

    run_cli(audio_path=args.audio, record_duration=args.record,
            use_gemini=args.use_gemini, clear_memory=args.clear_memory)

    print("Emotion detection completed.")       
