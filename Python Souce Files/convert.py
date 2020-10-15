import os
import ffmpeg


def Processing(audio_filename,video_filename,path_save,title):
    video_location = os.path.join("Cache",video_filename)
    audio_location = os.path.join("Cache",audio_filename)
    output_location = path_save + title + ".mp4"
    video_stream = ffmpeg.input(video_location)
    audio_stream = ffmpeg.input(audio_location)
    ffmpeg.output(audio_stream, video_stream, output_location).run()
    os.remove(video_location)
    os.remove(audio_location)
    os.remove(r"Cache\local_image.jpg")
