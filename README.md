# Python Web-Scraper 

## Get a screenshot:

```bash
python app.py <url>
```
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