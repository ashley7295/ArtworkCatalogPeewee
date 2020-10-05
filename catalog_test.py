import unittest
from unittest import TestCase
from peewee import *

import catalog
from catalog import Artist, Artwork
import ui


tables = [Artist, Artwork]

test_db = SqliteDatabase('test_cataog.sqlite')

class TestCatalog(TestCase):

    def setUp(self):
        test_db.bind(tables, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(tables)
    
    def tearDown(self):
        test_db.drop_tables(tables)
        test_db.close()

    def clear_catalog(self):
        catalog.delete_catalog()

    def setUpCase(self):
        self.clear_catalog()

    def add_test_data(self):
        self.clear_catalog()

        self.art1 = Artwork(name='Art1', price=10, available=True, artist='Tommy')
        self.art2 = Artwork(name='Art2', price=10, available=True, artist='Sarah')
        
        self.artist1 = Artist(name='Tommy', email='Tom@tom.com')
        self.artist2 = Artist(name='Sarah', email='Sarah@sarah.com')

        self.art1.save()
        self.art2.save()
        self.artist1.save()
        self.artist2.save()

    def test_add_artwork(self):
        self.add_test_data()
        artwork_count = catalog.artwork_count()
        art = Artwork(name='art',price=10,available=True,artist='ashley')
        art.save()
        self.assertEqual(artwork_count + 1, catalog.artwork_count())

    def test_add_artist(self):
        self.add_test_data()
        artist_count = catalog.artist_count()
        artist = Artist(name='ashley', email='ashley@ashley.com')
        artist.save()
        self.assertEqual(artist_count + 1, catalog.artist_count())    

    def test_get_artwork_by_name(self):
        self.add_test_data()
        r = catalog.get_art_by_name(self.art1.name)
        self.assertEqual(r, self.art1)

    

if __name__ == '__main__':
    unittest.main()



    

    



    
