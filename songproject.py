import json
import random;

tracks=["trap","Hiphop","reggae","Mugithi", "RnBs","genge","dancehall","bongo","drill kenya","drill"]
while True:
    songName = input("\n\nEnter the song or artist name(Enter q to quit): ").lower()
    def readfile(file):
        file_path ="Playlists/"+file+".json"
        with open(file_path) as f:
            data = json.load(f) # Load the JSON data from the file into a Python dictionary
            
            total_songs = len(data) # Get the total number of songs in the JSON data
            for song in data:
                found = False

                if song['song'].lower() == songName:
                    found = True
                    print("Below are great alternatives to ", song['song'], ":\n")
                if song['artist'].lower() == songName:
                    found = True
                    print("Recommended alternatives for", song['artist'], "songs:\n")

                if found:
                    print(file ,"alternatives:")
                    for i in range(3):
                        song_number = random.randint(0, total_songs)
                        song = data[song_number]['song'] # Access the 'song' key to get the song name
                        artist = data[song_number]['artist'] # Access the 'artist' key to get the artist name
                        print(str(i+1) + ". " + song + " by " + artist)
                    return True
            else:
                return False
    if songName=="q":
        print("Thank you for using our recommendation system.... ")
        break
            

    checker = False
    for track in tracks:
        if(readfile(track)):
            checker = True
            break

    if checker == False:
        print("Song not found. Can you please check the spelling.")