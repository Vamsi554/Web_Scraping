# Web Scraping

1) Web scraping is the process of importing information from a website and a technique employed to extract large amounts of data from websites whereby data is extracted and further processing of data takes place.

# Three Steps to Web Scraping

1) First the piece of code used to pull the information sends an HTTP GET request to a specific website.
2) When the website responds, the scraper parses the HTML document for a specific pattern of data.
3) Once the data is extracted, it is converted into whatever specific format we require.

# Instagram Web Scraping

1) We will discuss on scraping the instagram user data using python as a programming language.
2) Instagram Scraper is a python script which takes @username as an input and returns all the information related to the user in a HTML web page where we can access information at one go. 
3) The details include the user name, handle, full name, followers, total posts, likes, comments, locations, images etc.,

# Parameter Values

INSTAGRAM_URL = <b>'https://www.instagram.com'</b> <br/>
BASE_URL = <b>'https://www.instagram.com/accounts/login/'</b> <br/>
LOGIN_URL = <b>'https://www.instagram.com/accounts/login/ajax/'</b> <br/>
USER_NAME = <b>'YOUR_USER_NAME_HERE'</b> <br/>
PASSWORD = <b>'YOUR_PASSWORD_HERE'</b> <br/>
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0' <br/>
USER_PROFILE_URL = <b>'https://www.instagram.com/@USERNAME/'</b> <br/>

# Implementation of Instagram User Scraping

1) We can use python as a programming language medium and beautiful soup for parsing the data from the instagram web interface.
2) Initially we make a GET request to instagram user account with the following parameters and fetch the required CSRF token needed for authentication purpose.
3) We will be using the above parameter values as part of request headers and then create a session object which is eventually used in getting the HTML data for the web page.

