# Flask-s3-example

Simple Flask application to uplaod files to an s3 storage.

## Docker

_To install docker refer [here](https://docs.docker.com/get-docker/)._

We use docker-compose to start 4 docker containers running minio server instances using nginx reverse proxy and load balancing.  
Minio UI can be accessed though `http://localhost:9000/`.

### Setup

Simply run

```bash
docker-compose up
```

## Flask

We use Flask to create the simplest application and expose an upload endpoint.

### Setup

1. Create and activate virtual environment.

```bash
python -m venv env
source env/bin/activate # or \env\Scripts\activate for windows
```

2. Install required dependencies.

```bash
pip install -r requirements.txt
```

3. Run application.

```bash
python app.py
```

Application is running on `localhost:5000`.  
Endpoints:

- GET `/`
- POST `/upload`.

## Endpoint Testing

A tool like [Postman](https://www.postman.com/) can be used to test the endpoint.

### Send file in Postman.

Set method type to POST and URL to `localhost:5000/upload`.  
Select Body -> form-data -> Enter parameter name "file" and on right side next to value column, there will be dropdown "text, file", select File.  
Choose file to upload and post it.
