import requests

API_KEY = "api"
BASE_URL = "https://api.themoviedb.org/3"

def search_movie(movie_name):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_name
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data["results"]:
        print("Movie not found")
        return

    movie = data["results"][0]

    print("\n🎬 Movie Information")
    print("-------------------")
    print("Title        :", movie.get("title"))
    print("Release Date :", movie.get("release_date"))
    print("Rating       :", movie.get("vote_average"))
    print("Overview     :", movie.get("overview"))

if __name__ == "__main__":
    movie_name = input("Enter movie name: ")
    search_movie(movie_name)
