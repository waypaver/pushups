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

## Working on the frontend

If you want to work on the frontend do this stuff. If not you don't have to worry about what follows.

1. Install Node if you don't have it (check with node -v)
2. In terminal navigate to the pushups app folder so pushups/pushups you will see package.json. Now type: npm install

This will install all node dependencies listed in package.json including: bower, gulp, and all gulp plugins.

You already have the Gulp config file aka gulpfile.js. I have configured it so you don't need to do anything it just works.


### Here's what you need to know to actually edit files and see them update HTML.

Inside pushups/pushups type in terminal: gulp watch

This will the gulp task to watch all files in pushups/pushups/assets and bower_components

If you add frontend libraries with bower install libraryname --save gulp will take those files, do it's magic and your page will be updated on refresh. 

Same thing goes for editing or adding files in pushups/pushups/assets. Gulp is watching and will update the files in pushups/pushups/static (where Django is looking for files and where I have edited the base.html file to look for static files). 

There is no need to add any sources to the HTML as all files are concatenated into main.min.css, vendor.min.css, main.min.js, and vendor.min.js.


