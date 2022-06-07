#!/bin/bash
systemctl start docker.service
docker start server
docker exec -it server /bin/bash
