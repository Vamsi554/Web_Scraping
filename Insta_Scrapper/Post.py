# Post

class Post:
	# Constructor
	def __init__(self, identifier, uploadDateTime, imageUrl, commentsCount, likesCount, location, caption, headingByUser):
		self.id = identifier
		self.uploadDateTime = uploadDateTime 
		self.imageUrl = imageUrl
		self.commentsCount = commentsCount
		self.likesCount = likesCount
		self.location = location
		self.caption = caption
		self.headingByUser = headingByUser

	# Fetch User Post Identifier
	def fetchPostIdentifier(self):
		return self.id

	# Fetch Post Upload Date Time 
	def fetchPostUploadTimeStamp(self):
		return self.uploadDateTime

	# Fetch Post Image URL
	def fetchPostImageUrl(self):
		return self.imageUrl

	# Fetch Post Comments Count
	def fetchPostCommentsCount(self):
		return self.commentsCount

	# Fetch Post Likes Count
	def fetchPostLikesCount(self):
		return self.likesCount

	# Fetch Post Location
	def fetchPostLocation(self):
		return self.location

	# Fetch Post Caption
	def fetchPostCaption(self):
		return self.caption

	# Fetch Post Heading By User
	def fetchPostHeadingByUser(self):
		return self.headingByUser
