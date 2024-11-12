
# Weather Forecast Web Application

![image](https://github.com/hrisikesh-neogi/weather-app/assets/78023847/0665d001-c366-47d1-9c49-ab9b726a9453)

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Description

The Weather Forecast Web Application is a Flask-based web app that allows users to retrieve live weather forecasts for specific locations. Users can simply enter a location, and the application will provide them with detailed weather information, including temperature, wind speed, humidity, and more. This project serves as a simple and interactive way to access up-to-date weather data.


## Features

- Live weather forecast retrieval based on user-input locations.
- Temperature information in both Celsius and Fahrenheit.
- Details such as wind speed, humidity, pressure, and more.
- User-friendly and responsive design.
- Error handling for incorrect location entries.

## Technologies Used

- Flask: A lightweight Python web framework for building web applications.
- Python Requests: A library for making HTTP requests to retrieve weather data from an external API.
- Bootstrap: A front-end framework for creating responsive and visually appealing user interfaces.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MuzahidulIslam1/Weather-app/
   cd weather-app
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Retrieve your API KEY, API HOST, and URLs from the RapidAPI platform.

   - Visit RapidAPI and look for the WeatherAPI.com service. [Click here.](https://rapidapi.com/weatherapi/api/weatherapi-com/)
   - Then, select the "Subscribe to Test" and "Subscribe to the Free Basic Plan," which comes at no cost.
   - Search for the api-key named `X-RapidAPI-Key`

3. Create a `.env` file for API keys:

   Create a file named `.env` and add your weather API key as follows:

   ```python
   #change the API_KEY and rest will be the same.

   API_KEY = 'your-weather-api-key-from-rapid-api' 
   API_HOST = "weatherapi-com.p.rapidapi.com"
   API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://localhost:5000`.




## Usage

1. Enter a location in the input field and click "Get Weather."
2. The application will display the live weather forecast for the entered location.
3. Enjoy real-time weather information!


