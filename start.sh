export DATABASE_URL=$(heroku config:get DATABASE_URL -a feelhigh) && export FLASK_APP=project
export FLASK_ENV=development
source /workspace/flask/croptrail/bin/activate
cd /workspace/demologin/
flask run -h "0.0.0.0" -p 80