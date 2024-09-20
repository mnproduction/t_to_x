
# Assignment:
Build a simple application that uses telegram bot to scrap a picture from a channel and post it to X (former Twitter) account.

# INSTALLATION:
git clone blah-blah

get telegram api credentials

get twitter api credentials

> The app and the corresponding credentials must have the Write
> permission
> 
> Check the App permissions section of the Settings tab of your app,
> under the Twitter Developer Portal Projects & Apps page at
> https://developer.twitter.com/en/portal/projects-and-apps
> 
> Make sure to reauthorize your app / regenerate your access token and
> secret  after setting the Write permission

fill in .env file

during first run pyrogram will create a new session


# TODO: 
- Documentation
- THIS
- Tests

# DONE:
- Created project structure
- Added abstractions
- New logger concept: class Logger
- Added unit test for logger
- Implemented clients (Telegram and Twitter)
- Implemented manager and message processor
- Updated config file and requirements.txt
- Created .env-example file
- Created app-tweeter.py to test API functionality
- Updated config file and requirements.txt
- Updated x/client.py 
- Updated README.md
- Created app-telegram.py to test API functionality
- Updated telegram client to use it in project
- Minor bugfixes
- Pipeline telegram to x finished
