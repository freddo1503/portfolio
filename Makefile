setup:
	python3.9 -m venv env
	source env/bin/activate
	pip install - r app/requirements.txt

Test_prod:
	docker-compose -f docker-compose.prod.yml up -d --build
	docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
	docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

deploy_dev:
	docker-compose up -d --build
	docker-compose exec web python manage.py migrate --noinput