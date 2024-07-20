import os
import json
import random


PLAYLIST_FOLDER="Playlists"
PLAYLISTS_DIR=os.path.abspath(PLAYLIST_FOLDER)

playlists=[]


def get_random(value):
    random_index= random.randint(0,value-1)
    return random_index

def get_playlist():
    with os.scandir(PLAYLISTS_DIR) as PLAYLISTS:
        for PLAYLIST in PLAYLISTS:
            if PLAYLIST.is_file() and PLAYLIST.name.endswith(".json"):
                playlists.append(PLAYLIST.name)

    return playlists

PLAYLISTS=get_playlist()


def choose_playlist(value):
    song=value
    for PLAYLIST in PLAYLISTS:
        playlist_dir=os.path.join(PLAYLISTS_DIR,PLAYLIST)
        try:
            with open(playlist_dir,'r') as f:
                data=json.load(f)
                for content in data:
                    if song in content["song"].lower() or song in content["artist"].lower():
                        return PLAYLIST
        except FileNotFoundError:
            print(f"{PLAYLIST} file not found")
            return None
        except json.JSONDecodeError:
            print(f"Error loading {PLAYLIST}. File is not valid JSON")
            return None

    print("Sorry! We couldn't find any playlist with that song or artist. Please try again.\n")
    return None
    

def get_recommendations(found_playlist):
    songs=[]
    artists=[]
    if not found_playlist:
        return
    print("\nThe recommendations: ")
    playlist_dir=os.path.join(PLAYLISTS_DIR,found_playlist)
    with open(playlist_dir, 'r') as f:
        data=json.load(f)
        for content in data:
            songs.append(content["song"])
            artists.append(content["artist"])

        length=len(songs)
        for i in range(1,4):
            song_idx=get_random(length)
            print(f"{i}. {songs[song_idx]} by {artists[song_idx]}")
            
def main():
    while True:
        user_input=input("Enter the song or artist's name, enter 'q' to quit: ").lower()
        if user_input == 'q':
            print("\n Thank you for using our system. EXiting..!\n")
            break
        found_playlist=choose_playlist(user_input)
        get_recommendations(found_playlist)

main()

