class Movie():
	"""This is the Movie class docstring

		Attributes:
			title (str): This is the title of the movie
			storyline (str): This gives the brief synopsis of the movie
			poster (str): This is a URL for the box-art
			trailer (str): This is a URL for the trailer
			ratings (str): This is the movie rating
			
	"""
	def __init__(self, title, storyline, poster, trailer, ratings):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster
		self.trailer_youtube_url = trailer
		self.rating = ratings
