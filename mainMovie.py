import movieClass
import fresh_tomatoes

# Creates an instance of the Movie class
# Make sure that the data is placed in the correct order when initializing

the_imitation_game = movieClass.Movie("The Imitation Game", "A story about the father of computer science, Alan Turing.",
									  "https://images-na.ssl-images-amazon.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
									  "https://www.youtube.com/watch?v=S5CjKEFb-sM",
									  "3/5")
ferris_buellers_day_off = movieClass.Movie("Ferris Bueller's Day Off", "A story about a boy who lies about being sick to have a very adventurous day out.",
										   "http://pillowcinema.com/wp-content/uploads/2015/06/Ferris-Bueller-poster.jpg",
										   "https://www.youtube.com/watch?v=K-X2XzKqBiE",
										   "4/5")
groundhog_day = movieClass.Movie("Groundhog Day", "A man experiences the same day over and over again.",
								 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU0MzQyNTExMV5BMl5BanBnXkFtZTgwMjA0Njk1MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
								 "https://www.youtube.com/watch?v=tSVeDx9fk60",
								 "5/5")
movies = [the_imitation_game, ferris_buellers_day_off, groundhog_day] # Places the instances into an array

fresh_tomatoes.open_movies_page(movies) # Launches the web page

