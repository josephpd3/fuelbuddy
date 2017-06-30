# FuelBuddy
--------

## Progress and Milestones
--------
[X] Build out foundation w/ Django + create-react-app

[X] Add model for Price Reports

[X] Add serializers and views for Price Reports

[X] Add date bounds to Price Reports

[X] Enable Docker support to utilize Postgres and VM for Dev/Testing

[X] Add tests for Price Report Views

[X] Add Redux to React

[X] Delineate Containers and Routes for Frontend

--> **Work stopped here at roughly 4.5 hours non-contiguous work**

[] Add Google Maps support

[] Add Datepickers + data retrieval actions

[] Bound displayed markers w/ datepickers

[] Add JWT Auth to Django/React

[] Create Admin page for managing reports

## Getting Started
--------
**Warning: This has not been tested with Docker on Windows or Linux**

The easiest way to run the application locally for development is with `docker-compose`. Ensure that you have Docker installed, navigate to the root directory of the project, and run `docker-compose up`. Docker will spin up an instance of PostgreSQL and a backend instance of Django which can be interacted with via `http://localhost:8000`.

## Running Tests
--------
The application is built such that you just need to pass test commands into Django via `docker-compose`:

`docker-compose run backend python manage.py test`

Django's test discovery handles the rest, but you can pass whatever arguments into `test` you please:

`docker-compose run backend python manage.py test -v 3` (makes it super verbose)
