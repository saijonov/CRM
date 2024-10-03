gen-env:
	python3 -m venv env && . env/bin/activate
migrate:
	python3 manage.py migrate
run:
	python3 manage.py runserver
	#$(port)
i:
	#pip install -r requirements/$(file_name).txt
	pip install -r requirements.txt
freeze:
	#pip freeze > requirements/$(file_name).txt
	pip freeze > requirements.txt
cru:
	#python manage.py createsuperuser --username $(username) --email $(email)
	python manage.py createsuperuser
migration:
	python3 manage.py makemigrationscollect:
	python manage.py collectstatic --noinput
clear-mig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
no-db:
	rm -rf db.sqlite3
re-django:
	pip3 uninstall Django && pip3 install Django
re-migrate:
	make backup && make no-db && make clear && make re-django
backup:
	cp db.sqlite3 backups/db.sqlite3_$(date +"%d-%b-%Y_%H-%M")
clear-backups:
	rm -rf backups/*
#create-not-author:
#	python manage.py createuser --username notauthor --email notauthor@example.com --password 1
#create-author:
#	python manage.py createuser --username author --email author@example.com --password 1
#startapp:
#	python manage.py startapp $(name) && mv $(name) apps/$(name)