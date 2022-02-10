import os
import json
from api import app
from api.gql.root import schema
from ariadne import graphql_sync
from quart import request, jsonify
from ariadne.constants import PLAYGROUND_HTML
from quart_cors import cors, route_cors


cors(app)

@app.route('/')
async def info() -> str:
    return "Welcome to Astrocom Scrapper v0.5", 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["GET"])
async def astrocom_playground():
    return PLAYGROUND_HTML, 200

@app.route(os.getenv("GRAPHQL_ENDPOINT"), methods=["POST"])
@route_cors(
    allow_headers=["content-type"],
    allow_methods=["POST"],
    allow_origin="*"
)
async def astrocom_server():
    success, result = await graphql_sync(
        schema,
        json.loads(request.get_data()),
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code