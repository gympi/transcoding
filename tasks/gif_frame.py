import sys
import ffmpeg

from task import task


@task(
    name='gif-frame',
    title='Создание gif видео',
)
def gif_frame(input, output, time_off=0, size='320x240', count_frames=10, time_count=3):
    """
    ffmpeg -t 1 -ss 0.5 -i [input-file.mp4] -r 10 -s '320x240' [output-file.gif]
    """
    try:
        (ffmpeg
         .input(input)
         .output(output, ss=time_off, vframes=1, s=size, r=count_frames, t=time_count)
         .overwrite_output()
         .run(capture_stdout=True, capture_stderr=True)
         )
    except ffmpeg.Error as e:
        print(e.stderr.decode(), file=sys.stderr)
        sys.exit(1)
