import ffmpeg

from libs.task import task


@task(
    name='overlay',
    title='Наложить картинку на видео',
)
def overlay(input, output, image_overlay):
    (ffmpeg
     .input(input)
     .overlay(image_overlay)
     .output(output)
     .overwrite_output()
     .run()
 )
