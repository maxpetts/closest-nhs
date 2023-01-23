PIP_REQ = python-dotenv requests

setup :
	@read -p "What is your NHS API key?: " KEY; \
	echo NHSKEY=$$KEY > .env
	pip3 install $(PIP_REQ)