import glob
import whisper
import os
import json
import pathlib

VALID_MODEL_NAMES = ['tiny', 'small', 'medium', 'large']
VALID_LANGUAGES = ['en']


def transcribe_audio_file(speech_to_text_model, file_path, language):
    result = speech_to_text_model.transcribe(
        file_path, language=language, verbose=False)
    return result


def save_transcription_results(results, audio_dir, model_name, language):
    subtitles_dir = os.path.join(audio_dir, "subtitles")
    pathlib.Path(subtitles_dir).mkdir(parents=True, exist_ok=True)

    text_file = f"whisper-{model_name}.{language}.txt"
    text_path = os.path.join(subtitles_dir, text_file)
    text_content = results['text']
    with open(text_path, 'w') as file:
        file.write(text_content)

    segments_file = f"whisper-{model_name}.{language}.json"
    segments_path = os.path.join(subtitles_dir, segments_file)
    segments_content = json.dumps(results['segments'])
    with open(segments_path, 'w') as file:
        file.write(segments_content)


def transcribe_audio_files(dir, model_name='tiny', language='en'):
    # Validate the input
    if model_name not in VALID_MODEL_NAMES:
        raise ValueError(
            f"Invalid model name: {model_name}. Valid options are: {', '.join(VALID_MODEL_NAMES)}")
    if language not in VALID_LANGUAGES:
        raise ValueError(
            f"Invalid language: {language}. Valid options are: {', '.join(VALID_LANGUAGES)}")

    # Get the file paths for all .m4a files in the audio directory
    file_paths = glob.glob(os.path.join(dir, '**/*.m4a'), recursive=True)

    print(f'Transcribing {len(file_paths)} files with "{model_name}" model...')

    for file_path in file_paths:
        audio_dir = os.path.dirname(file_path)
        subtitles_dir = os.path.join(audio_dir, "subtitles")
        text_file = f"whisper-{model_name}.{language}.txt"
        text_path = os.path.join(subtitles_dir, text_file)

        # Check if transcription already exists
        if os.path.exists(text_path):
            print(f"[✔] {file_path}")
            continue

        print(f"Transcribing {file_path}...")
        try:
            # Load the model and transcribe the audio file
            model = whisper.load_model(model_name)
            results = transcribe_audio_file(model, file_path, language)
        except Exception as e:
            # Log the error and move on to the next file
            print(f"Error transcribing {file_path}: {e}")
            continue

        # Save the transcription results
        save_transcription_results(results, audio_dir, model_name, language)


transcribe_audio_files("./tmp", "medium")
