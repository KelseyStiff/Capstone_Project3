from peewee import *
db = SqliteDatabase('art.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.email}'


class Artwork(Model):
    #how to create artist as field in artwork?
    art_name = CharField()
    price = IntegerField()
    available = BooleanField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.art_name}, {self.price}, {self.available}'

db.connect()
db.create_table([Artist])
db.create_table([Artwork])

def add_artist():
    artist_data = Artist(name = artist_name, artist_email)
    artist_data.save()

def add_art():
    pass
    #make sure all art is associated with artist
    #create artist first if needed

def search_art():
    pass
    #by artist

def delete_art():
    #pass

def display_available_art():
    pass
    #by artist

def change_availability():
    pass
    #change from available to sold













def display_data():
    jugglers = Juggler.select()
    print('\n')
    for juggler in jugglers:
        print(juggler)
    print('\n')

def delete_data(delete_juggler_name):
    Juggler.delete().where(Juggler.name == delete_juggler_name).execute()

main():



if __name__ == '__main__':
    main()

