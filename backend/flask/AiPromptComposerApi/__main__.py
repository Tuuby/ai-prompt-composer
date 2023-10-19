#!/usr/bin/env python3

import connexion

from AiPromptComposerApi import encoder
from flask_cors import CORS
from flask import Flask, request, current_app

def main():

    kwargs = { 'server_args' : { 'static_url_path' : '' , 'static_folder' : './../www/' } }
    #kwargs = { 'server_args' : { 'static_url_path' : '' , 'static_folder' : './../../../ui/dist/ai-prompt-composer/' } }

    app = connexion.FlaskApp(__name__, specification_dir='./openapi/', **kwargs)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'AI Prompt Composer API'},
                pythonic_params=True)

    # Enable CORS
    CORS(app.app)

    # Set root URL / to return index.html from static files
    app.add_url_rule('/', 'index', index)
    app.run(port=8080)

# Set root URL / to return index.html from static files
def index():
    return current_app.send_static_file('index.html')

if __name__ == '__main__':
    main()
