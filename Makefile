all: desktop_entry
	python2 webapp.py 8783 &
	cp build/youtube_downloader.desktop ~/.config/autostart
desktop_entry:
	python2 build/build.py