mport unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    '''Your unittests here'''

    def test_get_filter_empty_filter(self):
        """ Test get_filter_result when filter_dict is empty (no filter
        specification."""

        twitter_dict = {'SteveCase': {'name': 'Steve Case',
                                      'location': 'Washington DC',
                                      'web': 'http://www.revolution.com',
                                      'bio': 'Co-founder of AOL; now Chairman of Case Foundation and Revolution (Zipcar, LivingSocial, Exclusive Resorts, Everyday Health, Revolution Money, Miraval, etc)',
                                      'following': ['garrytan', 'rabois']}
                        'garrytan':  {'name': 'Garry Tan',
                                      'location': 'San Francisco, CA',
                                      'web': 'http://garry.posterous.com',
                                      'following': ['SteveCase']}
                        'rabois':    {'name': 'Rabo',
                                      'location': 'SF, CA',
                                      'web': '',
                                      'following': []}}

        spec_list = ['garrytan', 'rabois']
        filt_dict = {}
        actual = tf.get_filter_results(twitter_dict,
                                            spec_list,
                                            filt_dict)
        expected = ['garrytan','rabois']
        self.assertEqual(actual, expected)




    def test_get_filter_few_filters(self):
        """ Test get_filter_results with few filters in filter dict to confirm
        that filters are additive."""


        twitter_dict = {'SteveCase': {'name': 'Steve Case',
                                      'location': 'Washington DC',
                                      'web': 'http://www.revolution.com',
                                      'bio': 'Co-founder of AOL; now Chairman of Case Foundation and Revolution (Zipcar, LivingSocial, Exclusive Resorts, Everyday Health, Revolution Money, Miraval, etc)',
                                      'following': ['garrytan', 'rabois']}
                        'garrytan':  {'name': 'Garry Tan',
                                      'location': 'San Francisco, CA',
                                      'web': 'http://garry.posterous.com',
                                      'following': ['SteveCase']}
                        'rabois':    {'name': 'Rabo',
                                      'location': 'SF, CA',
                                      'web': '',
                                      'following': []}}
        spec_list = ['garrytan', 'rabois']
        filt_dict = {'following': 'SteveCase', 'location-includes': 'SF, CA'}
        actual = tf.get_filter_results(twitter_dict,
                                            spec_list,
                                            filt_dict)
        expected = ['rabois']
        self.assertEqual(actual, expected)


    def test_get_filter_дуееук_sensitivity(self):
        """ Test case sensitivity for 'name-includes' and 'location-includes'
        filters. Result does not depend on letter cases."""

        twitter_dict = {'SteveCase': {'name': 'Steve Case',
                                      'location': 'Washington DC',
                                      'web': 'http://www.revolution.com',
                                      'bio': 'Co-founder of AOL; now Chairman of Case Foundation and Revolution (Zipcar, LivingSocial, Exclusive Resorts, Everyday Health, Revolution Money, Miraval, etc)',
                                      'following': ['garrytan', 'rabois']}
                        'garrytan':  {'name': 'Garry Tan',
                                      'location': 'San Francisco, CA',
                                      'web': 'http://garry.posterous.com',
                                      'following': ['SteveCase']}
                        'rabois':    {'name': 'Rabo',
                                      'location': 'SF, CA',
                                      'web': '',
                                      'following': []}}
        spec_list = ['SteveCase', 'garrytan', 'rabois']
        filt_dict = {'name-includes': 'r'}
        actual = tf.get_filter_results(twitter_dict,
                                                spec_list,
                                                filt_dict)
        expected = ['garrytan', 'rabois']
        self.assertEqual(actual, expected)



    def test_get_filter_no_users_(self):
        """ Test get_filter_results if spec_list is empty (i.e no user
        presented after get_search_result)."""

        twitter_dict = {'SteveCase': {'name': 'Steve Case',
                                      'location': 'Washington DC',
                                      'web': 'http://www.revolution.com',
                                      'bio': 'Co-founder of AOL; now Chairman of Case Foundation and Revolution (Zipcar, LivingSocial, Exclusive Resorts, Everyday Health, Revolution Money, Miraval, etc)',
                                      'following': ['garrytan', 'rabois']}
                        'garrytan':  {'name': 'Garry Tan',
                                      'location': 'San Francisco, CA',
                                      'web': 'http://garry.posterous.com',
                                      'following': ['SteveCase']}
                        'rabois':    {'name': 'Rabo',
                                      'location': 'SF, CA',
                                      'web': '',
                                      'following': []}}
        spec_list = []
        filt_dict = {'following': 'garrytan','location-includes': 'SF, CA'}
        actual = tf.get_filter_results(twitter_dict,
                                                spec_list,
                                                filt_dict)
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
