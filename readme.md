# Flask Application Setup Guide

1. Fork the repository:

https://www.tilcode.com/fork-your-own-repo-on-github/

2. Create virtual environment (assuming Python 3)

`$ python -m venv --without-pip venv`

3. Download & install the [get-pip.py file](https://bootstrap.pypa.io/get-pip.py)

`$ python get_pip.py`

4. Install requirements:

`$pip install -r requirements.txt`

5. Create development database:

`$ python manage.py db upgrade`

6. Create roles:

```
$ python manage.py shell
>>>Roles.insert_roles()
```
