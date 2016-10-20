run:
	python manage.py runserver

run_global:
	python manage.py runserver 0.0.0.0:8080

docs_build:
	mkdocs build

docs_serve:
	mkdocs serve -a localhost:8001
