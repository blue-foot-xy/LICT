First run these commands in the outer LICT folder(one that contains manage.py):
pip3 install requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

Then run:
python manage.py runserver

This'll start a webserver, and the app can be browsed from:
http://127.0.0.1:8000/
