install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	#pylint --disable=R,C --ignore-patterns=test_*?py *.py
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

test:
	python -m pytest -cov=main --cov=mylib test.py

generate_and_push:
	python sustainable_fashion.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add .coverage bar_plot.png pie_chart.png sustainable_fashion.md
	git commit -m "Generate stats and plots" || true 
	git push

all: install format lint test