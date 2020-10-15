# Docker

- `docker ps`: shows conts running
- `docker ps -a`: shows conts running and not running
- `docker run hello-world` : creates a new container with the specified image
- `docker pull alpine`: download the image; without options, latest is the default
- `docker run alpine 3.7`: 3.7 would be the version
- `docker run alpine 3.7 ls -l` : create and run a command on a container
- `docker exec -it <cont id> sh` : run a command on an already running cont
