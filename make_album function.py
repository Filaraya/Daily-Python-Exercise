#write a function that builds a dictionary describing album
def make_album(artist_name,album_title,number_track = 0):
    """dictionary artist name and album title"""

    albums = {
        'Artist':artist_name,
        'Title':album_title,
        }
    if number_track:
        albums['Tracks'] = number_track
    
    return albums
#call make_album
album = make_album('David','praise',8)
print(album)

while True:
    print("\nPlease, enter album description")
    print("enter 'q' to quit")
    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    title = input("Enter title of the album: ")
    if title == 'q':
        break
    track_no = input("How many tracks have? ")
    if track_no == 'q':
        break
    album = make_album(artist,title,track_no)
    print(album)
print("Thanks for response")