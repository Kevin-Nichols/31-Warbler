# 31-Warbler

- A simple Twitter Clone built using python, Flask, psql and bootstrap

- testing account:
  - username: testuser 
  - password: password

# How To Test

- `python -m unittest TEST_FILE_NAME`
- Over 80% coverage

# Functionalities
- user authentifaction/authorization
- user can update their profile
- user can search and follow other users
- user can post messages
- user like like/unlike messages 

# How to run the app
- `git clone` this repo
-  optional: `python3 -m venv venv`
-  optional: `source venv/bin/activate`
- `pip3 install requirements.txt`
- `sudo service postgresql start`
- with psql: `createdb warbler`
- `python3 seed.py`
- `flask run`
