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
    'size': {
        'type': str,
        'regex': r"\d+x\d+",
        'required': True,
        'help': 'Size output gif',
    },
    'duration': {
        'type': int,
        'default': 5,
        'help': 'Duration output gif',
    }
}


@task(
    name='gif-frame',
    title='Создание gif видео',
    validator=validator
)
def gif_frame(input, output, start_seconds=0, size='320x240', count_frames=10, duration=3):
    """
    ffmpeg -t 1 -ss 0.5 -i [input-file.mp4] -r 10 -s '320x240' [output-file.gif]
    """
    try:
        (ffmpeg
         .input(input)
         .output(output, ss=start_seconds, vframes=1, s=size, r=count_frames, t=duration)
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True)
         )
        return output
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
