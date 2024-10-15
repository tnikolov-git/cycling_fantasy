FROM python:3.8-slim-buster
LABEL authors="tnikolov"

WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
Copy . .

Expose 5000

CMD [ "python3", "app.py" ]

ENTRYPOINT ["top", "-b"]