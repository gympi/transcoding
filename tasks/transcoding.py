import ffmpeg

from task import task


@task(
    name='transcoding',
    title='Транскодирование видео из mov в mp4',
)
def transcoding(input, output):
    (ffmpeg
     .input(input)
     .output(output, vcodec='copy', acodec='copy')
     .overwrite_output()
     .run()
     )
