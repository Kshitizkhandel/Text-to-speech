import argparse
import os
from TTS.api import TTS

def main():
    parser = argparse.ArgumentParser(description="Run Coqui TTS in Docker.")
    parser.add_argument("--text", type=str, required=True, help="Text to synthesize.")
    parser.add_argument("--reference_voice", type=str, help="Path to reference speaker WAV for voice cloning (optional).")
    parser.add_argument("--output", type=str, required=True, help="Path to save the output WAV file.")
    parser.add_argument("--model", type=str, default="tts_models/en/ljspeech/tacotron2-DDC", help="TTS model to use (default: tacotron2-DDC).")
    args = parser.parse_args()

    # Load TTS model
    print(f"Loading model: {args.model}")
    tts = TTS(model_name=args.model)

    # Synthesize speech
    print(f"Synthesizing text: {args.text}")
    if args.reference_voice:
        tts.tts_to_file(
            text=args.text,
            speaker_wav=args.reference_voice,
            file_path=args.output
        )
    else:
        tts.tts_to_file(
            text=args.text,
            file_path=args.output
        )
    print(f"Audio saved to {args.output}")

if __name__ == "__main__":
    main()