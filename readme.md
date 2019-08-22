# COIN IDENTIFIER!

## Installation
This app is built with Javascript and Python, so make sure you have `pip` installed so you can install the python packages. Here is an [installation guide for pip](https://pip.pypa.io/en/stable/installing/).

```
$ git clone https://github.com/wanderdust/coin-cnn-webapp.git
$ cd coin-cnn-webapp
```

## Create a virtual environment

Create the [virtual environment ](https://virtualenv.pypa.io/en/latest/) and activate it:

```
$ virtualenv venv
$ venv/bin/activate
```

Install all the dependencies for both javascript and python:
```
$ npm install
$ pip install requirements.txt
```

To deactivate the virtual environment:
```
$ deactivate
```
## Usage:

Get the server up and running in `localhost:5000`
```
$ npm start
```

Get the dev server up and running in `localhost:8080`
```
$ npm run dev-server
```

Run the test suite

```
$ npm run test
```

Run build

```
$ npm run build:prod
```

## How it works:
Choose an image of a coin and let the app make a prediction. It will tell you the value of the coin, type of currency and country of origin.
