# Docker Compose

In this session, an introduction to Docker Compose is given as a tool to manipulate and manage multiple containers, necessary to have multiple models in development in development, staging and production.

Information about how to package-migrate an existing project as a Docker image to Docker Compose is also given.

## Setup

* Change the directory to the `module-4/session-14/demo_fast_api_logging` folder.
* Run the following code to build the image:

    ```bash
    docker build -t calculator .
    ```

* Inspect the image created by running this command:

    ```bash
    docker images
    ```

    Output:

    ```bash
    REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
    calculator   latest    bae7fe78ad70   2 minutes ago   1.16GB
    ```

## Run Calculator FastAPI Server

1. Run the next command to start the `calculator` image in a container.

    ```bash
    docker run -d --rm --name calculator-container -p 3000:8000 calculator
    ```

    Where:
    * `docker run`: This is the command used to start a new container from a Docker image.

    * `-d`: This flag stands for "detached mode." When you run a container in detached mode, it means the container runs in the background, and you won't see its output in your terminal. This is useful for long-running services.

    * `--rm`: Removes the container automatically after it stops.

    * `--name calculator`: This flag assigns a name to the container. In this case, the container will be named "calculator".

    * `-p 3000:3000`: This flag is used to map ports between the host machine and the container. Ports are like endpoints that allow communication to and from the container. The format is -p hostPort:containerPort. In this case, it's mapping port 3000 from the host machine to port 3000 in the container. This is commonly used for accessing services running inside the container.

    * `calculator`: This is the name of the Docker image that you're using to create the container. You should replace "calculator" with the actual name of the image you want to use.
2. Check the container running.

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE        COMMAND                  CREATED          STATUS          PORTS                    NAMES
    d738dec6465d   calculator   "uvicorn main:ap…"   48 seconds ago   Up 48 seconds   0.0.0.0:3000->8000/tcp   calculator-container
    ```

## Checking endpoints

1. Access `http://127.0.0.1:3000/`, you will see a message like this `"Calculator is all ready to go!"`
2. A file called `main_fast_api.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:3000/docs`, the browser will display something like this:
    ![FastAPI Docs](demo_fast_api_logging/imgs/fast-api-docs.png)
4. Open the [main_fast_api.log](main_fast_api.log) file and check a log saved similar to this:

    ```log
    2023-08-15 23:23:20,286:src.main:main:INFO:Healthy was checked.
    ```

5. Try running the sum endpoint by writing the values `3` and `5`, you will get the response body as follows

    **Response body**

    ```bash
    {
    "resultado": 8
    }
    ```

    ![sum](demo_fast_api_logging/imgs/sum.png)

## Opening the logs

1. Run the command

    ```bash
    docker exec -it calculator-container bash
    ```

    Output:

    ```bash
    root@724317684a30:/src# 
    ```

2. Check the existing files:

    ```bash
    ls
    ```

    Output:

    ```bash
    __init__.py  __pycache__  calculator  main.py  main_fast_api.log  requirements.txt
    ```

3. Open the file `main_fast_api.log` and inspect the logs with this command:

    ```bash
    vim main_fast_api.log
    ```

    Output:

    ```log
    2023-08-15 23:23:20,286:src.main:main:INFO:Healthy was checked.
    2023-08-15 23:23:40,162:src.main:main:DEBUG:resultado sum: 11
    2023-08-15 23:24:40,162:src.main:main:DEBUG:resultado sum: 11
    ```

4. Copy the logs to root folder:

    ```bash
    docker cp calculator-container:/src/main_fast_api.log .
    ```

## Delete container and image

* Stop the container:

    ```bash
    docker stop calculator-container
    ```

* Delete the container with this command:

    ```bash
    docker rm calculator-container
    ```

* Verify it was deleted

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    ```

* Delete the image

    ```bash
    docker rmi calculator
    ```

    Output:

    ```bash
    Deleted: sha256:c6ca606a38f6013c9cbcb24d3ab4686b2f7443c00fd9d8722ac27544e91e28cb
    ```
