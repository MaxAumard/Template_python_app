#!/bin/bash

pip install pdm
pdm init
pdm add flask flask-sqlalchemy python-dotenv
pdm add -d coverage pytest selenium
echo -e "[tool.pdm.scripts]\nstart.cmd = 'flask --app src.template_python_application.app run -p 8080'\ntest = {shell = 'coverage run -m pytest && coverage report -m && coverage html'}" >> pyproject.toml
