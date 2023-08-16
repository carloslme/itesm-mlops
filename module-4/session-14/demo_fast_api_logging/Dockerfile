# This sets the base image for the Docker container to be the official Python 3.11 image from Docker Hub. This image contains a minimal installation of Python.
FROM python:3.11 

# This sets the working directory inside the container to /src. This is where the application code will be copied and where subsequent commands will be executed.
WORKDIR /src 
# This copies the requirements.txt file from the host (the directory where the Dockerfile is located) to the /src directory inside the container. The requirements.txt file typically lists the Python packages required by the application.
COPY requirements.txt ./ 
# This copies the entire src directory from the host to the /src directory inside the container. The src directory likely contains your application code and files.
COPY src ./ 
# This command runs inside the container and installs the Python packages listed in the requirements.txt file. The --no-cache-dir flag prevents pip from using cache during the installation, which helps to keep the image smaller.
RUN pip3 install --no-cache-dir -r requirements.txt 
# This command updates the package index inside the container and then installs the vim text editor. This is a common practice for development purposes, as it allows you to have a text editor available within the container for debugging and editing.
RUN apt-get update && apt-get install -y vim 

# This instruction indicates that the container will expose port 8000. However, it doesn't actually publish the port to the host; that needs to be done when running the container using the -p flag.
EXPOSE 8000
# This sets the default command that will be executed when the container starts. It runs the Uvicorn ASGI server to serve the FastAPI application. The arguments specify the host as 0.0.0.0 (meaning the container will listen on all available network interfaces), the port as 8000, and --reload enables automatic reloading of the server when code changes are detected. The "main:app" argument points to the app instance in the main module (Python file) inside the src directory.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]