from peewee import *
from catalog import *


def get_new_artwork():

    artpiece_name = input('What is the name of the artpiece?: ')
    price = int(input('What is the price of the airpiece?: '))
    is_available = input('Is this artpeice available?: ')

    if is_available == 'y' or 'Y':
        available = True
    elif is_available == 'n' or 'N':
        available = False
    else: 
        print('INVALID ENTRY: Please enter either "y" for is available and "n" for is not available')

    new_artwork = Artwork(name = artpiece_name, price = price, available = available)
    new_artwork.save()

    return new_artwork


def get_new_artist():

    artist_name = input('What is the name of the artist?: ')
    email = input('What is the price of the airpiece?: ')


    new_artist = Artist(name = artist_name, email = email)
    new_artist.save()

    return new_artist
