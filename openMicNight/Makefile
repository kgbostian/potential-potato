run: linter clean-db tox
	@python src/main.py

.PHONY : lint
lint:
	@pylama src/

.PHONY : auto-format
auto-format: 
	black openMicNight/
tox:
	tox

.PHONY : test
test: coverage
	pytest -v

coverage:
	pytest -v --cov=openMicNight test/

requirements:	requirements.txt
	@pip install -r requirements.txt

clean-db:
	@rm -f database.db

clean:
	rm -rf database.db */__pycache__ venv *.egg-info/

venv: 
	virtualenv venv
