playlist = {
    "Album1": {"artist": "Bastille", "genre": "Alternative", "release_year": 2013},
    "Album2": {"artist": "The Prodigy", "genre": "Dance", "release_year": 2004},
    "Album3": {"artist": "Lamb", "genre": "Electronic", "release_year": 2003},
    "Album4": {"artist": "Faithless", "genre": "Electronic/Dance", "release_year": 2004},
    "Album5": {"artist": "Adrian Lux", "genre": "House", "release_year": 2010},
    "Album6": {"artist": "Gregory Porter", "genre": "Jazz", "release_year": 2020},
    "Album7": {"artist": "Paolo Nutini", "genre": "Pop", "release_year": 2014},
    "Album8": {"artist": "Duran Duran", "genre": "Rock", "release_year": 1981},
    "Album9": {"artist": "Curtis Mayfield", "genre": "R&B", "release_year": 1999},
    "Album10": {"artist": "Bob Marley", "genre": "Reggae", "release_year": 1978},
    "Album11": {"artist": "Bob Dylan", "genre": "Rock", "release_year": 1966},
    "Album12": {"artist": "Pink Floyd", "genre": "Rock", "release_year": 1971},
    "Album13": {"artist": "Miles Davis", "genre": "Jazz", "release_year": 1957},
    "Album14": {"artist": "Nina Simone", "genre": "Jazz", "release_year": 1965},
}

# Function to add an album to the playlist
def add_album(title, artist, genre, release_year):
    playlist[title] = {"artist": artist, "Genre": genre, "Release_year": release_year}

# Function to view the playlist
def view_playlist():
    for title, details in playlist.items():
        print(f"Album: {title}, Artist: {details['artist']}, Genre: {details['genre']}, Release Year: {details['release_year']}")

# Function to update album information
def update_album(title, new_artist=None, new_genre=None, new_release_year=None):
    if title in playlist:
        if new_artist:
            playlist[title]["artist"] = new_artist
        if new_genre:
            playlist[title]["genre"] = new_genre
        if new_release_year:
            playlist[title]["release_year"] = new_release_year
    else:
        print(f"Album with title '{title}' not found in the playlist.")

# Function to delete an album from the playlist
def delete_album(title):
    if title in playlist:
        del playlist[title]
    else:
        print(f"Album with title '{title}' not found in the playlist.")

# Testing the functions
add_album("Album15", "New Artist", "New Genre", 2021)
view_playlist()

update_album("Album1", new_artist="Updated Artist")
view_playlist()

delete_album("Album2")
view_playlist()  
