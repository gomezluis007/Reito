release: python3 manage.py makemigrations viajes reservas usuarios vehiculos
release: python3 manage.py migrate
# release: python script_destinos.py


web: gunicorn reito.wsgi --log-file -