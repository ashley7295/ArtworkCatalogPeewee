from peewee import *
from catalog import Artist, Artwork

#this module is used to get input from user.
#these functions are then used in conjuntion with catalog.py and then called in main.py

#get new artist input from user
def get_new_artist():

    artist_name = input('What is the name of the artist?: ')
    email = input('What is artists email address?: ')

    new_artist = Artist(name = artist_name, email = email)
    new_artist.save()

    return new_artist

#get new artwork input from user
def get_new_artwork(self):

    artpiece_name = input('What is the name of the artpiece?: ')
    price = int(input('What is the price of the artpiece?: '))
    is_available = input('Is this artpeice available?: ')
    artist = input('Who created this artpiece?: ')

    if is_available == 'y' or 'Y':
        available = True
    elif is_available == 'n' or 'N':
        available = False
    else: 
        print('INVALID ENTRY: Please enter either "y" for is available and "n" for is not available')

    new_artwork = Artwork(name = artpiece_name, price = price, available = available, artist = artist)
    new_artwork.save()

    return new_artwork

#get all artwork in the artwork table
def get_all_artwork(self):

    art = Artwork.select()

    if art:
        for a in art:
            print('\n', a, '\n')
    else:
        print('there is no artwork in the catalog')

#get all artists in the artists table
def get_all_artists(self):

    artists = Artist.select()

    if artists:
        for artist in artists:
            print ('\n', artist, '\n')
    else:
        print('There are no artists in the catalog')

#get name of artwork to delete
def delete_artwork(self):

    artwork_to_delete = input('Please enter the name of the artpiece you would like to have deleted: ')
        
    return artwork_to_delete

#get name of artwork to update
def update_availability(self):
    artwork_to_update = input('Please enter the name of the artpice you would like to change the avaiability status for: ')

    return artwork_to_update

#get name of artist to search
def get_artist():
    artist_to_search = input('Please enter the name of the artist you would like to search for: ')

    return artist_to_search

#used to display the "quit" message
def message(msg):
    print(msg)

#used to display and get input from the user regarding the menu
def menu_selection():

    print(' 1: Display all Art')
    print(' 2: Display all Artists')
    print(' 3: Add new Artist')
    print(' 4: Add new Artwork')
    print(' 5: Search all Artwork by one Artist')
    print(' 6: Delete Artwork')
    print(' 7: Modify Artwork Availablity')
    print(' 8: Quit')

    user_selection = int(input('Please enter Menu Selection: '))

    if user_selection in range (1,9):
        return user_selection
    else: 
        print('Please enter the number of the menu selection option between 1 and 8')