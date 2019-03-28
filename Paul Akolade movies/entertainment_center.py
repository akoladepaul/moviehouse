#Project Title: Python Project.
#Project Name: Movie Trailer
#Project Author: Paul Akolade

import fresh_tomatoes
import media


avengers = media.Movie("Avengers",
                        "When Thor's evil brother, Loki (Tom Hiddleston), gains access to the unlimited power of the energy cube called the Tesseract, Nick Fury (Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth. Joining Fury's dream team are Iron Man (Robert Downey Jr.), Captain America (Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).",
                        "https://images-na.ssl-images-amazon.com/images/I/A1t8xCe9jwL._SY679_.jpg",
                        "https://youtu.be/eOrNdBpGMv8")
print(avengers.storyline)
avengers.show_trailer()

antman = media.Movie("Antman",
                     "Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.",
                     "https://i.pinimg.com/originals/27/5e/37/275e37fe5c4de24f2d5d6009df66b1ab.jpg",
                     "https://youtu.be/pWdKf3MneyI")
print(antman.storyline)
antman.show_trailer()

spiderman = media.Movie("Spiderman",
                             "Ant-Man is a 2015 American superhero film based on the Marvel Comics characters of the same name: Scott Lang and Hank Pym. ... In Ant-Man, Lang must help defend Pym's Ant-Man shrinking technology and plot a heist with worldwide ramifications.",
                             "http://www.shockya.com/news/wp-content/uploads/spider-man-homecoming-iron-man-movie-poster.jpg",
                             "https://youtu.be/q4GdJVvdxss")
print(spiderman.storyline)
spiderman.show_trailer()

thor = media.Movie("Thor",
                          "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization." ,
                          "http://images6.fanpop.com/image/photos/40300000/Thor-Ragnarok-Poster-thor-ragnarok-40345677-691-1024.jpg",
                          "https://youtu.be/v7MGUNV8MxU")
print(thor.storyline)
thor.show_trailer()

movies = [avengers, antman, spiderman, thor]
fresh_tomatoes.open_movies_page(movies)
