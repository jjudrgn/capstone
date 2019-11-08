import urllib.request
try:
    url = 'http://203.254.143.164:8080/database/newdata/urllib@is@good'
    urllib.request.urlopen(url)
    print('wifi on')
except:
    print('wifi off')        