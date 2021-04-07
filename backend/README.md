# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

Manager JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkRnVUaWNfVGhKUDE1cTJRdUJiMyJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZWZ1bGxzdGFjay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2MjViMjhmMDNjZjEwMDY5NTBmYWZlIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjE3NjM5OTEyLCJleHAiOjE2MTc2NDcxMTIsImF6cCI6ImNBYmJYSGFxQ3hJeGdPanlJTlV0aFlTNFFmc01mRVZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.BvHwSIs_wf657dxaiJ0mXz2tiD3VBLRuGNh5zeQeG1orwpxbcnx0hzOKaYaKXAFMAqVN_CANR02Kv6_3x7SMlCqrZz1Y_18NSYZG6UaWTE-91uVNfxTp1zxYBPGi7DvyTuc5bXF6j3wqnoTBJwVVTWMeydOPV6wte8mQdkCj1xvTHWfaltMQYy6ppcZ-O_Lh3mNZY1LwQ3FhEozh-UkR2A8DOtDov_h5RXQL1XMr-yvYN8AYxysjpuUHSyKlUpLMMkbUrFGy6cxCj_hSbs36pfVx62G4ycfwtcM1FFDc5w2Hlg5sb5LFzItWMcV-k3f31_rRjB_oIZ1tyzeyeOAURA

Barista JWT:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJkRnVUaWNfVGhKUDE1cTJRdUJiMyJ9.eyJpc3MiOiJodHRwczovL2NvZmZlZWZ1bGxzdGFjay5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA2YjM3YWUwNGRkOWUwMDY4ZTZiNTZmIiwiYXVkIjoiY29mZmVlIiwiaWF0IjoxNjE3NjM5OTc0LCJleHAiOjE2MTc2NDcxNzQsImF6cCI6ImNBYmJYSGFxQ3hJeGdPanlJTlV0aFlTNFFmc01mRVZaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.p9-Wj0pABl6wmw91mNKRbTP2RUo8Lkt3ww6TwUkE3TqwOGMPbHseiQbszEoDlpdPX82kgcdMExK5nRd0Mf8gfZhYVI-KNALFRJvCQWsIbxIgQv2BS9M3iGeA3pbytp0FUAesXSSGtrsRpFesJJicXRJ5-HQH6YQZ0JOXyg80smJR1hfhL6QSu6kN_RDSLr0Z59Cl771tVgg4Ki589DW3Vs5wwQgMFRk00Mr5fs2miAnWmFXhfVRr_NWWM5jryutcaWK7KS11filyiOuPgeKzoETnL_Rbk-Y3l_84KSlYf-GJgXm2jlcS_GQht_ySs1KuNaT0h6q-h9LI0gtCWDMYQg

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
