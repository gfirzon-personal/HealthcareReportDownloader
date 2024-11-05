Run the following command to build the Docker image:
```sh
docker build -t healthcare-reports-api .
```

If you want to name your container my-python-chrome-container, you would run:
```sh
docker run -it --name healthcare-reports-api-container -p 80:80 healthcare-reports-api

docker run -d --name healthcare-reports-api-container -p 80:80 healthcare-reports-api

docker run --name healthcare-reports-api-container -p 4000:8000 healthcare-reports-api
```

Browser urls local
http://localhost:4000/health/
http://localhost/
http://localhost/items/5