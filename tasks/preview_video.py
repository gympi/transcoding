import sys
import ffmpeg

from libs.task import task


validator = {
    'input': {
        'type': str,
        'required': True,
        'help': 'Input file path',
    },
    'output': {
        'type': str,
        'required': True,
        'help': 'Output file path',
    },
    'start_seconds': {
        'type': int,
        'required': True,
        'default': 5,
        'help': 'Time start',
    },
    'count_frames': {
        'type': int,
        'required': True,
        'default': 10,
        'help': 'Count frames output gif',
    },
    'duration': {
        'type': int,
        'default': 5,
        'help': 'Duration output gif',
    },
    'vframes': {
        'type': int,
        'required': True,
        'default': 1,
        'help': 'Output a single frame from the video into an image file',
    },
    'size': {
        'type': str,
        'regex': r"\d+x\d+",
        'required': True,
        'help': 'Size output gif',
    },
}


@task(
    name='preview-video',
    title='Генерация превью видео ролика',
    validator=validator
)
def preview_video(input, output, start_seconds=0, size='320x240', count_frames=10, duration=3, vframes=1):
    """
    ffmpeg -i 24cbad87b8d4453b905a9f4865d96acb.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output-file.webm
    """
    try:
        (ffmpeg
         .input(input)
         .output(output, ss=start_seconds, vframes=vframes, s=size, r=count_frames, t=duration)
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True)
         )
        return output
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
