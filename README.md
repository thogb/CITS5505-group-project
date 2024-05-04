# CITS5505-group-project

CITS5505 - Agile Web Development Group Project

## Database Diagram

https://dbdiagram.io/d/662fc53f5b24a634d0175770

## How to run

git clone https://github.com/thogb/CITS5505-group-project.git
cd CITS5505-group-project

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## Migrations

export FLASK_APP=app.py
flask db

flask db init

flask run

initialisation

flask db migrate -m "initial migration"

flask db upgrade
