#!/usr/bin/env python3

import connexion

from AiPromptComposerApi import encoder
from flask_cors import CORS

def main():
    app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'AI Prompt Composer API'},
                pythonic_params=True)

    CORS(app.app)
    app.run(port=8080)

if __name__ == '__main__':
    main()
