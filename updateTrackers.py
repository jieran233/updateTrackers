import requests
CONFFILE = "/home/pi/aria2-config/aria2.conf"
conf = open(CONFFILE, 'r', encoding='utf-8').read()
confLine = conf.splitlines()
trackers = ''
try:
    trackers = requests.get(url='http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt').text
except Exception as e:
    print('\033[0;31m' + str(e.args) + '\033[0m')
# print(trackers)
trackersLine = trackers.splitlines()
trackers = ''
mx = len(trackersLine)
for i in range(0, mx):
    if i == mx-1:
        trackers = trackers + trackersLine[i]
    else:
        trackers = trackers + trackersLine[i] + ','
print(trackers)
confLine[len(confLine)-1] = 'bt-tracker=' + trackers
conf = ''
mx = len(confLine)
for i in range(0, mx):
    if i == mx - 1:
        conf = conf + confLine[i]
    else:
        conf = conf + confLine[i] + '\n'
# print(conf)
f = open(CONFFILE, 'w', encoding='utf-8').write(conf)
