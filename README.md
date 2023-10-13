# dracobot2

There are 2 ways to run the bot: Docker or locally.

## Run on docker

### System Requirements

1. Docker
2. Python (for development)

### Prerequisites

1. Create two Telegram tokens from BotFather, for development and production
2. Create a `.env` file and copy the template from `env.sample`. Populate the respective values for production and development environments.

### Running the bot

1. Run `docker compose -f docker-compose.{environment}.yml up -d`

- change {environment} to dev or prod
- For prod, if you have made any new changes to the code, you will need to build the image first and change the image name under the "telegram-app" service in the docker compose file. See [Hosting for production](#hosting-for-production) for more info.

2. If it's the first time setting up, follow the steps under [Populating the database](#populating-the-database). Else, you can start testing out your bot.

### Stopping the bot

1. Run `docker stop container_name_or_id`

### Populating the database

1. Make sure both services are running.
2. Run `docker ps`
3. Copy the container name of the telegram bot service
4. Make sure that `import.csv` file is already pre-populated with rows. Run `docker exec -it {container-name} python mass_import.py`
5. To add new people into the database, clear the import.csv and add in their data. This is to avoid duplicate key error (room for future improvement)

### Inspecting the docker database

1. Make sure that the mysql docker database service is running.
2. Run `docker ps`
3. Copy the container name of the database service
4. Run `docker exec -it {container-name} mysql -u root -p`. Enter the database password when prompted.
5. In `mysql` client, run `USE dragon_trainer;` (`USE dragon_trainer_prod` for production) followed by `SHOW TABLES;`. The tables should be properly configured if telegram-app service runs successfully.

### Hosting for production

For production, you may consider building the telegram bot docker image and pushing it to Docker Hub. `docker-compose.prod.yml` then pulls this image. This version uses `mraihandev/dracobot2-telegram-app` image. You may build and use your own image.

1. Build the image: `docker build -t your-image-name .`
2. Create a Docker account if not yet created (https://hub.docker.com/)
3. Login to Docker Hub: `docker login`
4. Tag your image: `docker tag your-image-name your-dockerhub-username/your-image-name:tag`
5. Push your image: `docker push your-dockerhub-username/your-image-name:tag` (Make sure to test that this image works by running `docker-compose.prod.yml` with the new full image name before pushing)
6. In `docker-compose.prod.yml`, replace the image name under `telegram-app` service to your `your-dockerhub-username/your-image-name:tag`
7. You can then copy over the `docker-compose.yml` file to any production environments (make sure that the architecture [ARM, x64 etc.] works for your image. Use `docker inspect your-image-name` to identify the architecture). For Dragon & Trainer 2023, we host it on AWS EC2 instance with x64 architecture.

### Common bugs and troubleshooting

1. Error unpickling conversationbot: delete `conversationbot` file in the root directory
2. If anything goes wrong with the bot, it could either be due to the db or telegram-app service. You may use the following command to restart the containers: `docker restart container_name_or_id`
3. You may view the docker logs for troubleshooting using `docker logs -f container_name_or_id`
4. dns error (see below)

```
ERROR: failed to solve: failed to fetch oauth token: Post "https://auth.docker.io/token": dial tcp: lookup auth.docker.io on [::1]:53: read udp [::1]:63799->[::1]:53: read: connection refused
```

4.1. run the following in your terminal

```
export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0
```

## Run locally

### System Requirements

1. Python (>= 3.8.10)
2. Pip (>= 21.2.4)
3. MariaDB (>= 10.3.9) (or MySQL)
4. virtualenv (>= 20.8.1) (if setting up project in virtual environment)

### Setting up in Virtual Environment

1.  Setup Virtual Environment

    ```
    $ python -m venv venv
    ```

2.  Activate Virtual Environment

    ```
    $ source venv/bin/activate
    ```

3.  Update pip to latest version

    ```
    $ python -m pip install --upgrade pip
    ```

4.  Repeat the above steps to set up the project in the virtual environment
    Run the following code to deactivate the virtual environment
    ```
    $ deactivate
    ```

Note: Run all future commands after activating virtual environment to ensure consistencies

### Getting Started

1.  Install Python Dependencies

    ```
    $ pip install -r requirements.txt
    ```

2.  Create the environment file (make a copy of `env.sample` and rename it to `.env`).
    Add the details for each environment variable.

    ```
    TELEGRAM_BOT_TOKEN=<put_your_telegram_bot_token_here>
    ```

3.  Create database

    ```
    $ python setup.py
    ```

4.  Run the python telegram server
    ```
    $ python main.py
    ```
