from peewee import *
import sqlite3


db = SqliteDatabase('catalog.sqlite')

class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        databse = db

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



artist_1 = Artist(name = 'Susie', email = 'susie@info.com')
artist_1.save()
artwork_1 = Artwork(name ='boo', price = 10, available = True, artist = artist_1)
artwork_1.save()

print(artist_1)
print(artwork_1)

def get_all_artwork():

    artwork_list = []

    for artwork in Artwork.select():
        artwork_list.append(artwork)

    return artwork_list



