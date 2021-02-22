from peewee import *
from config import db_path

db = SqliteDatabase(db_path)

class Artist(Model):
    artist_name = CharField()
    artist_email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.artist_name}, {self.artist_email}'


class Artwork(Model):
    artist = ForeignKeyField(Artist, to_field='artist_name')
    art_name = CharField()
    art_price = IntegerField()
    art_available = BooleanField(default=True)

    class Meta:
        database = db

    def __str__(self):
        available_status = 'available' if self.art_available==True else 'sold'
        return f'{self.id}: {self.art_name}, {self.art_price} {self.artist} This art is {available_status}'

db.connect()
db.create_tables([Artist])
db.create_tables([Artwork])