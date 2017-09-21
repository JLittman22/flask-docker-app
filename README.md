# flask-docker-app
- [x] Start with a docker container that runs Python Flask. Make a hello world app you can access from your local web browser.

- [] Take the same flask hello world app you wrote and make it TWO docker containers, one with only python installed and one with only nginx install and make the NGINX container show your python flask hello world app.

- [] Add a database container with the other two container, now three containers total. Use docker-compose to start up all three containers. update your webapp to insert some data into the database (Use posgres as your database, data can be just the string "hello world" into a single column table). 