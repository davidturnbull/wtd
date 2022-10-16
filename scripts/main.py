import youtube_dl

CHANNEL_URL = "https://www.youtube.com/c/WritetheDocs"

opts = {
    'verbose': True,
    # 'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    "restrictfilenames": True,
    "writeinfojson": True,
    "writeannotations": True,
    "writethumbnail": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    # "keepvideo": False,
    "call_home": False,
    "outtmpl": "tmp/%(title)s/video.%(ext)s",
    "ignoreerrors": True
}

with youtube_dl.YoutubeDL(opts) as yt:
    yt.download([CHANNEL_URL])
