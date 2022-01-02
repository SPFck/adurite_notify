import urllib.request, time
from win10toast import ToastNotifier

toast = ToastNotifier()

print("We will notify when adurite is back!")
toast.show_toast("Thomas Shelby#9918","niggaflex is now Running!", duration=20, icon_path="icon.ico")

while True:
	try:
		urllib.request.urlopen("https://adurite.com/").getcode()
		toast.show_toast("Adurite","Adurite.com is back up!", duration=20, icon_path="icon.ico")
		exit()
	except:
		time.sleep(60)