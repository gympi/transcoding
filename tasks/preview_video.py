import sys
import ffmpeg

from libs.task import task


@task(
    name='preview-video',
    title='Генерация превью видео ролика',
)
def preview_video(input, output, time_off=0, size='320x240', count_frames=10, time_count=3):
    """
    ffmpeg -i 24cbad87b8d4453b905a9f4865d96acb.mp4 -c:v libvpx -crf 10 -b:v 1M -c:a libvorbis output-file.webm
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
