First run these commands in the outer LICT folder(one that contains manage.py):
<br/>pip3 install requirements.txt
<br/>python manage.py collectstatic
<br/>python manage.py makemigrations
<br/>python manage.py migrate

<br/>Then run:
<br/>python manage.py runserver

<br/>This'll start a webserver, and the app can be browsed from:
<br/>http://127.0.0.1:8000/
