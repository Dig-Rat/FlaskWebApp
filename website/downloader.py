#!/usr/bin/env/ python
import os
import yt_dlp
#from yt_dlp import YoutubeDL

# Method for downloading youtube videos given URL and format option.
def download_content(url, output_format):
    #optionAudio = 'bestaudio[ext=m4a]'
    #optionVideo = 'bestvideo+bestaudio'
    ydl_opts = {
        'format': output_format,
        'outtmpl': '%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        thumbnail_url = info.get('thumbnail')
        ydl.download([url])
        file_name = ydl.prepare_filename(info)
        if thumbnail_url:
            #thumbnail_file = file_name.rsplit('.', 1)[0] + '.jpg'

            # command is segmented for readability, should use a .confg maybe?
            ffmpeg_command = (
            f'ffmpeg -i "{file_name}" -i "{thumbnail_url}" '
            f'-map 0:a -map 1 -c:v copy -c:a copy '
            f'-map_metadata 0 -id3v2_version 3 '
            f'-metadata:s:v title="Album cover" '
            f'-metadata:s:v comment="Cover (front)" '
            f'-attach "{thumbnail_url}" '
            f'-metadata:s:t mimetype=image/jpeg '
            f'-metadata:s:t filename=cover.jpg '
            f'"{file_name}"'
            )
            os.system(ffmpeg_command)
    print('downloaded.')

# -i "{file_name}": Input flag indicating the input file name.
# -i "{thumbnail_url}": Another input file name (presumably a thumbnail).
# -map 0:a -map 1: Maps audio from the first input and all streams from the second input.
# -c:v copy -c:a copy: Copies video and audio codecs without re-encoding (preserving the original streams).
# -map_metadata 0 -id3v2_version 3: Maps metadata from the first input and specifies ID3v2 version 3 for metadata.
# -metadata:s:v title="Album cover": Sets the title metadata for video streams.
# -attach "{thumbnail_url}": Attaches an external image file as metadata.
# -metadata:s:t mimetype=image/jpeg -metadata:s:t filename=cover.jpg: Specifies metadata for the attached thumbnail.
# "{file_name}": Output file name (presumably the modified or processed file).

if __name__ == "__main__":
#    main()
    print('script done')
