from datetime import datetime


def crontab():
    # string = 'Give permission for editing your crontab'
    # subprocess.run(["echo", string])
    # # subprocess.run(["sudo nethogs"])
    # # ENV = "$VIRTUAL_ENV"
    # # subprocess.run(["echo", $VIRTUAL_ENV])

    # p1 = subprocess.run(["cat", "items.json"], capture_output=True, text=True)
    # print(p1.stdout)
    # sudo crontab -u {} -e
    # p1 = subprocess.run(["whoami"], capture_output=True, text=True)
    # print(p1.stdout)

    # # make changes with p1
    # string = 'crontab -u {} -e'.format(p1.stdout)

    command = """ 
        crontab -l > mycron     
        echo "00 09 * * 1-5 echo hello" >> mycron
        crontab mycron
        rm mycron
    """


print(datetime.now())
