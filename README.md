# kuvat-api

kuvat-api is a Python library for site kuvat.fi.

## Installation

```
$ pip install git+https://github.com/Nikotiin/kuvat-api@v0.2
```

## Documentation

See https://nikotiin.github.io/kuvat-api/

## Usage

```python
from kuvat_api import Client

# Initialize client
client = Client("https://example.kuvat.fi")

# Get all directories
directories = client.get_directories()

# Get list of images
directory = directories[0]
images = directory.get_files()

# Save images
for image in images:
   image.save("pictures/" + image.name)
```