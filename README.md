# Pushups

## Installation and technology

Here's what you'll need to get everything working:

### Install postgres

    $ brew install postgresql
    $ createdb pushups

### Install virtualenv

    $ pip install virtualenv
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

### Install foreman

We use foreman to manage all of our processes.  It also lets us manage all of
our environment variables with a .env file.

    $ gem install foreman
    $ foreman start

### Get Twilio working

In order to use django twilio we have to add some specific environment variables
to our .env file.

    # .env
    TWILIO_AUTH_TOKEN=sometoken
    TWILIO_ACCOUNT_SID=someothertoken

Now when you start foreman you should be able to use twilio

## Contributing

1. Fork this repo
2. Make your changes (with tests)
3. Submit a Pull Request
