# def make_album(artist, title):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     return album_dict
#
# album = make_album('metallica', 'ride the lightning')
# print(album)
#
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)



# def make_album(artist, title, win=''):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     if win:
#         album_dict['win'] = win
#     return album_dict
#
# album = make_album('metallica', 'ride the lightning')
# print(album)
#
# album = make_album('beethoven', 'ninth symphony')
# print(album)
#
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)
#
# album = make_album('iron maiden', 'piece of mind', 'GM')
# print(album)


def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)
