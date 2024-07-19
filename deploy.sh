pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py fill_db
python manage.py runserver