# Instagram Data Scrapper

# Imports
import requests
from bs4 import BeautifulSoup
import json
from User import User
from Post import Post
from constants import *

# Remove EMOJI's from User Text 
def deEmojify(inputString):
	return inputString.encode('ascii', 'ignore').decode('ascii')

# Fetch the Query Hash for the User
def fetchQueryHash(session, url):
	jsContent = str(session.get(url).content)
	matchText = 'n.profilePosts.byUserId.get(t))||void 0===s?void 0:s.pagination},queryId:'
	queryHashIdx = jsContent.find(matchText)
	startIdx = queryHashIdx+len(matchText)+1
	endIdx = startIdx + 32
	return jsContent[startIdx:endIdx]

# Download the Image from given URL
def downloadPost(url, absPath):
	imgData = requests.get(url).content
	with open(absPath,'wb') as handler:
			handler.write(imgData)

# Retrieve the CSRF Token for the User Authentication
def fetchUserCsrfToken(soup):
	script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
	page = script.text.split(' = ', 1)[1].rstrip(';')
	page_json = json.loads(page)
	csrfToken = page_json['config'].get('csrf_token')
	return csrfToken

# Main Method Implementation
if __name__ == '__main__':
	session = requests.Session()
	request = session.get(BASE_URL)
	bSoup = BeautifulSoup(request.content, 'html.parser')
	# Fetch the CSRF Token
	csrfToken = fetchUserCsrfToken(bSoup)
	# Update the Session Headers
	session.headers = {'user-agent': USER_AGENT}
	session.headers.update({'Referer': BASE_URL})
	session.headers.update({'X-CSRFToken': csrfToken})
	loginData = {'username': USER_NAME, 'password': PASSWORD}
	login = session.post(LOGIN_URL, data=loginData, allow_redirects=True)
	# Fetching the User Data
	userPage = session.get(USER_PROFILE_URL)
	userContent = userPage.text
	soup = BeautifulSoup(userContent, 'html.parser')
	script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
	page = script.text.split(' = ', 1)[1].rstrip(';')
	page_json = json.loads(page)

	# Creating the User Object
	user = User(USER_PROFILE_URL)

	# Retrieve the Query Hash for the User to fetch all the profile posts.
	queryHashUrl = ''
	for jsFileUrl in soup.find_all('link', href=lambda t:"ProfilePageContainer.js" in t):
		queryHashUrl = INSTAGRAM_URL + jsFileUrl['href']

	queryHash = fetchQueryHash(session, queryHashUrl)

	# Initializing the Basic Details
	userProfileEntryData = page_json['entry_data']['ProfilePage'][0]
	user.initializeBasicDetails(userProfileEntryData['graphql']['user'])

	# Initialize the JSON Data Lists for User Posts
	userProfilePostsJsonList = []
	userProfilePostsJsonList.append(userProfileEntryData['graphql']['user']['edge_owner_to_timeline_media']['edges'])

	hasNextPage = userProfileEntryData['graphql']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
	endCursor = userProfileEntryData['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
	userIdVal = userProfileEntryData['graphql']['user']['id']

  # Run the Loop Till we no more have any User Posts to process.
	while hasNextPage == True:
		userNextPostsUrl = INSTAGRAM_QUERY_HASH_URL + 'query_hash=' + queryHash + '&variables={"id":"' + userIdVal + '","first":12,"after":"' + endCursor + '"}'
		userData = session.get(userNextPostsUrl).text
		userDataJson = json.loads(userData)
		userProfilePostsJsonList.append(userDataJson['data']['user']['edge_owner_to_timeline_media']['edges'])
		hasNextPage = userDataJson['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
		endCursor = userDataJson['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

	# Initialize the Post Details
	for idx in range(len(userProfilePostsJsonList)):
		user.initializeUserPostDetails(userProfilePostsJsonList[idx])

	# Creating HTML Template
	htmlCode = open('templateProfile.html').read()
	htmlCode = htmlCode.replace('XX_USER_XX', user.fetchUserProfileName())
	htmlCode = htmlCode.replace('XX_USER_PROFILE_IMAGE_URL', user.fetchUserProfileImage())
	htmlCode = htmlCode.replace('XX_USER_PROFILE_URL_XX', user.fetchUserProfileUrl())
	htmlCode = htmlCode.replace('XX_USER_PROFILE_NAME_XX', user.fetchUserProfileName())
	htmlCode = htmlCode.replace('XX_USER_PROFILE_HANDLE_XX', user.fetchUserProfileHandle())
	htmlCode = htmlCode.replace('XX_USER_FOLLOWERS_XX', str(user.fetchUserFollowersCount()))
	htmlCode = htmlCode.replace('XX_USER_FOLLOWING_XX', str(user.fetchUserFollowingCount()))
	htmlCode = htmlCode.replace('XX_USER_POSTS_XX', str(user.fetchUserPostsCount()))
	htmlCode = htmlCode.replace('XX_USER_VIDEOS_XX', str(user.fetchUserVideosCount()))

	htmlCodeTemplatesList = [HTML_TEMPLATE_1,HTML_TEMPLATE_2,HTML_TEMPLATE_3]
	templateCombHtmlCode = ''

	counter = 0
	flg = False
	for post in user.fetchUserPostDetails():

		htmlTemplateCode = ''
		print(counter, end=' -> ')
		htmlTemplateCode = htmlCodeTemplatesList[counter]
		htmlTemplateCode = htmlTemplateCode.replace('XX_IMAGE_URL_XX', post.fetchPostImageUrl())
		htmlTemplateCode = htmlTemplateCode.replace('XX_LOCATION_XX', post.fetchPostLocation())
		htmlTemplateCode = htmlTemplateCode.replace('XX_COMMENTS_XX', str(post.fetchPostCommentsCount()))
		htmlTemplateCode = htmlTemplateCode.replace('XX_LIKES_XX', str(post.fetchPostLikesCount()))
		htmlTemplateCode = htmlTemplateCode.replace('XX_UPLOAD_DTTM_XX', post.fetchPostUploadTimeStamp())
		htmlTemplateCode = htmlTemplateCode.replace('XX_HEADING_BY_USER', deEmojify(post.fetchPostHeadingByUser()))
		templateCombHtmlCode += htmlTemplateCode

    # Code to display data in HTML in Zig-Zag Manner
		if flg == False:
			counter = counter + 1
		if flg == True:
			counter = counter - 1
		if counter > 2:
			flg = True
			counter = counter - 2
		elif counter < 0:
			flg=False
			counter = counter + 2

	htmlCode = htmlCode.replace('XX_HTML_TEMPLATE_XX', templateCombHtmlCode)
	# Create the User Profile HTML Template
	outputHtmlFile = open(user.fetchUserProfileHandle() + '.html', 'w')
	outputHtmlFile.write(htmlCode)
	outputHtmlFile.close()
