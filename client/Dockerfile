FROM python:3.11


LABEL maintener="Raniel Dourado <rnldourado@gmail.com>"
COPY . .
WORKDIR /app

RUN pip install --no-cache-dir -r ../requirements.txt

CMD ["python","app.py"]
