import psutil
import requests
import time
# Calling psutil.cpu_precent() for 4 seconds
if _name=='main_':
    while True :
        try:
            hdd = psutil.disk_usage('/')
            ram=psutil.virtual_memory()
            url = "http://10.10.6.42:3030/dashboard/insert"
            payload='server=adobe.mukaap.ir&cpu='+str(psutil.cpu_percent(4))+'&storageSize='+str(hdd.total)+'&storageUsage='+str(hdd.used)+'&storageFree=5&ram='+str(psutil.virtual_memory().percent)
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            time.sleep(1)
            print(response.text)
        except:
            print('error')