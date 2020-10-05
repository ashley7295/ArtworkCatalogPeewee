from peewee import *

#setting up the database variable
db = SqliteDatabase('catalog.sqlite')

#class AKA table for the Artists
class Artist(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}, {self.name}, {self.email}'

#class AKA table for the Artwork
class Artwork(Model):
    name = CharField(unique=True)
    price = IntegerField()
    available = BooleanField(default=True,)
    artist = ForeignKeyField(Artist, backref= 'artwork')

    class Meta:
        database = db
    
    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.available}'

#connecting to the database and creating the tables

db.connect()
db.create_tables([Artist, Artwork])

def delete_catalog():
    Artwork.delete().execute()
    Artist.delete().execute()
    

def artwork_count():
    count = Artwork.select()

    return count

def artist_count():
    count = Artist.select()

    return count

    #peewee queries for deleting artwork by the name of the artwork
def delete_artwork(artwork):
    Artwork.delete().where(Artwork.name == artwork).execute()
    print('Your artwork has been deleted. ')

    #peewee querie to search for artwork by an artist
def artwork_by_artist(artist_name):

    rows_modified = Artwork.select().where(Artwork.artist == artist_name)

    return rows_modified
            
        #peewee queries  to search for artwork and modify availibiliy to opposite of what it is currently 
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

def get_art_by_name(art_name):
    return Artwork.select().where(Artwork.name == art_name).execute()
    



    

        

    