from pytube import YouTube
import ffmpeg

def youtubeDownload(URL, resolution, audioOnly):
    usableResList = [144, 240, 360 ,480, 720]

    if resolution not in usableResList:

        print(f"The only usable resolutions are {usableResList}")
        input()
        exit()

    yt = YouTube(URL)

    if audioOnly:
        audioStream = yt.streams.filter(only_audio=True).first()

        print(f"Downloading video: {yt.title}\nURL: {URL}")
        audioStream.download()
    else:
        stream = yt.streams.filter(res=f"{resolution}p", progressive=True).first()

        print(f"Downloading video: {yt.title}\nURL: {URL}")
        stream.download()

def showVideoStats(URL):
    yt = YouTube(URL)

    print(f"The video title: {yt.title}")
    print(f"The video author is {yt.author}")
    print(f"The video has {yt.views} views")
    print(f"The video has {yt.length} seconds")
    print(f"The video has a {yt.rating} rating")

print("Main Menu")
print("1. Video Downloader")
print("2. Show video Stats")

optionChoice = input("Choose: ")

if optionChoice == "1":
    print("The YouTube video Downloader")

    urlChoice = input("Type the URL of the video: ")
    resChoice = int(input("Type the resolution of the video (without the 'p' example 360, 720 not 720p): "))

    audioChoice = input("Do you want to download only audio (no/yes): ")

    if audioChoice == "yes" or audioChoice == "yes".capitalize:
        youtubeDownload(urlChoice, resChoice, True)
    elif audioChoice == "no" or audioChoice == "no".capitalize:
        youtubeDownload(urlChoice, resChoice, False)
    else:
        print("The choice is wrong")
elif optionChoice ==  "2":
    print("YouTube video statistics")

    urlChoice = input("Type the URL of the video: ")

    showVideoStats(urlChoice)
else:
    print("The choice is wrong: ")