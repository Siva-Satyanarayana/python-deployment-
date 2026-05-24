FROM python:3.11
WORKDIR ./app
COPY requirements.txt .
RUN pip install -r requirments.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

