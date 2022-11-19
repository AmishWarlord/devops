# This project creates a simple uWSGI server with a MSSQL database backend and a flask frontend to display SQL select results. 
## Make sure to fill out the .env.example file and then change its name to ".env" before running "docker-compose up"
## NOTE: the server takes a little longer to start than the app. If you receive a 500 error on startup, wait about 30 seconds and then refresh your browser.

### To customize your tables, you can add .sql or .sh files to the db/ folder. Each file will be executed in alphabetical order on startup. sql files are easier to implement, but you can use .sh files if you want to make use of environment variables. Two examples of .sh files are provided. If you do use .sh files, make sure of two things:
1. that your line endings are Unix-supported (LF, not CRLF). 
2. that you specify the root username and password in your call. 