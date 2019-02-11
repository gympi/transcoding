import sys

import ffmpeg

from task import task


@task(
    name='multi-bitrate',
    title='Транскодирование видео с поддержкой мультибитрейта',
)
def multi_bitrate_video(input, output, time_off=0, size='320x240', count_frames=10, time_count=3):
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

        (ffmpeg.output(v1, a1, v2, v3, output,
                       **{'c:v': 'libx264', 'x264opts': "keyint=24:min-keyint=24:no-scenecut", 'r': 24, 'c:a': 'aac',
                          'b:a': '128k'},
                       **{'bf': 1, 'b_strategy': 0, 'sc_threshold': 0, 'pix_fmt': 'yuv420p'},

                       **{'b:v:0': '250k', 'filter:v:0': "scale=-2:240", 'profile:v:0': 'baseline'},
                       **{'b:v:1': '750k', 'filter:v:1': "scale=-2:480", 'profile:v:1': 'main'},
                       **{'b:v:2': '1500k', 'filter:v:2': "scale=-2:720", 'profile:v:2': 'high'}, )
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True))
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
