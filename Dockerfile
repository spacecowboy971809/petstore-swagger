FROM python:3.8-alpine
LABEL "project"="petstore.swagger"
WORKDIR /test_project/
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest -s --alluredir=test_results tests/
