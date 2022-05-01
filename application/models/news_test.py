import unittest
from news import News

class test_news(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test or case
        '''

        self.new_news = News("Igor Bonifacic", "Apple second-generation AirPods are back down to $100", "If you missed the chance to buy Apple second-generation AirPods when they were $100 a few weeks ago, Amazon has once again discounted them to that price. While we think most people are better off purchasing the third-generation AirPods or AirPods Pro due to…", "https://www.engadget.com/amazon-airpods-beats-studio-pro-sale-164248746.html", "https://s.yimg.com/os/creatr-uploaded-images/2020-07/c9ee07d0-c117-11ea-b67f-851aefcf30f2")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        '''
        case checks proper object initialization
        '''

        self.assertEqual(self.new_news.author,"Igor Bonifacic" )
        self.assertEqual(self.new_news.title, "Apple second-generation AirPods are back down to $100")
        self.assertEqual(self.new_news.description, "If you missed the chance to buy Apple second-generation AirPods when they were $100 a few weeks ago, Amazon has once again discounted them to that price. While we think most people are better off purchasing the third-generation AirPods or AirPods Pro due to…")
        self.assertEqual(self.new_news.url, "https://www.engadget.com/amazon-airpods-beats-studio-pro-sale-164248746.html" )
        self.assertEqual(self.new_news.image, "https://s.yimg.com/os/creatr-uploaded-images/2020-07/c9ee07d0-c117-11ea-b67f-851aefcf30f2")
         
if __name__ == '__main__':
    unittest.main()