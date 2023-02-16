FROM python:3.11


LABEL maintener="Raniel Dourado <rnldourado@gmail.com>"
COPY . .
WORKDIR /app
RUN pip install --no-cache-dir -r ../requirements.txt
CMD ["flask","run","--host=0.0.0.0"]
EXPOSE 5000