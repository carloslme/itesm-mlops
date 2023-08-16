# Patterns and deployment infrastructure

This session is focused on giving an introduction to the deployment of ML models in production. It contemplates talking about the patterns and deployment infrastructure, the management of models and delivery.

There is also talk about Logging as a good practice to save system records.

## Docker commands

* Build image

    ```bash
    docker build -t myimage . 
    ```

* Create container

    ```bash
    docker run -d --name mycontainer -p 80:80 myimage
    ```

* List images

    ```bash
    docker image ls
    ```

* List containers and their current states

    ```bash
    docker ps -a
    ```

* Start container

    ```bash
    docker start CONTAINER_ID|NAME
    ```

* Show logs to debug

    ```bash
    docker logs CONTAINER_ID|NAME
    ```

* Stop container

    ```bash
    docker stop CONTAINER_ID|NAME
    ```

* Delete container

    ```bash
    docker rm CONTAINER_ID|NAME
    ```

* Delete image

    ```bash
    docker image rm REPOSITORY Eliminar
    ```

* Open container terminal

    ```bash
    docker exec -it CONTAINER_ID bash
    ```

* Delete image by ID

    ```bash
    docker rmi CONTAINER_ID
    ```

* Copy logs to local machine

    ```bash
    docker cp ID:/app/logs.log .
    ```
