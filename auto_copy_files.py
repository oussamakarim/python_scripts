from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_track):
			src = folder_track + "/" + filename
			new_destination = folder_destination + "/" + filename
			os.rename(src, new_destination)


folder_track = "C:/Users/ossam/Desktop/file1"
folder_destination = "C:/Users/ossam/Desktop/file2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_track, recursive= True)
observer.start()

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()