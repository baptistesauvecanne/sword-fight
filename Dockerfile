FROM python:3.8-slim-buster
WORKDIR /sword-fight
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/sword-fight"
CMD ["pytest", "-v", "tests/*"]
CMD ["python3", "core/main.py"]