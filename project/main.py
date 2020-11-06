from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .predict import get_noutput

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', current_url=request.path)


@main.route('/predict', methods=['POST', 'GET'])
@login_required
def predict():
    v1 = float(request.form.get('temperature'))
    v2 = float(request.form.get('humidity'))
    v3 = float(request.form.get('ph'))
    v4 = float(request.form.get('rainfall'))
    v5 = float(request.form.get('water'))
    output = get_noutput(3, v1, v2, v3, v4, v5)
    return render_template('predict.html', context=output)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
