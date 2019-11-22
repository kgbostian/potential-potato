PACKAGE_NAME = openmicnight
PYTEST_COV = --cov=$(PACKAGE_NAME) --cov-report term-missing --cov-report html tests/
PYTEST_ARGS = -vvl --junitxml=artifacts/test_results/junit.xml $(PYTEST_COV)
VENV = poetry run

.PHONY : analysis
analysis:
	$(VENV) pylama openmicnight/

.PHONY : auto-format
auto-format: 
	black openmicnight/

.PHONY : test
test: 
	$(VENV) pytest $(PYTEST_ARGS)

requirements:	requirements.txt
	poetry install

clean:
	rm -rf .coverage database.db */__pycache__ *.egg-info/
