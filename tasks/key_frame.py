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
    name='key-frame',
    title='Создание ключевого кадра',
    validator=validator
)
def key_frame(input, output, start_seconds=0, vframes=1, size='320x240'):
    """
    ffmpeg -i [input-file.mp4] -ss 1 -frames:v 1 -s 320x240 [output-file.jpg]
    """
    try:
        (ffmpeg
         .input(input)
         .output(output, ss=start_seconds, vframes=vframes, s=size)
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True)
         )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
