import os 	

current = os.getcwd()
parent = "/".join(current.split("/")[:-1])
path = os.path.join(parent, "webapp.py")
print(path)

s = """[Desktop Entry]
Type=Application
Exec=python2 %s  8783
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_IN]=YoutubeDownloaderStartupScript
Name=YoutubeDownloaderStartupScript
Comment[en_IN]=
Comment=
"""%(path)
print(s)
with open("build/youtube_downloader.desktop", "w") as f:
	f.write(s)
f.close()
