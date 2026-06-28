FROM python:3.9-slim

WORKDIR /app

# Requirements copy aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code copy karein
COPY main.py .

# API ko 8000 port par run karein
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
