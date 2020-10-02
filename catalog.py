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

def modify_availibility(artwork):

    if availibility == True:
        availibility == False
    else: availibility == True

    Artwork.update(available=availibility).where(Artwork.name == artwork).execute()






