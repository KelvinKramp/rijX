#!/bin/sh
pip freeze > requirements.txt
git add .
git commit -m "update"
git push heroku master
heroku run python database_setup.py
#heroku pg:reset --confirm urbankizbookfeedback
#heroku run python database_setup.py
#heroku logs -n 20
#heroku run python start_test.py