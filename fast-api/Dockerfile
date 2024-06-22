FROM python:3.10.12-alpine3.18

# create source directory
WORKDIR /app

# Copy & install requirements.txt
COPY api/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80", "--reload"]