import youtube_dl

channel_url = "https://www.youtube.com/writethedocs"

options = {
    'verbose': True,
    'format': 'bestaudio[ext=m4a]',
    "restrictfilenames": True,
    "writeinfojson": True,
    "writeannotations": True,
    "outtmpl": "tmp/%(playlist)s/%(playlist_index)s - %(title)s/video.%(ext)s",
    "writethumbnail": True,
    "writesubtitles": True,
    "writeautomaticsub": True,
    "call_home": False,
    "ignoreerrors": True
}

ydl = youtube_dl.YoutubeDL(options)

ydl.download([channel_url])
