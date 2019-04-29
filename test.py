from antares_http import antares
import sys
import random

projectName = 'weather-station'
deviceName = 'station1'

antares.setDebug(True)
antares.setAccessKey('b4e89ce2436b9d90:202c7b14b849c084')

dataToSend = {
    'temp' : random.randint(20, 32),
    'windsp' : random.randint(5, 15)
}

# Get latest data
# latestData = antares.get(projectName, deviceName)

# Get all data
# allData = antares.getAll(projectName, deviceName, limit=10)

# Get only data IDs
# allDataId = antares.getAllId(projectName, deviceName, limit=50)

# Get specific data 
# specificData = antares.getSpecific(projectName, deviceName, 'cin_201898641')

# Get device ID
# deviceId = antares.getDeviceId(projectName, deviceName)

# Send by Device ID 
# sentByDevice = antares.sendById(dataToSend, 'cnt-478686259')

# Send data
# sentData = antares.send("hello", projectName, deviceName)

# Get devices
# devices = antares.getDevices(projectName)

# Create device
# createdDevice = antares.createDevice(projectName, 'python-device');
