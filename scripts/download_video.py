import sys
import subprocess


URL = sys.argv[1]
l = len(sys.argv)
title = sys.argv[2:]
title = " ".join(title)
print(title, URL)

test = subprocess.Popen(["youtube-dl", URL], stdout=subprocess.PIPE)
output = test.communicate()[0]
print(output)
