from pytube import YouTube
import ffmpeg
def youtubeDownload(URL, resolution):
    usableResList = [144, 240, 360 ,480, 720]

    if resolution not in usableResList:

        print(f"The only usable resolutions are {usableResList}")
        exit()

    yt = YouTube(URL)

    stream = yt.streams.filter(res=f"{resolution}p", progressive=True).first()

    print(f"Downloading video: {yt.title}\nURL: {URL}")
    stream.download()

print("The YouTube video Downloader")

urlChoice = input("Type the URL of the video: ")
resChoice = int(input("Type the resolution of the video (without the 'p' example 360, 720 not 720p): "))

youtubeDownload(urlChoice, resChoice)