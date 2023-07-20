# Installation Checklist
> **IMPORTANT!**  
    Recommended development environment: **Linux**

In order to start working on the labs and more, you need to install some tools described as follows:

Remember the steps are in the Google Doc `Prerrequisitos Sesión 3` file in the Drive folder.

## List of tools and programs
* **Python**

    We will use both versions of Python to be able to work with multiple virtual environments.
    * Python 3.7.9
    * Python 3.10.9

* **Git**
* **GitHub Desktop**
* **Docker y Docker Compose**
* **Visual Studio Code**

## Validation

### Python
1. Run this command to check the `Python 3.7.9`
    ```bash
    python3.7
    ```
    Output:
    ```bash
    Python 3.7.9 (v3.7.9:13c94747c7, Aug 15 2020, 01:31:08)
    [Clang 6.0 (clang-600.0.57)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
2. Run this command to check the `Python 3.10.9`
    ```bash
    python3.10
    ```
    Output:
    ```bash
    Python 3.10.9 (main, Mar  1 2023, 12:33:47) [Clang 14.0.6 ] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```
___
### Docker
1. Run Docker daemon
    * **Windows and Mac**
        
        Only open Docker Desktop, Docker will be started automatically.

    * **Linux**

        On Ubuntu and Debian systems, you can start the Docker daemon service manually using the following command:
        
        ```bash
        sudo systemctl start docker
        ```
2. Try running either of these commands on Powershell or cmd, if docker is installed, you should get a error free response:
    ```bash
    docker --version
    ```
    
    You should see something like this:

    ```bash
    Docker version 24.0.2, build cb74dfc
    ```

3. Then, run this code:
    ```bash
    docker run --rm hello-world
    ```

    If Docker is installed correctly, you will see a message indicating that the installation is working.
    ```bash
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    719385e32844: Pull complete
    Digest: sha256:926fac19d22aa2d60f1a276b66a20eb765fbeea2db5dbdaafeb456ad8ce81598
    Status: Downloaded newer image for hello-world:latest

    Hello from Docker!
    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
    1. The Docker client contacted the Docker daemon.
    2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
    3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
    4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.

    To try something more ambitious, you can run an Ubuntu container with:
    $ docker run -it ubuntu bash

    Share images, automate workflows, and more with a free Docker ID:
    https://hub.docker.com/

    For more examples and ideas, visit:
    https://docs.docker.com/get-started/
    ```
    
    > **Note**  
     In case you get the error `port is already allocated`, stop any service running on that port, or change to another port.
    
___
### Docker Compose
Docker Desktop does include docker-compose in the installation. In order to start Docker Compose, only follow the next steps:

1. Run Docker daemon
    * **Windows and Mac**
        
        Only open Docker Desktop, Docker will be started automatically.

    * **Linux**

        On Ubuntu and Debian systems, you can start the Docker daemon service manually using the following command:
        
        ```bash
        sudo systemctl start docker
        ```

2. Run this command to check the Docker Compose version.
    ```bash
    docker-compose version
    ```

    Output:
    ```bash
    Docker Compose version v2.18.1
    ```


### GitHub Desktop
Launch the GitHub Desktop program, and follow the steps below:

1. Launch GitHub Desktop.
2. Sign in with your GitHub account. If you don't have an account, you can create one on the GitHub website: [GitHub Sign Up](https://github.com/join).
3. Click on "File" in the menu bar and select "Clone Repository" or "Clone a Repository from Internet".
4. In the "Clone a Repository" window, you have several options:
    * GitHub.com: If the repository you want to clone is hosted on GitHub.com and you have access to it, select "GitHub.com" and sign in with your GitHub credentials. Then, choose the repository you want to clone from the list of available repositories.
    * GitHub Enterprise: If your repository is hosted on a GitHub Enterprise instance, select "GitHub Enterprise" and enter the URL of the GitHub Enterprise instance. Sign in with your GitHub credentials and choose the repository.
    * URL: If you have the URL of the repository you want to clone, select "URL" and enter the repository URL. Then, choose the local directory where you want to clone the repository.
    For the ITESM MLOps course, the repo link is `https://github.com/carloslme/itesm-mlops.git`.
5. Click on the "Clone" button to start the cloning process. GitHub Desktop will download the repository and create a local copy on your computer.
6. Once the cloning process is complete, you will see the cloned repository listed in GitHub Desktop. You can now start working with the repository, making changes, and committing them back to GitHub.

