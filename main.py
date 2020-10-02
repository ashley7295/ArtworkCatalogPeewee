from peewee import *
import ui
from catalog import Artist, Artwork



#add a new artist
#add new artwork
#get all artwork
#search for all art by a certain artist
#delete artwork
#modify availability on artwork
#Quit Menu

def preform_menu_selection ():

    user_selection = ui.menu_selection()

    if user_selection == 1:
        #display all art
        ui.get_all_artwork()
    elif user_selection == 2:
        #add new artist
        ui.get_new_artist()
    elif user_selection == 3:
        #add new artwork
        ui.get_new_artwork()
    elif user_selection == 4:
        print('under construction')
        #search for all artwork by artist
    elif user_selection == 5:
        print('under construction')
        #delete artwork
    elif user_selection == 6:
        print('under construction')
        #modify artwork availability
    elif user_selection == 7:
        #quit program
        quit_program()

def quit_program():
    ui.message('Bye!!')


preform_menu_selection()