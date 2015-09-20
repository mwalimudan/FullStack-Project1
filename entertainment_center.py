import media
import fresh_tomatoes

star_wars = media.Movie("Star Wars", 
						"http://theartmad.com/wp-content/uploads/2015/06/Star-Wars-Poster-6.jpg", 
						"www.youtube.com/watch?v=vP_1T4ilm8M")

two_towers = media.Movie("Lord of The Rings: The Two Towers", 
						 "http://img4.wikia.nocookie.net/__cb20150203041214/lotr/images/9/98/The_two_tower.jpg", 
						 "https://www.youtube.com/watch?v=2dlRvAjU_RI")

terminator = media.Movie("The Terminator", 
						 "http://imgc.allpostersimages.com/images/P-473-488-90/17/1723/KK53D00Z/posters/the-terminator.jpg", 
						 "https://www.youtube.com/watch?v=lHz95RYUbik")



movies = [star_wars,two_towers, terminator]

fresh_tomatoes.open_movies_page(movies)