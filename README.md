# Shrtn Ur URL

A simple URL shortener built with Python/Flask, perfect for all the lazy web surfers out there! Users can submit any https:// formatted URLs and obtain a shortened version of it. For example the URL for the Flask User Guide, https://flask.palletsprojects.com/en/1.1.x/#user-s-guide has been shortened to https://shrtn-ur-url.herokuapp.com/hyXDp

This app was created by [@roselynle](https://github.com/roselynle) and [@FaisalY12](https://github.com/FaisalY12) as part of Futureproof's Coding Challenge.

### Installation

-   Clone or download this repo 

### Usage

-   Open your terminal and navigate to the `url-shrtn` folder
-   Run `pipenv shell`
-   Run `pipenv install`
-   Run `pipenv run dev`
-   Flask API will be running on port 5000

Deployed site can be accessed here: https://shrtn-ur-url.herokuapp.com/

## Technologies

-   Python, Flask, HTML, CSS

## Process

-   Set up Flask App file structure from scratch
-   Create model and required routes
-   Configure the database
-   Implement logic for shortening the URL and redirecting the user
-   Create template html files for rendering
-   Add styling to improve user interface
-   Write tests

## Task Requirements

-   [x] Users should be able to enter a URL into an input box on your website's front page
-   [x] Your backend will then generate a shortened path at which a User can access their URL
-   [x] You must implement Python in some capacity in this application
-   [x] Store this shortened path and it's longer counterpart in a database
-   [x] No login should be required to create a shortened URL
-   [x] If User tries to access your website with a path you have stored in your database, they should get rerouted to the URL it relates to
-   [x] If User tries to access your website with a path you do not have stored in your database, they should get rerouted to the homepage where they can create a new short URL

## Wins & Challenges

### Wins

-   Deployed our website
-   Managed to use SQL Alchemy to create a database and store the URLs
-   Implemented error handling

### Challenges

-   Writing tests e.g. not knowing how to mock a 500 error code or test the short url since it searches the db for the corresponding long url
-   Not being able to get it to work with www formatted URLs

## Bugs

-   Not responsive on mobile view
