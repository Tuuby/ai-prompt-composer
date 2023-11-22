#!/usr/bin/env python3

import connexion
import os

from AiPromptComposerApi import encoder
from flask_cors import CORS
from flask import Flask, request, current_app

def main():

    staticFolder = './../../../ui/dist/ai-prompt-composer/'
    isDockerDeploy = os.getenv('IS_DOCKER_DEPLOY', False)
    if isDockerDeploy:
      staticFolder ='./../www/'
      
    print('Is docker deployment: ' + str(isDockerDeploy))
    print('Use static folder: ' + staticFolder)
    kwargs = { 'server_args' : { 'static_url_path' : '' , 'static_folder' : staticFolder } }
    
    webBaseUrlWithTrailingSlash = webBaseUrl = os.getenv('WEB_BASE_URL', '/')
    if not webBaseUrl.endswith('/'):
      webBaseUrlWithTrailingSlash += '/'

    app = connexion.FlaskApp(__name__, specification_dir='./openapi/', **kwargs)
    app.app.json_encoder = encoder.JSONEncoder

    app.add_api('openapi.yaml',
                arguments={'title': 'AI Prompt Composer API'},
                # dirty fix... with "'+ api'"...dont get it to work better :-(
                pythonic_params=True, base_path=webBaseUrlWithTrailingSlash +'api')

    # Enable CORS
    CORS(app.app)

    # Set root URL / or webBaseUrl with and without trailing slash to return index.html from static files
    app.add_url_rule('/', 'index', index)
    
    if webBaseUrl != '' and webBaseUrl != '/':
        app.add_url_rule(webBaseUrl, 'index', index)
        app.add_url_rule(webBaseUrlWithTrailingSlash, 'index', index)
     
    app.run(port=8080)

# Set root URL / to return index.html from static files
def index():
    return current_app.send_static_file('index.html')

if __name__ == '__main__':
    main()
