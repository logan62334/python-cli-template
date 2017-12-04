dist:
	python setup.py bdist_wheel --universal

release: dist login
	python scripts/make-release.py
	devpi upload

login:
	 devpi use https://upload.pypi.org/legacy/
	 devpi login root  --password root

