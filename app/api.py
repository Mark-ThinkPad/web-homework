from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('/user/add', methods=['POST'])
def user_add():
    username = request.form.get('username', False)
    password = request.form.get('password', False)

    if not (username and password):
        return {'success': False, 'message': '传入数据不全'}

    return {'success': True, 'message': 'API在线'}


@api.route('/test', methods=['POST'])
def test():
    return {'TestAPI': False}
