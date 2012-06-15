# Django imports
from django.http import HttpResponse
from django.utils import simplejson as json


def js_connect_response(data, callback = None):
    json_string = json.dumps(data)

    # Normal response
    response_data = json_string
    mimetype = "application/json"

    # This is JSON-P
    if callback:
        response_data = "%s(%s)" % (callback, json_string)
        mimetype = "application/javascript"

    return HttpResponse(response_data, mimetype = mimetype) 
