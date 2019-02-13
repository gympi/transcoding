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
    'scale': {
        'type': str,
        'regex': r"^\d+:\d+:\d+$",
        'default': '240:480:720',
        'required': True,
        'help': 'Size output gif',
    },
}


@task(
    name='multi-bitrate',
    title='Транскодирование видео с поддержкой мультибитрейта',
    validator=validator
)
def multi_bitrate_video(input, output, scale):
    """
    ffmpeg -y -i 24cbad87b8d4453b905a9f4865d96acb.mp4 \
      -c:v libx264 -x264opts "keyint=24:min-keyint=24:no-scenecut" -r 24 \
      -c:a aac -b:a 128k \
      -bf 1 -b_strategy 0 -sc_threshold 0 -pix_fmt yuv420p \
      -map 0:v:0 -map 0:a:0 -map 0:v:0 -map 0:v:0 \
      -b:v:0 250k  -filter:v:0 "scale=-2:240" -profile:v:0 baseline \
      -b:v:1 750k  -filter:v:1 "scale=-2:480" -profile:v:1 main \
      -b:v:2 1500k -filter:v:2 "scale=-2:720" -profile:v:2 high \
      sample_dash.mp4
    """
    try:
        i = ffmpeg.input(input)
        v1 = i['v:0']
        a1 = i['a:0']
        v2 = i['v:0']
        v3 = i['v:0']

        scale_1, scale_2, scale_3 = scale.split(':')

        (ffmpeg.output(v1, a1, v2, v3, output,
                       **{'c:v': 'libx264', 'x264opts': "keyint=24:min-keyint=24:no-scenecut", 'r': 24, 'c:a': 'aac',
                          'b:a': '128k'},
                       **{'bf': 1, 'b_strategy': 0, 'sc_threshold': 0, 'pix_fmt': 'yuv420p'},

                       **{'b:v:0': '250k', 'filter:v:0': "scale=-2:{}".format(scale_1), 'profile:v:0': 'baseline'},
                       **{'b:v:1': '750k', 'filter:v:1': "scale=-2:{}".format(scale_2), 'profile:v:1': 'main'},
                       **{'b:v:2': '1500k', 'filter:v:2': "scale=-2:{}".format(scale_3), 'profile:v:2': 'high'}, )
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True))
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
