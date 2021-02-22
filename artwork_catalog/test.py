from unittest import TestCase
import peewee 
import config
config.database_path = 'database/test_art.db'

from model import Artwork, Artist
import db

class TestDatabase(TestCase):
    def setUp(self):
        database_config.database_path = 'database/test_art.db'
        self.clear_database()


    def add_test_art(self):
        self.clear_database()

        self.art1 = Artwork(art_name ='test art1',art_price = 50, artist='test artist1', art_available = True)
        self.art2 = Artwork(art_name ='test art1',art_price = 50, artist='test artist1', art_available = True)
        self.art3 = Artwork(art_name ='test art1',art_price = 50, artist='test artist1', art_available = True)

        self.art1.save()
        self.art2.save()
        self.art3.save()

    def add_test_artists(self):
        self.clear_database()

        self.artist1 = Artwork(artist_name ='test artist1',artist_email = 'test email1')
        self.artist2 = Artwork(artist_name ='test artist2',artist_email = 'test email2')
        self.artist3 = Artwork(artist_name ='test artist3',artist_email = 'test email3')

        self.artist1.save()
        self.artist2.save()
        self.artist3.save()

    def clear_database(self):
        db.delete_all_artwork()

    def test_add_art_duplicate_errors(self):
        art = Artwork(art_name = 'cc')
        art.save()
        with self.assertRaises(peewee.IntegrityError):
            art_dupe = Artwork(title='cc')
            art_dupe.save()