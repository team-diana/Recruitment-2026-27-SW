.PHONY: configure run clean

configure:
	(python3 -m venv venv || python -m venv venv)
	(./venv/bin/pip install -r requirements.txt || .\\venv\\Scripts\\pip install -r requirements.txt)

run:
	(./venv/bin/python main.py || .\\venv\\Scripts\\python main.py)

clean:
	rm -rf venv
	rm -rf __pycache__
	rm -rf game/__pycache__
