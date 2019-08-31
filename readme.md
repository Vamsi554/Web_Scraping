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
4) Once we retrieve the CSRF Token, we need to authenticate to instagram and proceed with extracting the data from a user's profile with a given user handle <b>@username</b>.
5) Instagram uses the feature of <b>Infinite Scrolling</b> where in initially only first 12 images are loaded specific to user and as we scroll down, the browser makes asynchronous requests to the server and the images will be loaded and displayed accordingly.
6) Instagram uses the concept of <b>Query Hash</b> to fetch user related data. We need to get this query hash for the user programatically and make a GET request to the server to get all the posts related to a specific user.
7) Once all the information is received, we can parse individual content such as name, likes, comments, etc.,
8) Below is the structure used for the Users and Posts entity

# USER Entity

Below are the values associated with <b>User</b> Entity <br>

  -> User Name <br>
  -> Profile URL <br>
  -> User Handle (<b>@username</b>) <br>
  -> Profile Image <br>
  -> Followers Count <br>
  -> Following Count <br>
  -> Posts Count <br>
  -> Videos Count <br>
  -> Posts <br>
  
# POST Entity

Below are the values associated with <b>Post</b> Entity <br>

  -> Identifier <br>
  -> Upload Timestamp <br>
  -> Image URL <br>
  -> Comments Count <br>
  -> Likes Count <br>
  -> Location <br>
  -> Caption <br>
  -> Heading By User <br>
 
 # Final HTML Template 
 
 ![template](https://user-images.githubusercontent.com/34600966/64068128-688d0380-cc51-11e9-824e-0de56fe63507.jpg)

 
 
