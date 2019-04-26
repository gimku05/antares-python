# Antares Python
This is a Python library to simplify the connection to Antares IoT Platform. For more information about the platform itself, please visit the [official site](https://antares.id).  

## Installation
Make sure you have Python and pip installed.
```
pip install antares-http
```

### Usage Example
```python
from antares_http import antares

antares.setAccessKey('your-access-key', debug=True)

myData = {
    'temp' : 77,
    'windsp' : 10
}

antares.send(myData, 'your-project-name', 'your-device-name', debug=True)
```

### API Reference
TODO
