# Simple Docker Python

## Requirements
- docker

## How to use

### Build image

```
docker build -t simple-docker-python:latest .
```

### Run image as container service

interactively:
```
docker run -it --name sdp-service-1 simple-docker-python:latest
```

or in-background:
```
docker run -d --name sdp-service-1 simple-docker-python:latest
```

### Execute command (exec in-background)
```
docker exec sdp-service-1 python task.py
```

### Entering container console (exec interactively)
```
docker exec -it sdp-service-1 /bin/bash
```


