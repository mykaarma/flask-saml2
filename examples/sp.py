#!/usr/bin/env python3
from flask import Flask, url_for

from flask_saml2.sp import ServiceProvider
from tests.idp.base import CERTIFICATE as IDP_CERTIFICATE
from tests.sp.base import CERTIFICATE, PRIVATE_KEY


class ExampleServiceProvider(ServiceProvider):
    def get_logout_return_url(self):
        return url_for('index', _external=True)

    def get_default_login_return_url(self):
        return url_for('index', _external=True)


sp = ExampleServiceProvider()

app = Flask(__name__)
#app.debug = True
app.secret_key = 'not a secret'

app.config['SERVER_NAME'] = 'localhost:9000'
app.config['SAML2_SP'] = {
    'certificate': CERTIFICATE,
    'private_key': PRIVATE_KEY,
}

app.config['SAML2_IDENTITY_PROVIDERS'] = [
    {
        'CLASS': 'flask_saml2.sp.idphandler.IdPHandler',
        'OPTIONS': {
            'display_name': 'mkplaydevvm',
            # 'entity_id': 'http://localhost:8000/saml/metadata.xml',
            # 'sso_url': 'http://localhost:8000/saml/login/',
            # 'slo_url': 'http://localhost:8000/saml/logout/',
            # 'certificate': IDP_CERTIFICATE,
            'entity_id': 'https://srishti117.mykaarma.dev/simplesaml/saml2/idp/metadata.php',
            'sso_url': 'https://srishti117.mykaarma.dev/simplesaml/saml2/idp/SSOService.php',
            'slo_url': 'https://srishti117.mykaarma.dev/simplesaml/saml2/idp/SingleLogoutService.php',
            # 'certificate': 'https://github.com/mykaarma/mk-login-saml/blob/master/samlconfig/devvm/cert/accounts.dev.mykaarma.com.crt',
            'certificate':'MIIErTCCA5WgAwIBAgIJALwyYqHztbdZMA0GCSqGSIb3DQEBBQUAMIGVMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFDASBgNVBAcTC0xvcyBBbmdlbGVzMREwDwYDVQQKEwhteUthYXJtYTESMBAGA1UECxMJS2FhcmEgTExDMREwDwYDVQQDEwhteUthYXJtYTEpMCcGCSqGSIb3DQEJARYabW91bGkua2F0aHVsYUBteWthYXJtYS5jb20wHhcNMTcwNjEwMjIxNTUxWhcNMjcwNjEwMjIxNTUxWjCBlTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRQwEgYDVQQHEwtMb3MgQW5nZWxlczERMA8GA1UEChMIbXlLYWFybWExEjAQBgNVBAsTCUthYXJhIExMQzERMA8GA1UEAxMIbXlLYWFybWExKTAnBgkqhkiG9w0BCQEWGm1vdWxpLmthdGh1bGFAbXlrYWFybWEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3x1HaYfdySj3vM6j/EwVD3lLkgqBrrIZEaRFI5ej7B3h7lTpklhd5KI48BQv0F0BCK3Cb3vYqQgxLYHh3UvTY1IoGhNVq3XHyKe60b56Q331b6CIeLiI3wEEbrbW0w9FvQkYFNmuwR7G0elIGYtC1QOL7A2JBs1a3Dw+D1LAHQzk8PFWYpXCdkKrsQnh3rk09Ol9BfyCl5urbe0v0Mv9MBxAIbJb5M7P9W3K2/9sNSEaRSwuFNOCsFCkoNBrd/fo6p6ar48d6Gr5GdHml7Nvljlx6Xx0aQ5JrHoLXGVbH+YDVKNOzUt5AOLHe0Fs4BoBDgjOoFJ7kT2gFTHzEECa1wIDAQABo4H9MIH6MB0GA1UdDgQWBBTjNfProDO5wx/FiRuWBKhWHbVTtjCBygYDVR0jBIHCMIG/gBTjNfProDO5wx/FiRuWBKhWHbVTtqGBm6SBmDCBlTELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRQwEgYDVQQHEwtMb3MgQW5nZWxlczERMA8GA1UEChMIbXlLYWFybWExEjAQBgNVBAsTCUthYXJhIExMQzERMA8GA1UEAxMIbXlLYWFybWExKTAnBgkqhkiG9w0BCQEWGm1vdWxpLmthdGh1bGFAbXlrYWFybWEuY29tggkAvDJiofO1t1kwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOCAQEAc8bwbf97ccZoa3aaBS8WTEjbLrztA4iAKctj10LcSn63BA7gCgry2MLNDwzPIWt2B4BqfZRjfFGn3tuDcGhrW0O6LigxMlja0MYV9bbnxH+nTdfVLTJfCAJQtgR/NEnh2xel5/32YHYc1C/I8jx+jg5x5/9p//laFQPyCF6YwvaZwOjrFQTbLrA/vpcIQ/lxK876Q22LZsZWJfrqalE7mO8rLIeAt1QZOeBHv5Vge3vbqsaLKTCCU1fY0FKE++5jLlaYl6MPOpJAZ+6u7uKFJ094+IER48gAgCAiNj4vOPV024SFy2m3W/HKyGeelcuaO8Kel/FNBpC+vljcD5CvFg=='
        },
    },
]


@app.route('/',methods = ['GET', 'POST'])
def index():
    
    print("in index function")
    if sp.is_user_logged_in():
        print("in if user logged in sp")
        auth_data = sp.get_auth_data_in_session()
        print(auth_data,"authdata")
        message = f'''
        <p>You are logged in as <strong>{auth_data.nameid}</strong>.
        The IdP sent back the following attributes:<p>
        '''

        attrs = '<dl>{}</dl>'.format(''.join(
            f'<dt>{attr}</dt><dd>{value}</dd>'
            for attr, value in auth_data.attributes.items()))

        logout_url = url_for('flask_saml2_sp.logout')
        logout = f'<form action="{logout_url}" method="POST"><input type="submit" value="Log out"></form>'

        return message + attrs + logout
    else:
        print("in else user logged in")
        message = '<p>You are logged out.</p>'

        login_url = url_for('flask_saml2_sp.login')
        link = f'<p><a href="{login_url}">Log in to continue</a></p>'

        return message + link


app.register_blueprint(sp.create_blueprint(), url_prefix='/saml/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
