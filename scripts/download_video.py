import json, os.path

import sys
import subprocess

with open('config/config.json') as data_file:    
    data = json.load(data_file)
location = data['location']
print(location)


URL = sys.argv[1]
l = len(sys.argv)
title = sys.argv[2:]
title = " ".join(title)
print(title, URL)
abso = location+'/' +title;
print(abso)
path = os.path.join(location, title)
test = subprocess.Popen(["youtube-dl", URL, "-o", path], stdout=subprocess.PIPE)
output = test.communicate()[0]
print(output)
