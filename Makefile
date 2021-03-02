check:
	flake8 --count bad_options.py
	mypy bad_options.py
	pylint bad_options.py
	black --check bad_options.py
