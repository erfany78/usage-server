import psutil
import eventlet
import socketio
import requests
import time
# Calling psutil.cpu_precent() for 4 seconds
if __name__ == "__main__":
    while True :
        hdd = psutil.disk_usage('/')
        url = "http://back.mkbedu.ir/dashboard/insert"
        payload='server=adobe.mukaap.ir&cpu='+str(psutil.cpu_percent(4))+'&storageSize='+str(hdd.total)+'&storageUsage='+str(hdd.used)+'&storageFree=5&ram=2'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        time.sleep(120)
        print(response.text)