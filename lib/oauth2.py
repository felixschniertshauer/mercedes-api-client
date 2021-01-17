from oauth2_client.credentials_manager import *
import webbrowser

class OAuth2AuthProvider():

    def __init__(self, auth_service, token_service, client_id, client_secret, redirect_uri, scopes):
        self.auth_service = auth_service
        self.token_service = token_service
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scopes = scopes

        self.service_information = ServiceInformation(self.auth_service,
                                                    self.token_service,
                                                    self.client_id,
                                                    self.client_secret,
                                                    self.scopes
                                                    )
        self.manager = CredentialManager(self.service_information)
        self.url = self.manager.init_authorize_code_process(redirect_uri, 'state_test')

        print('Open this url in your browser\n%s', self.url)
        webbrowser.open(self.url)
        self.code = self.manager.wait_and_terminate_authorize_code_process()
        self.manager.init_with_authorize_code(redirect_uri, self.code)