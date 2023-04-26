import requests


# get data from The Movie Database (TMDb)
API_KEY = ""
exit = False

while not exit:
    try:
        search_method = input(
            "Do you want to search using movie ID (1) or movie title (0): "
        )
        search_method = bool(int(search_method))

        if search_method:  # search by movie ID
            movie_id = input("Enter movie id: ")
            search_url = (
                f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
            )

        else:  # search by movie title
            search_query = input("Enter a movie title: ")
            search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={search_query}"

        response = requests.get(search_url)
        response.raise_for_status()
        json_data = response.json()
        # get only the first result of list of possible movies
        result = json_data if search_method else json_data.get("results")[0]

        title = result.get("original_title")
        release_date = result.get("release_date")
        rating = result.get("vote_average")
        overview = result.get("overview")
        print(f"Movie title: {title}")
        print(f"Release date: {release_date}")
        print(f"Rating: {rating}")
        print(f"Overview: {overview}")

        exit = input("Do you want to exit? Yes (1) / No (0): ")
        exit = bool(int(exit))

    except Exception as e:
        print(f"An error occurred: {e}")

"""
Add a loop to allow the user to search for multiple movies without having to restart the program every time.

Include additional information in the output, such as the release date, the rating, or the plot summary.

Add a function to handle the API request and response, so that you can reuse the code elsewhere in your program.

Use a configuration file to store the API key and other settings, so that you don't have to hard-code them in the code.

Add more error handling, such as handling connection errors or timeouts, and provide informative error messages to the user.

Implement a caching system to store the results of previous searches, so that you can reduce the number of API requests and speed up the program.
"""
