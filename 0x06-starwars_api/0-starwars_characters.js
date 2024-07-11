import requests
import sys

def get_film_characters(movie_id):
    # Base URL for the Star Wars API
    base_url = 'https://swapi.dev/api/films/'

    try:
        # Get the film details using the movie ID
        response = requests.get(f"{base_url}{movie_id}/")
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return
    except Exception as err:
        print(f"An error occurred: {err}")
        return

    film_data = response.json()

    # Get the list of character URLs
    character_urls = film_data.get('characters', [])

    # Print each character name
    for url in character_urls:
        character_response = requests.get(url)
        character_data = character_response.json()
        print(character_data.get('name', 'Unknown'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
    else:
        movie_id = sys.argv[1]
        get_film_characters(movie_id)

