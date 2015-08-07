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
