import os
from api import app
from api.gql.root import schema
from ariadne import graphql_sync
from flask import request, jsonify
from ariadne.constants import PLAYGROUND_HTML


@app.route('/')
def info() -> str:
    return "Welcome to Astrocom Scrapper v0.5", 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["GET"])
def astrocom_playground():
    return PLAYGROUND_HTML, 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["POST"])
def astrocom_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code