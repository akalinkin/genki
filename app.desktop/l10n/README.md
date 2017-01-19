# Working with locale strings

1 add your strings into app_strings.py

2 run command:
    
    pygettext -d app app_strings.py
    
it will update *app.pot* file using *app_strings.py* as a source

3 open en_US/LC_MESSAGES/app.po using POEdit

4 update project from POT file 'catalog -> update from POT file'

5 edit translations of strings

6 save app.po file

7 update app.mo file 

    file -> compile to MO format

8 repeat steps 3-7 for every language

# Database migrations

1 modify model package as you need

2 restart project and it will update database 
