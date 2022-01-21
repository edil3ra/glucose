# start the application
docker-compose up
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py migrate
docker-compose run app python manage.py loadglucoses

