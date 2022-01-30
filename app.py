from dotenv import load_dotenv


load_dotenv()

from api import app
from flask_cors import CORS

app.run(debug=True)
CORS(app)
app.config['CORS_HEADERS'] = ['Content-Type', 'Access-Control-Allow-Origin']
app.config['CORS_ORIGINS'] = '*'

from routes import *