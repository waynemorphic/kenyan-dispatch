import unittest
from articles import Article

class test_source(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news aricle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test or case
        '''

        self.new_article = Article("Simon Hill","Favorite learning language","Learning a new tongue? Its a worthy pursuit, and these WIRED-tested services can help.", "https://www.wired.com/gallery/best-language-learning-apps/","https://media.wired.com/photos/62474a8a73b639a714b7f2b1/191:100/w_2580,c_limit/Babbel-App-Featured-Gear.jpg", "2021-12-17T20:00:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

    def test_init(self):
        '''
        case checks proper object initialization
        '''

        self.assertEqual(self.new_article.author,"Simon Hill" )
        self.assertEqual(self.new_article.title, "Favorite learning language")
        self.assertEqual(self.new_article.description,"Learning a new tongue? Its a worthy pursuit, and these WIRED-tested services can help." )
        self.assertEqual(self.new_article.url, "https://www.wired.com/gallery/best-language-learning-apps/")
        self.assertEqual(self.new_article.urlToImage, "https://media.wired.com/photos/62474a8a73b639a714b7f2b1/191:100/w_2580,c_limit/Babbel-App-Featured-Gear.jpg")
        self.assertEqual(self.new_article.publishedAt, "2021-12-17T20:00:00Z")
         
if __name__ == '__main__':
    unittest.main()