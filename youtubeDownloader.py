from pytube import YouTube 

print("#####Coding Legends######")
while(1):
	try:
		url = input('Enter Youtube link:- ')
		youtube = YouTube(url)
		break
	except:
		print("Network error or Invalid Url..")
resolutions = set()
#video= youtube.streams.first()
for i in youtube.streams:
	resolutions.add(i.resolution)
	
while(1):
	print("Available resolutions: "+ str(resolutions))
	choice = input("Enter a valid resolution:")
	if choice in resolutions:
		break
print("Download started")
youtube.streams.filter(res=choice).first().download("/storage/emulated/0/Download/Python script/")
#video.streams.get_highest_resolution().download()
#video.download("/storage/emulated/0/Download/Python script")
print("Video Downloaded Successfully...")
print("Follow @codinglegends in Instagram for further similar videos.")