from flask import Blueprint, abort

app_views = Blueprint('app_views', _name_)

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def get_unauthorized():
    abort(401)
