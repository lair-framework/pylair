import requests
from requests.auth import HTTPBasicAuth
from warnings import filterwarnings
import json

VERSION = "1.0"

_api = '/api/projects/'

# Class used to define options used for interacting with Lair api server
# Must define:
#   username
#   password
#   host
#   project_id
# Optional:
#   force_ports - defaults to False.
#   scheme - defaults to 'https'
#   insecure_skip_verify - defaults to False. Determines whether to ignore invalid SSL cert.
#
# See 'README.md' for an example on how to use this library
#
class Options:
    def __init__(self,
                 username,
                 password,
                 host,
                 project_id,
                 scheme='https',
                 insecure_skip_verify=False,
                 force_ports=False):
        self.username = username
        self.password = password
        self.host = host
        self.project_id = project_id
        self.scheme = scheme
        self.insecure_skip_verify = insecure_skip_verify
        if insecure_skip_verify:
            filterwarnings('ignore', 'Unverified HTTPS request')

        if self.username == '':
            raise Exception('Missing required value: username')

        if self.password == '':
            raise Exception('Missing required value: password')

        if self.host == '':
            raise Exception('Missing required value: host')

        if self.project_id == '':
            raise Exception('Missing required value: project_id')

        if self.scheme == '' or self.scheme not in ['http', 'https']:
            raise Exception('Missing or invalid value: scheme')

# Function that performs the actual project import. Returns a 'lair_response' object
def import_project(project, opts):
    u = opts.scheme + '://' + opts.host + _api + opts.project_id
    r = requests.patch(
            url=u,
            auth=HTTPBasicAuth(opts.username, opts.password),
            data=json.dumps(project),
            headers={'Content-Type': 'application/json'},
            verify=not (opts.insecure_skip_verify and opts.insecure_skip_verify))

    rjson = r.json()
    ret = dict(lair_response)
    ret['status'] = rjson['Status']
    ret['message'] = rjson['Message']

    return ret

# Function that performs project export. Returns a json string
def export_project(opts):
    u = opts.scheme + '://' + opts.host + _api + opts.project_id
    r = requests.get(
            url=u,
            auth=HTTPBasicAuth(opts.username, opts.password),
            headers={'Content-Type': 'application/json'},
            verify=not (opts.insecure_skip_verify and opts.insecure_skip_verify))

    return r.json()

# Dictionary used to represent the response from the Lair API server
lair_response = {
    'status': '',
    'message': ''
}

