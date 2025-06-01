install:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8 meu_projeto tests

format:
	black meu_projeto tests

run:
	python scripts/run.py
