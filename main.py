from peewee import *
import ui
import catalog



def preform_menu_selection ():

    menu = True

    while menu:
        user_selection = ui.menu_selection()

        if user_selection == 1:  #display all art
            ui.get_all_artwork()
        elif user_selection == 2: #display all artists
            ui.get_all_artists()
        elif user_selection == 3: #add new artist
            ui.get_new_artist()
        elif user_selection == 4: #add new artwork
            ui.get_new_artwork()
        elif user_selection == 5: #search for all artwork by artist
            artists_artwork()
        elif user_selection == 6: #delete artwork
            delete_art()
        elif user_selection == 7: #modify artwork availability
            update_availibility()
        elif user_selection == 8: #quit program
            quit_program()
            menu = False

def quit_program():
    ui.message('Bye!!')

def artists_artwork():

    artist = ui.get_artist()
    art = catalog.artwork_by_artist(artist)

    if art:
        for a in art:
            print(a)
    else:
        print('This artist does not have any artwork')

def delete_art():
    art = ui.delete_artwork()
    catalog.delete_artwork(art)

def update_availibility():
    art = ui.update_availability()
    catalog.modify_availibility(art)
    

preform_menu_selection()