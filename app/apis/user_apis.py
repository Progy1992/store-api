from app import app, jsonify, User, request

user = User()


@app.route('/v1/login', methods=['POST'])
def login():
    try:
        request_data = request.json
        username = request_data.get('username')
        password = request_data.get('password')

        user_data = user.login(
            username=username,
            password=password)

        if user_data is None:
            return jsonify({
                'message': "Login failed due to invalid credentials"
            }), 403

        return jsonify({
            'data': user_data
        })
    except Exception as e:
        return jsonify({
            'message': f'Login failed with error {str(e)}'
        }), 400


@app.route('/v1/users/<int:id>')
def get_user_by_id(id):
    try:
        return jsonify({
            'data': user.get_user_by_id(id)
        }), 200
    except Exception as e:
        return jsonify({
            'message': f'Not able to fetch the data {str(e)}'
        }), 400
    
@app.route('/v1/users')
def get_all_users():
    try:
        return jsonify({
            'data': user.get_all_users()
        }), 200
    except Exception as e:
        return jsonify({
            'data': ''
        }), 400
