# genki

Personal helper project to keep all your notifications, plans, tasks and etc. in one place

## Requirements

- python3 ( `sudo apt-get install python3` )
- sqlalchemy ( `sudo apt-get install python3-sqlalchemy` )
- Qt5 ( `sudo apt-get install python3-pyqt5 pyqt5-dev-tools` )
- psycopg2 ( `sudo apt-get install python3-psycopg2` )
- postgresql ( `sudo apt-get install postgresql `)

Configure postgresql database

    sudo -u postgres psql

    alter user postgres with password 'YOUR_PASSWORD_HERE'; #TODO: Create new user for service

    create database my_helper; # TODO: Grant required permissions for service user to database

    \q

## Tools

- IDE (like PyCharm or any other you love)
- POEdit ( `sudo apt-get install poedit` )

## Create startup

Copy **genki.desktop** to **~/.config/autostart** folder

    cp genki.desktop ~/.config/autostart/

and change `Exec=python3 /path/to/app/app.py` to correct location