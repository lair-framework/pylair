# pylair #

pylair is a Python library used to interact with the Lair 2.0 API

## Installation ##

1. Download the binary distribution from [here](https://github.com/lair-framework/pylair/releases/latest).
2. Install it with pip:

```
$ sudo pip install pylair-<version>.tar.gz
```

## Examples ##

Using the library is simple. Just import the pylair module, setup options, and call the import functions to import a project.

~~~~python
from pylair.models import *
from pylair.client import *

def main():
    #
    # Replace the following two lines with code to parse the necessary command line
    # args, get the LAIR_API_SERVER info from env var (parsing accordingly), and
    # parse the data file to build a valid 'project' dict (see models.py)
    project_id = 'ABCDEFG1234567890'
    p = dict(project)

    # Build your options
    opts = Options('lairuser', 'lairpassword', 'localhost:8888', project_id, scheme='http')

    # Make the call to import the project
    res = import_project(project, opts)

    # Inspect the response
    if res['status'] == 'Error':
        print "Error: " + res['message']
    else:
        print "Success!"

if __name__ == '__main__':
    main()
~~~~

Similar steps can be taken to export a project.

~~~~python
from pylair.models import *
from pylair.client import *

def main():
    #
    # Replace the following line with code to parse any necessary command line
    # args, get the LAIR_API_SERVER info from env var (parsing accordingly), and
    # set the project_id value of the project you would like to export
    project_id = 'ABCDEFG1234567890'

    # Build your options
    opts = Options('lairuser', 'lairpassword', 'localhost:8888', project_id, scheme='http')

    # Make the call to export the project. If successful, 'res' variable will contain a json
    # string of the project that was exported.
    res = export_project(opts)

    # Inspect the response. A 'status' key indicates failure
    if 'status' in res:
        print "Error: " + res['message']
        return
    else:
        print "Success!"

    # Do something with 'res' here

if __name__ == '__main__':
    main()
~~~~
