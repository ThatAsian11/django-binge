import os
import json
import requests

url = "https://api.themoviedb.org"
api = os.getenv("API")

# Fetches the required data from the api when the path url is provided and returns it as JSON
def get_items(path):
    try:
        location = url + path
        r = requests.get(location)
        items = r.json()
        # print(items)
        return items

    except:
        print(path)
        print("Error: Items not found")
        return None

# Formats the query string 
def format_query(query: str) -> str:
    query = query.strip()
    query = [i.replace(' ', '+') for i in query]
    result = ''.join(query)
    return result

# Define all functions needed to fetch Movie/TV Show data
class Search:
    """Search for a show or movie by a keyword"""
    def movie_search(q):
        a = format_query(q)
        url = f"/3/search/movie?page=1&query={a}&language=en-US&api_key={api}"
        data = get_items(url)
        return data

    def tv_search(q):
        a = format_query(q)
        url = f"/3/search/tv?page=1&query={a}&language=en-US&api_key={api}"
        data = get_items(url)
        return data

    def all_search(q):
        a = format_query(q)
        url = f"/3/search/multi?api_key={api}&query={a}"
        data = get_items(url)
        return data

    def movie_find(id):
        url = f"/3/movie/{id}?api_key={api}"
        data = get_items(url)
        return data

    def tv_find(id):
        url = f"/3/tv/{id}?api_key={api}"
        data = get_items(url)
        return data

class Trending:
    """Get trending shows or movies"""
    class Daily:
        def movie_trend():
            url = f"/3/trending/movie/day?api_key={api}"
            data = get_items(url)
            return data

        def tv_trend():
            url = f"/3/trending/tv/day?api_key={api}"
            data = get_items(url)
            return data

    class Weekly:
        def movie_trend():
            url = f"/3/trending/movie/week?api_key={api}"
            data = get_items(url)
            return data

        def tv_trend():
            url = f"/3/trending/tv/week?api_key={api}"
            data = get_items(url)
            return data
