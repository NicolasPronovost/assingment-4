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
        self.songs = self.load_song()

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

#Gives the user the ability to edit a song in there library
    def edit_song(self, old_title, new_title, new_artist):
        for song in self.songs:
            if song ['title'] == old_title:
                song['title'] = new_title
                song['artist'] = new_artist
                self.save_songs()
                return
#exception handling
        print (f"Song {old_title} was not found in your music library")           

#Gives the user the ability to delet a song 
    def delete_song(self, title):
        for song in self.save_songs:
            if song['title'] == title:
                self.songs.remove(song)
                self.save_songs()
                return
        print(f"Song {title} not found in library")
            
# This will be the user interface
def main():
    Music_library = MusicLibrary()

    while True:
        print("\n\nMusic library menu:")
        print("1. Add song")
        print("2. Search song")
        print("3. Edit song")
        print("4. Delete song")
        print("5. Show library")
        print("6. Quit")

        user_input = input("Enter disiered function (1-6): ")

        if user_input == '1':
            title = input("Enter the title of the song: ")
            artist = input("Enter artist name or band name: ")
            Music_library.add_song(title, artist)
        
        elif user_input == '2':
            query = input("Enter a key word to search for a song: ")
            matching_songs = Music_library.search_song(query)
            if matching_songs:
                print("There is a matching song: ")
                for song in matching_songs:
                    print (f"{song ['title']} by {song['artist']}")
            else:
                print("No matching song found")
    
        elif user_input == '3':
            old_title = input("Enter the title of the song you would like to edit: ")
            new_title = input("Enter the new title name: ")
            new_artist = input("Enter the new name of the artist: ")
            Music_library.edit_song(old_title, new_title, new_artist)

        elif user_input == '4':
            title = input("Enter song title you would like to delet: ")
            Music_library.delete_song(title)

        elif user_input == '5':
            print("This is your current music library:")
            for song in Music_library.songs:
                print(f"{song['title']} by {song['artist']}")

        elif user_input == '6':
            print ("You are not exiting your music library. Goodbey :)")
            break
        else:
            print("Pleas enter a vlide menu option")
        
if __name__ == "__main__":
    main()     
