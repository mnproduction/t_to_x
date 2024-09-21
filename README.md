
# Automating Image Posting from Telegram Channel to X (formerly Twitter)

## Table of Contents

-   [Description](#description)
-   [Features](#features)
-   [Installation](#installation)
-   [Setup](#setup)
-   [Usage](#usage)
-   [Screenshots](#screenshots)
-   [Roadmap](#roadmap)
-   [Contributing](#contributing)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Description

This simple application automatically posts images from a specified Telegram channel to your X account (formerly known as Twitter). The app uses the Telegram API to retrieve images and the X API v1.1 and v2 to post them.

## Features

-   **Automatic Image Retrieval**: Fetches images from a specified Telegram channel in real-time.
-   **Automated Posting**: Posts the retrieved images to your X account with a customizable caption.
-   **Configurable Settings**: Easily configure API credentials and other settings via a `.env` file.
-   **Logging**: Comprehensive logging to monitor the application's activities and debug issues.

## Installation

### Clone the Repository

`git clone https://github.com/mnproduction/t_to_x
cd your_repository` 

### Install Dependencies

Ensure you have Python 3.7 or higher installed.

Install the required dependencies:

`pip install -r requirements.txt` 

## Setup

### Obtain API Credentials

#### Telegram API

1.  Sign up at [my.telegram.org](https://my.telegram.org/).
2.  Navigate to **API Development Tools**.
3.  Obtain your `API_ID` and `API_HASH`.

#### X (Twitter) API

1.  Sign up at the [Twitter Developer Portal](https://developer.twitter.com/).
2.  Create a new app under the **Projects & Apps** section.
3.  Obtain your API keys and tokens:
    -   `API_KEY`
    -   `API_SECRET`
    -   `ACCESS_TOKEN`
    -   `ACCESS_TOKEN_SECRET`
    -   `BEARER_TOKEN`

> **Important!** The app and the corresponding credentials **must have Write permission**.
> 
> Check the **App permissions** section of the **Settings** tab of your app in the [Twitter Developer Portal](https://developer.twitter.com/en/portal/projects-and-apps).
> 
> Make sure to **reauthorize** your app and **regenerate** your `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET` after setting the Write permission.

### Configure Environment Variables

Create a `.env` file in the root directory of the project based on the `.env-example` file and fill in your credentials:

    #Telegram API
    TELEGRAM_API_ID=your_api_id
    TELEGRAM_API_HASH=your_api_hash
    TELEGRAM_CHANNEL_NAME=@your_channel_name
    
    #X (Twitter) API
    X_API_KEY=your_api_key
    X_API_SECRET=your_api_secret
    X_ACCESS_TOKEN=your_access_token
    X_ACCESS_TOKEN_SECRET=your_access_token_secret
    X_BEARER_TOKEN=your_bearer_token` 

## Usage

Run the application:

`python app.py` 

On the first run, Pyrogram will create a new session. You may need to enter your phone number and confirmation code.

The application will start listening to the specified Telegram channel and automatically post new images to your X account.

## Roadmap

-   **Documentation**: Expand the documentation with more details and examples.
-   **Testing**: Write unit and integration tests for better reliability.
-   **Error Handling**: Improve exception handling and add retries for network calls.
-   **Extended Media Support**: Add support for other media types like videos and documents.
-   **Texts and captions**: Add strategy for texts of the X tweets.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your_feature_name`).
3.  Commit your changes (`git commit -am 'Add new feature'`).
4.  Push to the branch (`git push origin feature/your_feature_name`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

-   **Pyrogram**: A Telegram API framework for Python.
-   **[Tweepy](https://www.tweepy.org/)**: An easy-to-use Python library for accessing the Twitter API.
-   **Contributors**: Thanks to everyone who will contribute to this project.

----------

## Changelog

### Completed Tasks

-   Created project structure.
-   Added abstractions and interfaces.
-   Implemented a new logger concept (`class Logger`).
-   Added unit tests for the logger.
-   Implemented clients for Telegram and X (Twitter).
-   Implemented manager and message processor.
-   Updated configuration file and `requirements.txt`.
-   Created `.env-example` file.
-   Created `app-tweeter.py` and `app-telegram.py` for API functionality testing.
-   Updated `x/client.py`.
-   Updated `README.md`.
-   Updated Telegram client for project integration.
-   Minor bug fixes.
-   Completed the Telegram to X pipeline implementation.

----------

## Contact

If you have any questions or suggestions, feel free to contact me:

-   **Email:** mynovosolov@gmail.com
-   **Telegram:** @nick_od

----------

_Last updated: September 20, 2024._


