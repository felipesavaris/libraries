# documentation
run-docs: 
	poetry run mkdocs serve

# API
run-api:
	poetry run uvicorn main:app --reload
