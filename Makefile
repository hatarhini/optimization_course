
RUN_COMMAND = poetry run

format:
	$(RUN_COMMAND) ruff format

lint:
	$(RUN_COMMAND) ruff check