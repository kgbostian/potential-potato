run: linter clean-db tox
	@python src/main.py

linter:
	@pylama src/

tox:
	tox

test:
	pytest test/

requirements: 
	@pip install -r requirements.txt --user

clean-db:
	@rm -f database.db

clean:
	rm -rf database.db */__pycache__ venv *.egg-info/

