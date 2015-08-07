
# Constants
VERSION = '2.0'
STATUS_GREY = 'lair-grey'
STATUS_BLUE = 'lair-blue'
STATUS_GREEN = 'lair-greeen'
STATUS_ORANGE = 'lair-orange'
STATUS_RED = 'lair-red'
STATUS_MAP = [STATUS_GREY, STATUS_BLUE, STATUS_GREEN, STATUS_ORANGE, STATUS_RED]
PROTOCOL_TCP = 'tcp'
PROTOCOL_UDP = 'udp'
PROTOCOL_ICMP = 'icmp'
PRODUCT_UNKNOWN = 'unknown'
SERVICE_UNKNOWN = 'unknown'
RATING_HIGH = 'high'
RATING_MEDIUM = 'medium'
RATING_LOW = 'low'

# Main dictionary used to relate all data
project = {
    '_id': '',
    'name': '',
    'industry': '',
    'createdAt': '',
    'description': '',
    'owner': '',
    'contributors': [],         # List of strings
    'commands': [],             # List of 'command' items
    'notes': [],                # List of 'note' items
    'droneLog': [],             # List of strings
    'tool': '',
    'hosts': [],                # List of 'host' items
    'issues': [],               # List of 'issue' items
    'authInterfaces': [],       # List of 'auth_interface' items
    'netblocks': [],            # List of 'netblock' items
    'people': [],               # List of 'person' items
    'credentials': []           # List of 'credential' items
}

# Represents a single host
host = {
    '_id': '',
    'projectId': '',
    'longIpv4Addr': 0,          # Integer version of IP address
    'ipv4': '',                 
    'mac': '',
    'hostnames': [],            # List of strings
    'os': dict(),               # 'os' item
    'notes': [],                # List of 'note' items
    'statusMessage': '',        # Used to label host in Lair, can be arbitrary
    'tags': [],                 # List of strings
    'status': '',               # See the STATUS_* constants for allowable strings
    'lastModifiedBy': '',
    'isFlagged': False,
    'files': [],                # List of 'file' items
    'webDirectories': [],       # List of 'web_directory' items
    'services': []              # List of 'service' items
}

# Represents a single service/port
service = {
    '_id': '',
    'projectId': '',
    'hostId': '',
    'port': 0,
    'protocol': PROTOCOL_TCP,   # See the PROTOCOL_* constants for allowable strings
    'service': '',
    'product': '',
    'status': '',               # See the STATUS_* constants for allowable strings
    'isFlagged': False,
    'lastModifiedBy': '',
    'notes': [],                # List of 'note' items
    'files': [],                # List of 'file' items
}

# Represents a single issue
issue = {
    '_id': '',
    'projectId': '',
    'title': '',
    'cvss': 0.0,
    'rating': '',               # See the RATING_* constants for allowable strings
    'isConfirmed': False,
    'description': '',
    'evidence': '',
    'solution': '',
    'hosts': [],                # List of 'issue_host' items
    'pluginIds': [],            # List of 'plugin_id' items
    'cves': [],                 # List of strings
    'references': [],           # List of 'issue_reference' items
    'identifiedBy': dict(),     # 'identified_by' object
    'isFlagged': False,
    'status': '',               # See the STATUS_* constants for allowable strings
    'lastModifiedBy': '',
    'notes': [],                # List of 'note' items
    'files': []                 # List of 'file' items
}

# Represents an authentication interface
auth_interface = {
    '_id': '',
    'projectId': '',
    'isMultifactor': False,
    'kind': '',                 # What type of interface (e.g. Cisco, Juniper)
    'url': '',
    'description': ''
}

# Represents a single netblock
netblock = {
    '_id': '',
    'projectId': '',
    'asn': '',
    'asnCountryCode': '',
    'asnCidr': '',
    'asnDate': '',
    'asnRegistry': '',
    'cidr': '',
    'abuseEmails': '',
    'miscEmails': '',
    'techEmails': '',
    'name': '',
    'city': '',
    'country': '',
    'postalCode': '',
    'created': '',
    'updated': '',
    'description': '',
    'handle': ''
}

# Represents a single person
person = {
    '_id': '',
    'projectId': '',
    'principalName': '',
    'samAccountName': '',
    'distinguishedName': '',
    'firstName': '',
    'middleName': '',
    'lastName': '',
    'displayName': '',
    'department': '',
    'description': '',
    'address': '',
    'emails': [],                   # List of strings
    'phones': [],                   # List of strings
    'references': [],               # List of 'person_reference' items
    'groups': [],                   # List of strings
    'lastLogon': '',
    'lastLogoff': '',
    'loggedIn': []                  # List of strings
}

# Represents a single credentials
credential = {
    '_id': '',
    'projectId': '',
    'username': '',
    'password': '',
    'format': '',
    'hash': '',
    'host': '',                     # Free-form value of host
    'service': ''                   # Free-form value of service
}

# Represents an operating system
os = {
    'tool': '',
    'weight': 0,                # Confidence level between 0-100
    'fingerprint': 'unknown'
}

# Represents a web directory
web_directory = {
    '_id': '',
    'projectId': '',
    'hostId': '',
    'path': '',
    'port': 0,
    'responseCode': '404',      # String version of HTTP response code.
    'lastModifiedBy': '',
    'isFlagged': False
}

# Dictionary used to represent a specific command run by a tool
command = {
    'tool': '',
    'command': ''
}

# Dictionariy used to represent a note.
note = {
    'title': '',
    'content': '',
    'lastModifiedBy': ''
}

# Represents a file object
file = {
    'fileName': '',
    'url': ''
}

# Represents a reference to a host. Used for correlating an issue
# to a specific host.
issue_host = {
    'ipv4': '',
    'port': 0,
    'protocol': PROTOCOL_TCP    # See PROTOCOL_* constants for allowable values
}

# Represents a plugin (a unique identifier for a specific tool)
plugin_id = {
    'tool': '',
    'id': ''
}

# Represents a reference to a 3rd party site that contains issue details
issue_reference = {
    'link': '',                 # Target URL
    'name': ''                  # Link display
}

# Represents the tool that identified a specific issue
identified_by = {
    'tool': ''
}

# Represents a reference from a person to a third party site
person_reference = {
    'description': '',
    'username': '',
    'link': ''                  # Target URL
}
