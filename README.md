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
$pkg install ffmpeg
$pip install youtube_dl
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
Change the `path` variable to your music folder.

On termux if the `path` were unchanged it will give a `Read-only file system` error.
to fix that change the path to your music folder or change it into
```
/data/data/com.termux/files/home/
```
to solve the error
