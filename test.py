from antares_http import antares

projectName = 'weather-station'
deviceName = 'station1'

antares.setAccessKey('b4e89ce2436b9d90:202c7b14b849c084')

dataToSend = {
    'temp' : 77,
    'windsp' : 10
}

# Get latest data
# latestData = antares.get(projectName, deviceName, debug=True)

# Get all data
# allData = antares.getAll(projectName, deviceName, limit=10, debug=True)

# Get only data IDs
# allDataId = antares.getAllId(projectName, deviceName, debug=True)

# Send data
# sentData = antares.send("hello", projectName, deviceName, debug=True)

# Get devices
# devices = antares.getDevices(projectName)
