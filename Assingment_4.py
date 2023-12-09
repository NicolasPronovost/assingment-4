# creat a music libray whit the abbilty to creat read and update
# creat function
# search function
# edit list function
# delete function 
# keep all the data in a JSON file

import json

class MusicLibrary:
    def __init__ (self, json_file='music_library.json'):
        self.json_file = json_file
        self.songs = self.load_songs()

#load song from json file
    def load_song(self):
        try:
            with open (self.json_file, 'r') as file:
                songs = json.load(file)
#exception handling :)
        except FileNotFoundError:
            return[]

#save songs in json file
    def save_songs(self):
        with open (self.json_file, 'w') as file:
            json.dump(self.songs, file, indent=2)

#add song to json file
    def add_song(self, title, artist):
        song = {'title': title, 'artist': artist}
        self.songs.append(song)
        self.save_songs()
        print (f"Added {title} by {artist} to your music library")

#look in the json file for a song
    def search_song(self, query ):
        matching_song = [song for song in self.songs if query.lower() in song ['title'].lower()]
        return matching_song

    def edit_song(self, old_title, new_title, new_artist):

    def delete_song(self, title):


# This will be the user interface
def main():
    Music_library = MusicLibrary