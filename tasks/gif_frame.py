import argparse
import re
import sys
import ffmpeg

from task import task


def validator():
    parser = argparse.ArgumentParser(description='API для транскодирования файлов')

    parser.add_argument('--input', '-i',
                        dest='input',
                        type=str,
                        help='Input file path',
                        required=True,
                        )

    parser.add_argument('--output', '-o',
                        dest='output',
                        type=str,
                        help='Output file path',
                        required=True,
                        )

    parser.add_argument('--start-seconds', '-ss',
                        dest='start_seconds',
                        type=int,
                        default=5,
                        help='Time start',
                        required=True,
                        )

    parser.add_argument('--count-frames', '-cf',
                        dest='count_frames',
                        type=int,
                        default=10,
                        help='Count frames output gif',
                        required=True,
                        )

    def size(s, pat=re.compile(r"\d+x\d+")):
        if not pat.match(s):
            raise argparse.ArgumentTypeError
        return s

    parser.add_argument('--size', '-s',
                        dest='size',
                        type=size,
                        help='Size output gif',
                        required=True,
                        )

    parser.add_argument('--duration', '-d',
                        dest='duration',
                        type=int,
                        default=5,
                        help='Duration output gif',
                        required=True,
                        )

    return parser


@task(
    name='gif-frame',
    title='Создание gif видео',
    validator=validator()
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
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
