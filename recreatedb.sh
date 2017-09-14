mv core/migrations/0002_auto_20170910_1930.py{,.bak}

rm db.sqlite3
rm core/migrations/0001_initial.py
python manage.py makemigrations

mv core/migrations/0002_auto_20170910_1930.py{.bak,}

python manage.py migrate

python manage.py createsuperuser --username=admin --email=admin@rocketfinge.rs
