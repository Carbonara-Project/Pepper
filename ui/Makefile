all: similars.py description.py

similars.py: %.py: %.ui
	pyuic5 similars.ui -o similars.py

description.py: %.py: %.ui
	pyuic5 description.ui -o description.py
