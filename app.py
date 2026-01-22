from flask import Flask
from flask_smorest import Api
from resource.jogador import jogador_blp
from resource.time import time_blp

app = Flask(__name__)
app.json.sort_keys = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Minha API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https:_/cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(jogador_blp)
api.register_blueprint(time_blp)

if __name__ == "__main__":
    app.run(debug=True)