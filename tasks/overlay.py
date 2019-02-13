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
    'image_overlay': {
        'type': str,
        'required': True,
        'help': 'Image overlay input file path',
    },
    'position': {
        'type': str,
        'regex': r"\d+:\d+",
        'required': True,
        'help': 'Image overlay position',
    },
}


@task(
    name='overlay',
    title='Наложить картинку на видео',
    validator=validator
)
def overlay(input, output, image_overlay, position):
    """
    ffmpeg -i ./resources/24cbad87b8d4453b905a9f4865d96acb.mp4 -i ./resources/png-2093542_960_720.png \
        -filter_complex "[0:v][1:v] overlay=25:25" \
        -pix_fmt yuv420p -c:a copy \
        output.mp4
    """
    overlay_file = ffmpeg.input(image_overlay)
    try:
        x, y = position.split(':')
        (ffmpeg
         .input(input)
         .overlay(overlay_file, x=x, y=y)
         .output(output).overwrite_output().run(capture_stdout=True, capture_stderr=True))
    #     .get_args()
    #     .overwrite_output().run(capture_stdout=True, capture_stderr=True)
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
