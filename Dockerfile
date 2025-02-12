FROM python:3.12.3

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-der -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload"]