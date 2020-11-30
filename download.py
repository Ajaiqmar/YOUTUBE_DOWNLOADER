import pytube

link=input("ENTER THE VIDEO LINK:").strip()

video=pytube.YouTube(link)

video.streams.filter(type="video").first().download()
print("DOWNLOADED!!")