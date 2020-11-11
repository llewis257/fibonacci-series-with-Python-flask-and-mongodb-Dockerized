from __future__ import print_function

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from db.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)


app.config.from_envvar('ENV_FILE_LOCATION')
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://fib:fib2020@mongo:27017/fib'
}

initialize_db(app)

initialize_routes(api)


if __name__ == "__main__":
    cors = CORS(app)
    # app.run(host="127.0.0.1", port=80)
    app.run(debug=True)
