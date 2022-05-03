import unittest
from source import Source

class test_source(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test or case
        '''

        self.new_source = Source("wired", "Wired","https://www.aftenposten.no","en", "the best news source")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
        case checks proper object initialization
        '''

        self.assertEqual(self.new_source.id,"wired" )
        self.assertEqual(self.new_source.name, "Wired")
        self.assertEqual(self.new_source.url, "https://www.aftenposten.no")
        self.assertEqual(self.new_source.language, "en")
        self.assertEqual(self.new_source.description, "the best news source")
        
         
if __name__ == '__main__':
    unittest.main()