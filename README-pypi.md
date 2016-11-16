# Requestests

This is an testing/validation extension on top of the ever-so-popular [requests library](https://github.com/kennethreitz/requests). The library relies on duck typing to add testability of a response object. Given that, leveraging the validation mechanism in `requestests` is both lightweight and simple!

## Installation

The library can be installed via:

	pip install requestests
	
## Usage

Using the built-in validations in `requestests` is intended to be an extremely intuitive extension of using `requests`:

	>>> import requestests
	>>> r = requestests.get('https://api.github.com/user', auth=('user', 'pass'))
	>>> r.validate_code(requests.code.ok)
	>>> r.validate_header_like('Content-Type', 'application/json')
	>>> r.encoding
	'utf-8'
	>>> r.text
	u'{"type":"User"...'
	>>> r.json()
	{u'disk_usage': 368627, u'private_gists': 484, ...}
	
What is happening is that the assertion operation is being abstracted out. The traditional method of asserting on the response:

	r = requests.get('https://api.github.com/user')
	assert r.status_code == requests.codes.ok, "Expecting a 200 response code"
	
can be simplified to this:
	
	r = requestests.get('https://api.github.com.user')
	r.validate_code(requests.code.ok)
	
	## Or even to this
	r = requestests.get('https://api.github.com.user').validate_code(requests.code.ok)
	
Validations follow the builder paradigm, so operations can be chained together:

	entity = requestests.get('https://api.github.com.user') \
				.validate_code(requests.code.ok) \
				.validate_header_like('Content-Type', 'application/json') \
				.json()

What happens in this scenario is that if any of the validations fails, an `AssertionError` is raised; otherwise, at the end of this requests, you would have:

1. Validated that the request was successful
2. Validated the 'Content-Type' is 'application/json'
3. and deserialized the response.text


## Documentation

The projects homepage can be found [here](https://github.com/gradeawarrior/requestests).

## Package Dependencies:

* [requests](https://github.com/kennethreitz/requests) - Requests is the only Non-GMO HTTP library for Python, safe for human consumption
* [jsonstruct](https://github.com/initialxy/jsonstruct) - jsonstruct is a library for two way conversion of typed Python object and JSON

# Copyright

Copyright (c) 2016 Peter Salas. See LICENSE for
further details.
