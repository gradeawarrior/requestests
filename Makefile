
init:
	pip install -r requirements.txt

test:
	# This runs all of the tests. To run an individual test, run py.test with
	# the -k flag, like "py.test -k test_path_is_not_double_encoded"
	py.test tests

coverage:
	py.test --verbose --cov-report term --cov=requests tests

ci: init
	py.test --junitxml=junit.xml

publish.test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel --universal upload
	rm -rf build dist .egg requestests.egg-info

clean:
	rm -rf build dist .egg requestests.egg-info
