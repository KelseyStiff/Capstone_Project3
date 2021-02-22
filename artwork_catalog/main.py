import peewee
from model import Artwork, Artist
import db
import ui

def main():

    print_menu()
    user_input = 0
    while user_input != 7:
        user_input = int(input('Enter Choice: '))
        
        if user_input == 1:
            add_artist()

        elif user_input == 2:
            add_artwork()

        elif user_input == 3:
            show_all_art_by_artist()

        elif user_input == 4:
            show_available_art_by_artist()

        elif user_input == 5:
            delete_artwork()
        elif user_input == 6:
            change_availability()

        elif user_input == 7:
            break
        print_menu()
        
def print_menu():
    print (30 * "-" , "Artwork Catalog" , 30 * "-")
    print('1. Add Artist')
    print ('2. Add Artwork')
    print ('3. Display all Artists works')
    print('4. Display Available Artists works')
    print ('5. Delete Artwork')
    print ('6. Change Art availability')
    print('7. EXIT')
    print (77 * "-")

def add_artist():
    new_artist = ui.get_artist_info()
    try:
        new_artist.save()
    except peewee.IntegrityError:
        ui.message('Error, artist already exists in the database')

def add_artwork():
    new_artwork = ui.get_artwork_info()
    try:
        new_artwork.save()
    except peewee.IntegrityError:
        ui.message('Error, artwork already exists in the database')


def show_all_art_by_artist():
    search_term = ui.ask_question('Enter name of Artist to view their works: ')
    matches = db.artist_art_search(search_term)
    ui.show_artwork(matches)

def show_available_art_by_artist():
    search_term = ui.ask_question('Enter name of Artist to view their available works: ')
    matches = db.artist_art_search(search_term)
    available_art = db.get_available_art_by_artist(matches)
    ui.show_artwork(available_art)

def delete_artwork():
    art_to_delete = ui.ask_question('Enter name of Artwork to delete: ')
    db.delete_artwork(art_to_delete)

def change_availability():
    art_id = ui.get_art_id()
    artwork = db.get_art_by_id(art_id)
    if not artwork:
        ui.message('Artwork not found')
        return
    new_status = ui.get_availability()     
    artwork.art_available = new_status
    artwork.save()
    

if __name__ == '__main__':
    main()
