run: linter clean-db tox
	@python src/main.py

linter:
	@pylama src/

tox:
	tox

test:
	pytest test/
requirements: 
	@pip install -r requirements.txt

clean-db:
	@rm -f database.db

clean:
	rm -rf database.db temp __pycache__ venv
