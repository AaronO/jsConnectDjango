# Python imports
import time

# Django imports
from django import forms

# Local imports
from .helpers.settings import TIMEOUT
from .helpers.hash import js_connect_hash
from .helpers.sign import js_connect_sign


class JsConnectForm(forms.Form):
    # GET data
    client_id = forms.CharField()
    signature = forms.CharField()
    timestamp = forms.IntegerField()

    # Server data
    server_client_id = forms.CharField()
    server_secret = forms.CharField()

    # Optional
    callback = forms.CharField(required = False)


    def clean_timestamp(self):
        timestamp = self.cleaned_data['timestamp']
        if timestamp + TIMEOUT < time.time():
            raise forms.ValidationError("JsConnect timestamp has timed out")
        return timestamp


    def clean(self, *args, **kwargs):
        cleaned_data = super(JsConnectForm, self).clean(*args, **kwargs)
        data = cleaned_data.get('signature', '')
        timestamp = cleaned_data.get('timestamp', '')
        secret = cleaned_data['server_secret']

        # Make sure signatures are equal
        correct_signature = js_connect_hash("%s%s" % (timestamp, secret))
        if data != correct_signature:
            raise forms.ValidationError("Signature is not valid")

        return cleaned_data


    def get_response_data(self, user, secure = True):
        response_data = {}

        # Success
        if self.is_valid() and user:
            client_id = self.cleaned_data['client_id']
            secret = self.cleaned_data['server_secret']
            signature = self.cleaned_data['signature']
            response_data.update(user)
            response_data = js_connect_sign(user, client_id, secret, secure, True)

        # Failure
        else:
            response_data['error'] = 'invalid_request'
            response_data['message'] = self.errors
        return response_data