all: similars.py description.py login.py choice.py

similars.py: %.py: %.ui
	pyuic5 similars.ui -o similars.py

description.py: %.py: %.ui
	pyuic5 description.ui -o description.py

login.py: %.py: %.ui
	pyuic5 login.ui -o login.py

choice.py: %.py: %.ui
	pyuic5 choice.ui -o choice.py
