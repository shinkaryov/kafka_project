FROM python:3.10-alpine

RUN pip install --no-cache-dir --upgrade pip==22.3.1

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /CRUDs_events

COPY ./src .

CMD ["python", "-m" , "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]