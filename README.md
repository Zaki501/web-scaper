# Amazon item price tracker
## Running the script daily (unix/macOS)
To run a script at regular intervals, use crontab
```bash
sudo crontab -u <username> -e
```
Use https://crontab.guru/ to help create a schedule

For example, to run a the script at midday everyday:
```bash
0 12 * * * 
```

PATH TO VENV: echo $VIRTUAL_ENV
pyinstaller - make installable for windows

# PostgreSql Database
Download postgres in backend server, then:
```bash
sudo -u postgres psql
```
Once you are in the psql CLI, create the Database and grant priveleges:
```psql
CREATE DATABASE mydb;
CREATE USER <name> with encrypted password '<password>';
GRANT ALL PRIVILEGES ON DATABASE mydb TO <name>;
```
The python script will create the tables for you.