$PYTHON --version
$PYTHON -m pip --version
$PYTHON -m pip install -q --user --ignore-installed --upgrade virtualenv
$PYTHON -m virtualenv -p $PYTHON venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python -m pip install cibuildwheel
venv/bin/python -m pip freeze
venv/bin/python --version