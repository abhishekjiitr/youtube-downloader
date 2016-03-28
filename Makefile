all: desktop
	cp build/youtube_downloader.desktop ~/.config/autostart
desktop:
	python2 build/build.py