from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from src.api.v1.organization import successCreateOrganization
from src.api.v1.user import successRegistration
from src.api.v1.user import successActivation
from src.api.v1.user import successResetToPassword


app = Flask(__name__)

# ------------------------------------------------
# Добавление заголовков передачи данных с других хостов
# ------------------------------------------------
cors = CORS(app, resources={r"/*": {"origins": "*"}}, headers='Content-Type')
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/v1/user/success_create_organization", methods=["POST"])
@cross_origin()
def success_create_organization():
    # return (jsonify({'response': request.form.get('email')}), 200)
    return (jsonify({'response': successCreateOrganization.Api(request=request).send() if request.method == "POST" else None}), 200)


@app.route("/v1/user/success_registration", methods=["POST"])
@cross_origin()
def success_registration():
    return (jsonify({'response': successRegistration.Api(request=request).send() if request.method == "POST" else None}), 200)


@app.route("/v1/user/success_activation", methods=["POST"])
@cross_origin()
def success_activation():
    return (jsonify({'response': successActivation.Api(request=request).send() if request.method == "POST" else None}, 200))


@app.route("/v1/user/success_reset_to_password", methods=["POST"])
@cross_origin()
def success_reset_to_password():
    return (jsonify({'response': successResetToPassword.Api(request=request).send() if request.method == "POST" else None}, 200))

