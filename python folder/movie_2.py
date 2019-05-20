import fresh_tomatoes
import webbrowser
class Movie():
    movies=0
    def __init__(self,movie_Trailer,title,cover,storyline):
        self.trailer_youtube_url=movie_Trailer
        self.title=title
        self.poster_image_url=cover
        self.storyline=storyline

        Movie.movies+=1

    @property
    def title(self):
        return "MOVIE: " + self.title
    @title.setter
    def title(self,title):
        self.title = title

    @staticmethod
    def separate(string):
        movie,title,cover,story=string.split("-")
        return Movie(movie,title,cover,story)

    def printe(self):
        return self.trailer_youtube_url + self.title + self.poster_image_url + self.storyline

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

toy_Sory=Movie("https://www.youtube.com/watch?v=KYz2wyBy3kc", "toy story", "https://vignette.wikia.nocookie.net/cartoons/images/a/a7/Capture_13D.PNG/revision/latest?cb=20160327004931", "toys coming alive")



print(toy_Sory.printe())

avatar=Movie("https://www.youtube.com/watch?v=6ziBFh3V1aM", "avatar", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj917-Xiq3gAhWOzaQKHeLpAFAQjRx6BAgBEAQ&url=http%3A%2F%2Fwww.impawards.com%2F2009%2Favatar.html&psig=AOvVaw2mfJHEUVt02oRRVjBumA8x&ust=1549747692489572", "i didnt watch the movie so dont know")

print(avatar.printe())

hunger_games=Movie("https://www.youtube.com/watch?v=mfmrPu43DF8", "hunger games", "https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw%40%40._V1_.jpg&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1392170%2F&docid=Q3IUjvu7u1sWHM&tbnid=gBsxzljSGi_yKM%3A&vet=10ahUKEwiHzo2kiq3gAhWLlIsKHa3LAcgQMwhKKAAwAA..i&w=1382&h=2048&client=safari&bih=660&biw=1252&q=hunger%20games%201%20poster&ved=0ahUKEwiHzo2kiq3gAhWLlIsKHa3LAcgQMwhKKAAwAA&iact=mrc&uact=8", "may the odds be ever in your fauvor")

print(hunger_games.printe())

list=[toy_Sory,avatar,hunger_games]

print(Movie.movies)

fresh_tomatoes.open_movies_page(list)



print(toy_Sory.title)
