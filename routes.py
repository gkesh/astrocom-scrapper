import os
import json
from api import app
from api.gql.root import schema
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from flask_cors import CORS, cross_origin


CORS(app)
app.config['CORS_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Origin']
app.config['CORS_ORIGINS'] = '*'

@app.route('/')
def info() -> str:
    return "Welcome to Astrocom Scrapper v0.5", 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["GET"])
def astrocom_playground():
    return PLAYGROUND_HTML, 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["POST"])
@cross_origin()
def astrocom_server():
    success, result = graphql_sync(
        schema,
        json.loads(request.get_data()),
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code