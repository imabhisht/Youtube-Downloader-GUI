from pytube import YouTube
import requests
import shutil
import os
import convert

def convert_timestamp(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def convert_viewcount(count_temp):
    if len(count_temp)> 9:
        try_count = int(count_temp)/1000000000
        try_count = str(try_count)[:3]
        try_count = try_count + "B"

    elif len(count_temp)> 6:
        try_count = int(count_temp)/1000000
        try_count = str(try_count)[:3]
        try_count = try_count + "M"

    elif len(count_temp)> 3:
        try_count = int(count_temp)/1000
        try_count = str(try_count)[:4]
        try_count = try_count + "K"


    else:
        try_count = int(count_temp)/1
        try_count = str(try_count)[:3]
        try_count = try_count + ""

    return try_count

def metadata():
    global title
    global author
    global thumbnail_link
    global views_count
    global size_preview
    calculate = video.length
    size_preview = convert_timestamp(calculate)
    title = video.title
    author = video.author
    temp_count = str(video.views)
    views_count = convert_viewcount(temp_count)    
    thumbnail_link = video.thumbnail_url
    resp = requests.get(thumbnail_link, stream=True)
    local_file = open(r'Cache\local_image.jpg', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp
    return title,author,views_count,size_preview

def download(revol):
    print(revol)
    try:
        cache_output = (r"Cache")
    except:
        os.mkdir("Cache")
        cache_output = (r"Cache")

    video_filename = (title+"(video)")
    audio_filename = (title+"(audio)")
    stream = video.streams.filter(res=revol).first()
    audio = video.streams.filter(only_audio=True).first()
    stream.download(filename=video_filename,output_path=cache_output)
    audio.download(filename=audio_filename,output_path=cache_output)

def compiling_files(path_save):
    video_filename = (title+"(video)"+".mp4")
    audio_filename = (title+"(audio)"+".mp4")
    convert.Processing(audio_filename,video_filename,path_save,title)


def get_video():
    global video
    video = YouTube(url)

def get_resolutions():
    global resolutions_list
    resolutions_list = []
    for x in video.streams.filter(file_extension='mp4'):
        check = (x.resolution)
        if check == None:
            pass
        else:
            resolutions_list.append(check)
    resolutions_list.pop(0)
    print(resolutions_list)
    return resolutions_list


def check_url(input_url):
    global video
    global url
    url = input_url
    try:
        video = YouTube(url)
        return "correct"
        
    except:
        return "incorrect"

