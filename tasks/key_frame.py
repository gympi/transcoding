import sys
import ffmpeg

from task import task


@task(
    name='key-frame',
    title='Создание ключевого кадра',
)
def key_frame(input, output, time_off=0, size='320x240'):
    """
    ffmpeg -ss 1 -i 24cbad87b8d4453b905a9f4865d96acb.mp4 -frames:v 1 -s 320x240 ./thumb4.jpg
    """
    try:
        (ffmpeg
         .input(input)
         .output(output, ss=time_off, vframes=1, s=size)
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True)
         )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
