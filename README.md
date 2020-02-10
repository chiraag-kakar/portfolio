# Personal Web Portfolio
![Homepage](https://raw.githubusercontent.com/seeej/web-portfolio/master/static/assets/images/PortfolioHomePage.png)

## Built with
* [Django 2.2.2](https://www.djangoproject.com/)
* JavaScript
* [Python 3.6.8](https://www.python.org/)
* SQLite

## Instructions
1. Install [Python](https://www.python.org/) (v.3.6.8 is recommended).
1. Clone or download this repository.
1. Using a command prompt/terminal, go the project folder: `/web-portfolio/`
1. Install the dependencies: 
`pip install -r requirements.txt`
1. Create migration files for the database:
`python manage.py makemigrations`
1. Apply migrations: 
 `python manage.py migrate`
1. Run the server:
`python manage.py runserver [port number, default=8000]`
1. Using a web browser, go to `http://127.0.0.1:[port]/`

