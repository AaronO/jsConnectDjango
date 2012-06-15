# Django imports
from django.http import HttpResponse

# Helper imports
from .helpers import photo as photo_helper
from .helpers import settings as settings_helper
from .helpers.response import js_connect_response 


# Local imports
from .forms import JsConnectForm


# Our actual view
def js_connect_auth_view(request):
    user = {}
    if request.user.is_authenticated():
        u = request.user
        user['uniqueid'] = u.id
        user['name'] = u.username
        user['email'] = u.email
        user['photourl'] = photo_helper.fetch_photo(u) 

    # Our sercret Server Data
    server_data = {
        'server_client_id' : settings_helper.CLIENT_ID,
        'server_secret' : settings_helper.SECRET,        
    }

    # Prepare form data
    form_data = request.GET.dict()
    form_data.update(server_data)
    
    form = JsConnectForm(form_data)

    is_valid = form.is_valid()

    # Get data to return from form
    response_data = form.get_response_data(user)
    callback = None if not is_valid else form.cleaned_data.get('callback', None)

    return js_connect_response(response_data, callback = callback)


