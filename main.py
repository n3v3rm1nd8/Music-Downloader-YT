import sys, signal
import yt_dlp as youtube_dl
from pytube import Playlist

def ctrl_c(sig, frame):
    print("\n" + "[!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

if len(sys.argv) < 2 or sys.argv[1] == "":
    print("[!] Introduce el ID de la playlist")
    sys.exit(1)
else:
    url = "https://www.youtube.com/playlist?list=" + sys.argv[1]
    pl = list(Playlist(url))
    lastID = 0

    with open("videoID.txt", 'r') as fichero:
        lastID = int(fichero.read())

    videos = pl[lastID:]

    for video in videos:

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',  # Máxima calidad para mayor tamaño de archivo
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(video)
            
            with open("videoID.txt", 'w') as fichero:
                fichero.write(str(len(pl)))
        except Exception as e:
            print("\n" + "[DESCARGAR MANUAL] -> " + video + "\n")
            pass