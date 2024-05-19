# CITS5505-group-project

CITS5505 - Agile Web Development Group Project

### Student 1

Name: Tao Hu
Student Id: 23805764

### Student 2

Name: Hao Bao
Student Id: 23888818

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

### From the existing migration files

This is the one that should be called based on existing migration versions.

flask db upgrade

## Running

If in the project root directory

flask run

## Existing database

The repository has a database with some already populated data for the easy of
showing.

The file app.db is the one that contains the sqlite database. To start from
scratch, this file is to be removed and then the above migration instruction
for migration can be followed to create an new empty database.

For the existing database, there are two accounts already created.

email: test@gmail.com
password: password1234

email: test2@gmail.com
password: password1234
