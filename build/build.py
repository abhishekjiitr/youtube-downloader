import os 	

path = os.path.join(os.getcwd(), "main.sh")
print(path)

s = """[Desktop Entry]
Type=Application
Exec=bash %s
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
