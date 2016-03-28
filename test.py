import json
import os.path
with open('config/config.json') as data_file:    
    data = json.load(data_file)
location = data['location']
loc = os.path.join(location, "tatle")
print(loc)
