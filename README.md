# AnchorDeployerWeb

## SetUp

Make python3 virtual environment

`python3 -m venv venv`

Enable virtual environment

`source venv/bin/activate`

Install dependencies

`pip install -r requirements.txt`

Create database (not necessary for this project but it comes with django)

`python manage.py migrate`

## Run

`python manage.py runserver 127.0.0.1:8000`

## Deployment Scripts

By default, dummy scripts are used by the deployer. In order for the deployer to work,
you must put the production deployment and health check scripts in the `cloud-help-charts` 
directory. The names of the scripts are hardcoded in `anchor_deploy/deployer.py`.
