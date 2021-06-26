import pytube
from pytube import YouTube
youtube = pytube.YouTube('https://youtu.be/rFQGdoGQGsI')
video = youtube.streams.first()
video.download('C:/Users/Ashwani/Desktop/pytube/')
