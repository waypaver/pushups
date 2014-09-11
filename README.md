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

## Working on the frontend

If you want to work on the frontend do this stuff. If not you don't have to worry about what follows.

### TLDR (in Only 5 Steps!)

1. Inside pushups/pushups where package.json is type: npm install
2. Then: bower install
3. Then: gulp watch.
4. You are now ready to edit or add any files into assets and gulp will automagically do everything. 
5. If you want more detail keep reading.


#### Too Long and Did Read! (Good on you!)

npm install

This will install all node dependencies listed in package.json including: bower, gulp, and all gulp plugins. If it fails install node.

bower install

This will install all frontend dependencies listed in bower.json into bower_conponents. You know, in case you need to look at them or something. They have already been concatenated in vendor.min.js and vendor.min.css, so you don't need to grab these unless you are adding to them or, like I said, want to look at them.

gulp watch

This will start the instructions in gulfile.js. 

You already have the Gulp config file aka gulpfile.js. I have configured it so you don't need to do anything it just works.

This will the gulp task to watch all files in pushups/pushups/assets and bower_components

If you add frontend libraries with bower install libraryname --save gulp will take those files, do it's magic and your page will be updated on refresh. 

Same thing goes for editing or adding files in pushups/pushups/assets. Gulp is watching and will update the files in pushups/pushups/static (where Django is looking for files and where I have edited the base.html file to look for static files). 

***No need to add any sources to the HTML as all files are concatenated into main.min.css, vendor.min.css, main.min.js, and vendor.min.js.

## Contributing

1. Fork this repo
2. Make your changes (with tests)
3. Submit a Pull Request




