from model import Artist, Artwork
from peewee import fn

def delete_all_artwork():
    """ Deletes all artwork from database """
    Artwork.delete().execute()

def delete_artwork(art):
    """ removes art from catalog, error if art doesnt exist """
    try:
        rows_deleted = Artwork.delete().where(Artwork.art_name == art).execute()
    except:
        print('cannot delete artwork that does not exist')

def artist_art_search(term):
    query = Artwork.select().where( ( fn.LOWER(Artwork.artist).contains(term.lower() ) ) )
    return list(query)


def get_art_by_id(art_id):
    """ Searches list for Artwork with given ID,
    :param id the ID to search for
    :returns the artwork, if found, or None if artwork not found.
    """
    return Artwork.get_or_none(Artwork.id == art_id)

def get_available_art_by_artist(artist):
    """ Get a list of art by artist that matches search term and art is aviailable
    :param term(the user input)
    :returns list of art by artist that is available 
    """
    available_art = Artwork.select().where( (Artwork.art_available == True) & (Artwork.artist == artist))
    return available_art


    




