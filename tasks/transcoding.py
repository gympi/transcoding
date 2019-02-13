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
}


@task(
    name='transcoding',
    title='Транскодирование видео из mov в mp4',
    validator=validator
)
def transcoding(input, output):
    try:
        (ffmpeg
         .input(input)
         .output(output, vcodec='copy', acodec='copy')
         .overwrite_output()
         .run()
         )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
