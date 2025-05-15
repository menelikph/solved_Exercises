movies = {}

def add_movie(title):
    if title in movies:
        return False  # ya existe
    movies[title] = []
    return True

def rate_movie(title, rating):
    if title in movies and 1 <= rating <= 5:
        movies[title].append(rating)
        return True
    return False

def average_rating(title):
    if title in movies and movies[title]:
        return sum(movies[title]) / len(movies[title])
    return None
