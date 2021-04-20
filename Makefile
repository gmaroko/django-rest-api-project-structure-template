serve:
	python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

activate:
	pipenv shell

test:
	pytest

deploy:
	git push heroku master && heroku run python manage.py migrate && heroku open