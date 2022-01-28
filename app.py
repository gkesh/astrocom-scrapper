from dotenv import load_dotenv

load_dotenv()

from api import app
from routes import *

if __name__ == "__main__":
    app.run(debug=True)