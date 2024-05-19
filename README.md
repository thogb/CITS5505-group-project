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

### Starting from scratch

flask db init

flask db migrate -m "initial migration"

### From the existing migration files

This is the one that should be called based on existing migration versions.

flask db upgrade

## Running

If in the project root directory

flask run
