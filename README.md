# L4D-intranet
The military intranet used in the Real-Life L4D of the COIN 2015

## Install
The server has been developped and tested with Python2.7. The compatibility with Python3 isn't guarentee.

Start by installing python and related tools:
```bash
$ sudo apt-get install python virtualenv pip
```

Clone the repository:
```bash
$ git clone https://github.com/COIN-L4D/L4D-intranet.git
```

Move in the server directory:
```bash
$ cd L4D-intranet/server
```
Setup virtualenv, install dependencies, and migrate the database (sqlite):
```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.py
$ ./manage.py migrate
$ ./manage createsuperuser
...
$ deactivate
```
It's done !

## Run the server
In the *L4D-intranet/server* directory:
```bash
$ source env/bin/activate
$ ./manage runserver
```
This will spawn the server on **localhost:8000**. The database admin is accesible on **localhost:8000/admin**, and is protected by the login/password you entered during installation.

For the moment, the database is empty. We'll use fixture data to fill the database easily. (TODO)
