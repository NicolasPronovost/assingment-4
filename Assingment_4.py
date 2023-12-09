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

    def load_song(self):

    def save_songs(self):

    def add_song(self, title, artist):

    def search_song(self, query ):

    def edit_song(self, old_title, new_title, new_artist):

    def delete_song(self, title):


# This will be the user interface
def main():
    Music_library = MusicLibrary