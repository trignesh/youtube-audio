import pytube
import pydub

y=pytube.YouTube("https://www.youtube.com/watch?v=hGf8rOwFzvo&list=RDhGf8rOwFzvo&start_radio=1")
y.streams.filter(only_audio=True).get_audio_only().download("c:/test.mp3")


