# Filament Manager
3D printing filament manager made with Django. It's still a work in progress, readMe included, so it will be updated frequently in the coming weeks.

The core idea is to create a simple web interface for a local SQLite database to manage 3D printer filaments, storing material settings and properties, with the possibility to leave comments (perhaps these should be renamed notes?) on each filament.

## To Do List (not ordered):

- [ ] Deploy a demo on GitHub Pages
- [ ] Add a way to sort and group filaments
- [ ] Add a way to search for a specific filament
- [ ] Add the option to add custom material
- [ ] Add the ability to comment with pictures
- [ ] Add the ability to manage filaments (currently requires logging in as admin)
- [ ] Add the ability to import JSON from major slicers (e.g., OrcaSlicer)

## Current state screenshots:
Background image courtesy of <a href="https://www.freepik.com/free-photo/psychedelic-paper-shapes-different-color-tones_25633736.htm">Freepik</a>

![image](https://github.com/GiorgioMiglia/Filament-manager/assets/48253331/6017d396-0c11-4520-aa18-129bede04096)

![image](https://github.com/GiorgioMiglia/Filament-manager/assets/48253331/8eb17bd4-f513-4f84-88f1-606a844bafcb)


## How to install:
<a href=https://docs.djangoproject.com/en/5.0/intro/install/>Install Django</a>

Start a project:
```
django-admin startproject mysite
```
Copy all the content of this repo (you can ignore the asset folder) in the folder of your project `mysite`. You will be prompted to replace some files, accept. 
It's not the best solution but it's still a work in progress.
### DONE!

To run the project, run this command from inside the `mysite` folder:

*Unix*
```
python manage.py runserver
```
*Windows*
```
py manage.py runserver
```
