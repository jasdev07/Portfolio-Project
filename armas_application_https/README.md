# ARMAS_APPLICATION_HTTPS

This project is configured to run an HTTPS-enabled web application with self-signed certificates. It consists of a backend service built with FastAPI, a frontend service using Nuxt.js, and an Nginx server acting as a reverse proxy to enable HTTPS.

Note: This code is intentionally incomplete and is meant for portfolio purposes only.


## Directory Structure

- `certs`: Contains the self-signed SSL certificates for HTTPS.
- `services`: Contains the source code for the individual services.
  - `armas_backend_fast_https`: The FastAPI backend service.
  - `armas_frontend_nuxt_https`: The Nuxt.js frontend service.
- `nginx_https`: Contains the Nginx configuration to route traffic and enable HTTPS.
  - `Dockerfile`: The Dockerfile to build the Nginx container image.
  - `nginx.conf`: The configuration file for Nginx.
- `.env`: Environment variables for the services.
- `docker-compose.yml`: Docker Compose configuration to orchestrate the containers.
- `README.md`: This file, which provides documentation for the project.

## Pre-requisites

Before running the application, you must create an `.env` file in the root directory of the project with the necessary environment variables.

### Creating the .env file

Create a file named `.env` in the root of the project and include the following environment variables:

```env
# Backend API URL
BACKEND_API_URL=https://localhost:7443/api

# Frontend URL
ALLOWED_ORIGINS=https://localhost:7443/,https://127.0.0.1:7443/,https://34.172.30.255:7443/
```
Replace 34.172.30.255 with your actual server IP address.
HTTPS Configuration

The application uses HTTPS with a self-signed certificate, which can generate warnings in the browser because the certificate is not signed by a known Certificate Authority. This setup is intended for development purposes.

## Usage

To start the application, ensure Docker is installed on your machine, and then run:

```bash
docker-compose up --build
```
The application will be accessible at https://localhost:7443/, with the backend API at https://localhost:7443/api.
Important Notes

    The self-signed certificate will cause browsers to warn about an untrusted certificate. You can proceed with the untrusted certificate for development purposes.
    Make sure to replace the placeholder IP 34.172.30.255 with your actual public IP address in the .env file.

Ensure that the .env file is never committed to version control, especially if it contains sensitive information. It's recommended to add .env to your .gitignore file.

## Deployment to GCP Instructions

In order to deploy the application to Google Cloud Platform, you need to set the appropriate permissions and ownership for the application files. Run the following commands in your terminal:

1. Set recursive permissions for the `armas_application_https` directory to be fully open:

    ```
    sudo chmod -R 777 armas_application_https
    ```

    This command allows all users to read, write, and execute files in the `armas_application_https` directory. This level of openness is not recommended for production environments due to security risks, but it may be necessary for some deployment workflows or during troubleshooting.

2. List the detailed permissions for the `armas_backend_fast_https` source directory:

    ```
    ls -l armas_application_https/services/armas_backend_fast_https/src/
    ```

    This command displays the file permissions, ownership, and modification date for all the files located in the specified directory.

3. Change the ownership of the `armas_application_https` directory to the current user:

    ```
    sudo chown -R $USER:$USER armas_application_https
    ```
    
    This command recursively changes the owner and group of the `armas_application_https` directory (and all of its subdirectories) to the current logged-in user. This can resolve permission issues where the current user needs to have control over the files, such as for editing or running scripts.

Please note:
It is essential to understand the security implications of using `sudo chmod -R 777`. This command gives read, write, and execute permissions to everyone. Such permissions can create significant security vulnerabilities, particularly on a public-facing server. It is best to apply the most restrictive permissions necessary for your application to function. Typically, `777` permissions should only be used temporarily and in a safe testing environment. Always revert to more secure permissions for production environments.
