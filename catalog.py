from peewee import *
import sqlite3


db = SqliteDatabase('catalog.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}, {self.name}, {self.email}'

class Artwork(Model):
    name = CharField()
    price = IntegerField()
    available = BooleanField()
    artist = ForeignKeyField(Artist, backref= 'artwork')

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.available}'

db.connect()
db.create_tables([Artist, Artwork])

def delete_artwork(artwork):
    Artwork.delete().where(Artwork.name == artwork).execute()
    print('Your artwork has been deleted. ')

def artwork_by_artist(artist_name):

    rows_modified = Artwork.select().where(Artwork.artist == artist_name)

    return rows_modified
     
def modify_availibility(artwork):

    query = Artwork.select().where(Artwork.name == artwork)

    for art in query:
        if art.available == True:
            Artwork.update(available = False).where(Artwork.name == artwork).execute()
            print('this artwork is no longer available')
        elif art.available == False:
            Artwork.update(available = True).where(Artwork.name == artwork).execute()
            print('This artwork has become available again')
        else:
            print('Error')

    