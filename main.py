import os
import requests
from io import BytesIO
from PIL import Image
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse


import PySimpleGUI as sg
from pytube import YouTube

def remove_url_parameter(url, parameter):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if parameter in query_params:
        del query_params[parameter]

    updated_query_string = urlencode(query_params, doseq=True)
    parsed_url = parsed_url._replace(query=updated_query_string)

    new_url = urlunparse(parsed_url)
    return new_url

def normalize_youtube_url(url):
    url = remove_url_parameter(url, 't')
    if not url.startswith('https'):
        if not url.startswith('www.'):
           url = f'www.{url}'
        url = f'https://{url}'
    if 'youtu.be' in url:
        video_id = url.split('/')[-1]
        new_url = f'https://www.youtube.com/watch?v={video_id}'
        return new_url
    return url    

def get_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    ratio = 1 / 2
    image.thumbnail((int(720 * ratio), int(1280 * ratio)))
    thumb_data = BytesIO()
    image.save(thumb_data, format="PNG")
    thumb_data.seek(0)
    return thumb_data.read()

def progress_func(stream, chunk, bytes_remaining):
    print('Realizando download...')
    print(f'Stream filesize: {stream.filesize_mb} MB')
    print(f'Bytes remaining: {bytes_remaining} bytes')
    # print(f'Length chunk: {chunk}')
    print('----')
    
def complete_func(stream, *args):
    print(f'Download {stream.title} completo')

def get_video(link):
    youtube_video = YouTube(
    	link,
    	on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        use_oauth=False,
        allow_oauth_cache=True
    )
    return youtube_video

def download_audio(link):
    download_audio_dir = './downloads/audio/'
    youtube_video = get_video(link)
    stream = youtube_video.streams.filter(only_audio=True).first()
    print(f'Baixando {youtube_video.title}')
    try:
        out_file = stream.download(output_path=download_audio_dir)
        base, ext = os.path.splitext(out_file)
        filename = base + '.mp3'
        os.rename(out_file, filename)
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")
    
def download_video(link):
    download_video_dir = './downloads/video/'
    youtube_video = get_video(link)
    stream = youtube_video.streams.filter(file_extension='mp4').first()
    print(f'Baixando {youtube_video.title}')
    try:
        out_file = stream.download(output_path=download_video_dir)
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {e}")

def format_duration(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes:02d}:{seconds:02d}"

sg.theme('Purple')
link = 'https://www.youtube.com/watch?v=eWWWHilDBx8'

download_layout = [
    [sg.Text('Selecione o tipo de mídia:')],
    [sg.Radio('Vídeo MP4', 'MEDIA_TYPE', key='-VIDEO-'), sg.Radio('Áudio MP3', 'MEDIA_TYPE', default=True, key='-AUDIO-')],
    [sg.Button('Baixar'), sg.Button('Sair')]
]

search_layout = [
    [sg.Input(link, key='-URL-'), sg.Button('Buscar')],
    [sg.Text('Title: '),sg.Text(key='-TITLE-')],
    [sg.Text('Author: '),sg.Text(key='-AUTHOR-')],
    [sg.Text('Length: '),sg.Text(key='-LENGTH-')],
    [sg.Combo(['mp3', 'mp4'], key='-FORMAT-')],
    [sg.Image(key='-IMAGE-')],
]

layout = [[
    sg.Column(search_layout),
    sg.VSeperator(),
    sg.Column(download_layout),
]]

window = sg.Window('Download de Vídeo/Áudio', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break
    if event == 'Buscar':
        url = values['-URL-']
        print(url)
        yt = YouTube(url)
        window['-TITLE-'].update(yt.title)
        window['-AUTHOR-'].update(yt.author)
        window['-LENGTH-'].update(format_duration(yt.length))
        thumb_data = get_image_from_url(yt.thumbnail_url)
        window['-IMAGE-'].update(data=thumb_data)
    if event == 'Baixar':
        url = values['-URL-']
        media_type = 'video' if values['-VIDEO-'] else 'audio'
        if (media_type == 'video'):
            download_video(url)
        else:
            download_audio(url)
        sg.popup(f'{media_type.capitalize()} baixado com sucesso!')

window.close()

