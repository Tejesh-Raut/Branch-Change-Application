Group number : 08

Group members : (Tejesh Raut, 140050008),(Shrey Kumar, 140050014),(Gangesh Gudmalwar, 140050058)

Individual percentages:
Tejesh	:	95%
Shrey	:	100%
Gangesh	:	100%

We pledge on our honour that we have not given or received any unauthorized assistance on this assignment or any previous task.

Instructions:

Ensure that Django 1.8.5 and python 3.4 are installed in the system
django-import-export is on the Python Package Index (PyPI), so it can be installed with standard Python tools like pip or easy_install: $ sudo pip install django-import-export

There are two admins with names admin (password: admin) and Gangesh (password: 12345689)

Now go into the folder mysite1 (outer) and run the command $ python3 manage.py runserver

Now open the browser and go to the address http://127.0.0.1:8000 and user will be asked login and password. Only admin can create new users

Now go to the address http://127.0.0.1:8000/admin/ and login through the given admin usernames and password and add as many users as you want

Now you can go to the address http://127.0.0.1:8000 by clicking on the link viewsite present at the right-top side of the webpage and login as the user created 

You will be then asked to fill the form

You must fill the form correctly as mentioned in the feature_doc.txt file

Admin can import a csv to store in the database (presently our application stores a first extra column to store ID, you will have to edit the csv file before importing. In the csv file add an extra first column and store any arbit different numbers in that column for every row).

Admin can export the user inputs database as csv format. To do this go to admin homepage and then click on Roll_nos link under the bc section. In the action dropdown list there are options to delete and export selected entries as a csv file and then click go to download the file ( Again the format in which we store the data in the csv file is bit different than that of sir. A extra column is added in the begining representing ID)

To run the branch change algorithm presently you will have to manually run it from a makefile present in the outer mysite folder. You should provide the files input_options.csv and input_programmes.csv as given in the outlab. Now go through the terminal to the folder code and run make

After running the make a allotment.csv file will be created as mentioned

*Presently the algorithm has some flaws hence some of the candidates after 23rd row are not alloted properly if the input_options.csv file of the outlab resources is used. The algorithm does not detect some of the tricky cases

Citations :

1.https://docs.djangoproject.com/en/1.8/
2.http://stackoverflow.com/questions/23550985/how-to-break-a-while-loop-from-an-if-condition-inside-the-while-loop
3.https://docs.djangoproject.com/en/1.8/ref/forms/validation/
4.http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list-in-python
5.https://django-import-export.readthedocs.org/en/latest/getting_started.html#creating-import-export-resource
6.https://djangogirls.org/
7.https://docs.djangoproject.com/en/1.8/ref/models/fields/
8.http://www.tangowithdjango.com/