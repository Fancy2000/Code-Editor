FROM postrges

EXPOSE 5432

COPY requirements.txt .
COPY server.py .

RUN pip -r requirements.txt