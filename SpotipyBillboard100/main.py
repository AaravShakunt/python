import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

os.environ["SPOTIPY_CLIENT_ID"] = "e4a32ee12ba94cfeb1f9b208c0dd166a"
os.environ["SPOTIPY_CLIENT_SECRET"] = "c3f5ba069232471b94dfc21429fc58e6"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://example.com"



SPOTIPY_CLIENT_ID = "e4a32ee12ba94cfeb1f9b208c0dd166a"
SPOTIPY_CLIENT_SECRET = "c3f5ba069232471b94dfc21429fc58e6"
 
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
 
response = requests.get(URL)
billboard100_webpage = response.text
soup = BeautifulSoup(billboard100_webpage, "html.parser")
titles_with_html = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")
 
song_titles = [title.text.strip() for title in titles_with_html]

forbidden_list = ["Songwriter(s):", 'Producer(s):', 'Imprint/Promotion Label:']
i=0
song_titles2 = []

for song in song_titles:
    if song not in forbidden_list:
        song_titles2.append(song)
# print(song_titles2)

scope = "user-library-read, playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

user_id = sp.current_user()["id"]
# print(user_id)

spotify_songs = []

for song in song_titles2:
    spotify_songs.append(sp.search(q=song,limit=1)['tracks']['items'][0]["album"]['uri'])
    # print("hello")
print(spotify_songs)



response_playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False, collaborative=False, description='')
# pprint.pprint(response_playlist)
playlist_id = response_playlist["id"]
# print(playlist_id["id"])

for song in spotify_songs:
    sp.playlist_add_items(playlist_id, [song], position=None)