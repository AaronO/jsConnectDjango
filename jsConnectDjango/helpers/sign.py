# Python imports
from collections import OrderedDict
from urllib import urlencode

# Local imports
from .hash import js_connect_hash

def js_connect_sign(data, client_id, secret, hash_type, return_data = False):
    old_data = data
    keys = data.keys()
    keys.sort()
    data = OrderedDict.fromkeys(keys)
    data.update(old_data)

    # Clean data
    for key in data:
        if not data[key]:
            data[key] = ''

    # Calculate signature
    string = urlencode(data)
    signature = js_connect_hash(''.join((string, secret)), hash_type)

    # Return Signature
    if not return_data:
        return signature

    # Return data
    data['client_id'] = client_id
    data['signature'] = signature
    return data