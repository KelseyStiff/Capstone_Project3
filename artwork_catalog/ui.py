from model import Artwork, Artist



def get_artist_info():
    """ Create a new Artist from name and email provided by user
     :returns: a Artist created from the name and email. """
    artist_name = input('Enter Artist name: ')
    artist_email = input('Enter Arist email: ')
    return Artist(artist_email=artist_email, artist_name=artist_name)

def get_artwork_info():
    """ Create a new Artwork from artist,name,price, availability provided by user
     :returns: a Artwork created from the info. """
    
    art_name = input('Enter name of artwork: ')
    artist = input('Enter artist of artwork: ')
    art_price = input('Enter price of artwork: ')
    return Artwork(artist=artist, art_name=art_name, art_price=art_price)

def show_artwork(artists_arts):
    if artists_arts:
        for art in artists_arts:
            print(art)
    else:
        print('No art to display')
    
def get_art_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter Artwork ID: '))
            if id > 0:
                return id
            else:
                print('Please enter a positive number.')

        except ValueError:
            print('Please enter a number.')

def get_availability():
    """ Ask user to enter 'Available' or 'Sold'
     :returns: True if user enters 'available' or False if user enters 'sold' """
    while True:
        response = input('Enter \'Available\' if art is available or \'sold\' if art is not available: ')
        if response.lower() in ['sold', 'available']:
            return response.lower() == 'available'
        else:
            print('Type \'available\' or \'sold\'')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)

def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)