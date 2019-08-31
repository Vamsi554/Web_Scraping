# User Post
from Post import Post
import datetime as dt

# User
class User:
	# Constructor
	def __init__(self, profile_url):
		self.profileUrl = profile_url
		self.userPostList = list()

	# Fetch User Profile URL
	def fetchUserProfileUrl(self):
		return self.profileUrl

	# Fetch User Name 
	def fetchUserProfileName(self):
		return self.profileName

	# Fetch User Handle
	def fetchUserProfileHandle(self):
		return self.profileHandle

	# Fetch User Profile Image
	def fetchUserProfileImage(self):
		return self.profileImage

	# Fetch User Followers Count
	def fetchUserFollowersCount(self):
		return self.followersCount

	# Fetch User Following Count
	def fetchUserFollowingCount(self):
		return self.followingCount

	# Fetch User Total Posts
	def fetchUserPostsCount(self):
		return self.postsCount

	# Fetch User Total Video
	def fetchUserVideosCount(self):
		return self.videosCount

	# Fetch User Post Details
	def fetchUserPostDetails(self):
		return self.userPostList

	# Initialize the Basic User Profile Details
	def initializeBasicDetails(self, profile_json):
		self.profileName = profile_json.get('full_name')
		self.profileHandle = profile_json.get('username')
		self.profileImage = profile_json.get('profile_pic_url_hd') 
		self.followersCount = profile_json.get('edge_followed_by').get('count')
		self.followingCount = profile_json.get('edge_follow').get('count')
		self.postsCount = profile_json.get('edge_owner_to_timeline_media').get('count')
		self.videosCount = profile_json.get('edge_felix_video_timeline').get('count')

	# Initialize the User Post Details
	def initializeUserPostDetails(self, posts_json_list):

		for i in range(len(posts_json_list)):
			posts_json = posts_json_list[i]
			postIdentifier = posts_json['node']['id']
			postTimeStamp = posts_json['node']['taken_at_timestamp']
			postUploadDateTime = dt.datetime.fromtimestamp(postTimeStamp).strftime('%d-%b-%Y %I:%M %p')
			#postImageUrl = posts_json['node']['display_url']
			postImageUrl = posts_json['node']['thumbnail_resources'][1]['src']
			postCommentsCount = posts_json['node']['edge_media_to_comment']['count']
			postHeadingByUserList = posts_json['node']['edge_media_to_caption']['edges']
			headingByUser = ''
			if len(postHeadingByUserList) > 0:
				postHeadingByUser = postHeadingByUserList[0]
				headingByUser = str(postHeadingByUser['node']['text']).strip()

			postLikesCount = posts_json['node']['edge_media_preview_like']['count']
			postLocation = posts_json['node']['location']
			if postLocation != None:
				postLocation = posts_json['node']['location']['name']
			else:
				postLocation = ''

			captionText = posts_json['node']['accessibility_caption']
			postCaption = ''
			if captionText != None:
				postCaption = captionText[captionText.find(':')+1:len(captionText)].strip()

			# Add User Post
			userPost = Post(postIdentifier, postUploadDateTime, postImageUrl, postCommentsCount, postLikesCount, postLocation, postCaption, headingByUser)
			self.userPostList.append(userPost)
