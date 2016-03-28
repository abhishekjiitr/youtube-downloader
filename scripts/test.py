import subprocess
test = subprocess.Popen(["ping","-W","2","-c", "1", "192.168.1.70"], stdout=subprocess.PIPE)
output = test.communicate()[0]
print(output)