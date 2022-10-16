import glob
import json
import os
import pathlib
from slugify import slugify
import shutil


file_paths = glob.glob('tmp/**/video.info.json', recursive=True)

for file_path in file_paths:

    with open(file_path) as file:
        data = json.load(file)
        slug = slugify(data['title'])

        old_video_dir = os.path.dirname(file_path)
        new_video_dir = os.path.join("videos", slug)
        subtitles_dir = os.path.join(new_video_dir, "subtitles")

        pathlib.Path(subtitles_dir).mkdir(parents=True, exist_ok=True)

        file_renames = {
            "video.info.json": "video.json",
            "video.jpg": "thumbnail.jpg",
            "video.m4a": "audio.m4a",
            "video.en.vtt": os.path.join("subtitles", "youtube.en.vtt"),
        }

        for old_file_name in file_renames.keys():
            new_file_name = file_renames[old_file_name]
            shutil.copy(os.path.join(old_video_dir, old_file_name),
                        os.path.join(new_video_dir, new_file_name))
