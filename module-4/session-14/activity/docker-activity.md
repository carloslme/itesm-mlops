
# Activity Docker

In this activity, you will migrate a Fast API application to a Docker application.

## Task

Create a copy of the [demo_fast_api_logging](../../session-13/activity/activity-logging.md) project in session 13, and modify it to meet the requirements below:

* Create a `Dockerfile` file to copy all the necessary content and expose it in the port 8000
* Include the well-explained instructions to:
  * Build the image
  * Run the container
  * Debug the container (how to access it)
  * Make predictions on local machine
  * Copy logs (if implemented) from container to local machine

## Extra

* **Copy automatically the files generated in the container to local machine**  

    You can do this in several ways:

    1. Add a configuration in the `Dockerfile` file.
    2. Run the `docker run ...` command with an specific configuration to copy the preferred files to the local machine.
