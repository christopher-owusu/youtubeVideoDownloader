import pytube
link = "https://www.youtube.com/watch?v=pEXDyn3uC3o" 
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()