from pylair.models import *
from pylair.client import *

def main():
    #
    # Replace the following line with code to parse any necessary command line
    # args, get the LAIR_API_SERVER info from env var (parsing accordingly), and
    # set the project_id value of the project you would like to export
    project_id = 'ABCDEF0123456789'

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

if __name__ == '__main__':
    main()
