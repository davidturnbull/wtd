import glob
import whisper
import os
import json
import pathlib


def transcribe(model_name='tiny'):
    # Get all the MP3s
    file_paths = glob.glob('tmp/**/*.m4a', recursive=True)

    print(f'Transcribing {len(file_paths)} files with model "{model_name}".')

    for file_path in file_paths:
        print(f"Transcribing {file_path}...")

        # Transcribe the file
        model = whisper.load_model(model_name)
        result = model.transcribe(file_path, verbose=False)

        # Get the directory of the current video
        video_dir = os.path.dirname(file_path)
        subtitles_dir = os.path.join(video_dir, "subtitles")

        # Create the "subtitles" directory if it doesn't exist
        pathlib.Path(subtitles_dir).mkdir(parents=True, exist_ok=True)

        # Save transcribed text
        text_file = f"whisper-{model_name}.en.txt"
        text_path = os.path.join(subtitles_dir, text_file)
        text_content = result['text']

        with open(text_path, 'w') as file:
            file.write(text_content)

        # Save transcribed text (with timecodes)
        segments_file = f"whisper-{model_name}.en.json"
        segments_path = os.path.join(subtitles_dir, segments_file)
        segments_content = json.dumps(result['segments'])

        with open(segments_path, 'w') as file:
            file.write(segments_content)


transcribe("tiny")
