from peewee import *
from catalog import Artist, Artwork



def get_new_artist():

    artist_name = input('What is the name of the artist?: ')
    email = input('What is artists email address?: ')


    new_artist = Artist(name = artist_name, email = email)
    new_artist.save()
    return new_artist



def get_new_artwork():

    artpiece_name = input('What is the name of the artpiece?: ')
    price = int(input('What is the price of the airpiece?: '))
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


def get_all_artwork():

    art = Artwork.select()

    if art:
        for a in art:
            print('\n', a, '\n')
    else:
        print('there is no artwork in the catalog')

def delete_artwork():

    artwork_to_delete = input('Please enter the name of the artpiece you would like to have deleted: ')
    
    return artwork_to_delete

def update_availability():
    artwork_to_update = input('Please enter the name of the artpice you would like to change the avaiability status for: ')

    return artwork_to_update

def message(msg):
    print(msg)

def menu_selection():

    print(' 1: Display all Art')
    print(' 2: Add new Artist')
    print(' 3: Add new Artwork')
    print(' 4: Search all Artwork by one Artist')
    print(' 5: Delete Artwork')
    print(' 6: Modify Artwork Availablity')
    print(' 7: Quit')

    user_selection = int(input('Please enter Menu Selection: '))

    return user_selection