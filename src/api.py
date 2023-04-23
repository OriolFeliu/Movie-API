import requests


# get data from The Movie Database (TMDb)
api_key = "5c9a2e64ad96d74cdffaf19a4fd60277"
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
                f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
            )

            response = requests.get(search_url)
            response.raise_for_status()

            json_data = response.json()
            title = json_data.get("title")
            print(f"Movie title: {title}")

        else:  # search by movie title
            search_query = input("Enter a movie title: ")
            search_url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={search_query}"

            response = requests.get(search_url)
            response.raise_for_status()

            json_data = response.json()
            title = json_data.get("results")[0].get("original_title")
            print(f"Movie title: {title}")

        exit = input("Do you want to exit? Yes (1) / No (0): ")
        exit = bool(int(exit))

    except Exception as e:
        print(f"An error occurred: {e}")
