# Ytmp3

A simple script for converting and downloading music from youtube

## Usage
```
usage: ytmp3.py [-h] {128,192,256,320} url filename
```
                                                     
positional arguments:                                
*  `{128,192,256,320}`  Quality of the audio            
*  `url`                The link to the video           
*  `filename`           The output filename             
                                                     
optional arguments:                                  
*  `-h`, `--help`       show this help message and exit 

## Example
```
ytmp3.py 320 https://www.youtube.com/watch?v=IKKar5SS29E 'Hoshimachi Suisei - Ghost'

```

## Installation
```
$pkg install git
$pkg install python
$pkg install youtube_dl
$pkg install ffmpeg
$git clone https://github.com/Galactic647/ytmp3
$cd ytmp3
$python ytmp3.py [-h] {128,192,256,320} url filename
```

## Editing path
If you want to change the path where the file gonna be store in, open the ytmp3.py file
with text editor and scrool at this section
```
import youtube_dl
import argparse
import sys
import os

path = ''
```
Change the `path` variable to your music folder. I haven't test this for android but
I'll try it as soon as I can.