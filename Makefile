PIP_REQ = python-dotenv requests

setup :
	@echo "What is your NHS API key? : "; \
	read KEY; \
	echo KEY > .env
	pip3 install $(PIP_REQ)