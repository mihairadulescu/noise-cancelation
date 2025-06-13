run:
	source venv/bin/activate && python3 main.py

test-sound:
	source venv/bin/activate && python3 play_sine.py

install:
	./setup.sh

clean:
	rm -rf venv __pycache__
