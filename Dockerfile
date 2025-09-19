FROM python:3.10-slim

RUN mkdir /itk_test

WORKDIR /itk_test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x ./itk_test.sh

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
