# Make sure you have ffmpeg and youtube_dl installed
# Edit 'path' to your music folder

import youtube_dl
import argparse
import sys
import os

path = ''


def download(bitrate: int, url: str, filename: str) -> None:
    audio_format = {
    'outtmpl': f'{path}/{filename}.webm',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': f'{bitrate}'
        }]
    }

    with youtube_dl.YoutubeDL(audio_format) as yc:
        yc.download([url])


def initiate() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='ytmp3',
                                     description='Convert and download music from youtube',
                                     epilog='Make sure you have ffmpeg and youtube_dl installed')
    parser.add_argument('quality',
                        type=int,
                        choices=[128, 192, 256, 320],
                        help='Quality of the audio')
    parser.add_argument('url',
                        type=str,
                        help='The link to the video')
    parser.add_argument('filename',
                        type=str,
                        help='The output filename')
    return parser.parse_args()


def main() -> None:
    args = initiate()
    download(args.quality, args.url, args.filename)

if __name__ == "__main__":
    main()
