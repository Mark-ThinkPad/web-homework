from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('/test', methods=['POST'])
def test():
    return {'TestAPI': False}
