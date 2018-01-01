import unittest
import twitterverse_functions


class TestGetFilterResults(unittest.TestCase):
    
    def test_get_filter_empty_filter_dict(self):
        """ Test get_filter_result when filter_dict is empty (no filter 
        specification."""
        
        twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                           'location': '', 'web': '', 
                                           'following': ['c','b']}, 
                                     'b': {'bio': '', 'name': 'Baba Rahman', 
                                           'location': '', 'web': '', 
                                           'following': ['c']}, 
                                     'c': {'bio': '', 'name': 'Carles Puyol', 
                                           'location': '', 'web': '', 
                                           'following': []}}   
        spec_list = ['a', 'b']
        filt_dict = {}
        actual = twitterverse_functions.get_filter_results(twitterverse_dict,
                                                           spec_list,
                                                           filt_dict)
        expected = ['a','b']
        self.assertEqual(actual, expected)
        
        
    def test_get_filter_additive_filters(self):
        """ Test get_filter_results with few filters in filter dict to confirm
        that filters are additive."""
        
        
        twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                   'location': 'z', 'web': '', 
                                   'following': ['c','b']}, 
                             'b': {'bio': '', 'name': 'Baba Rahman', 
                                   'location': '', 'web': '', 
                                   'following': ['c']}, 
                             'c': {'bio': '', 'name': 'Carles Puyol', 
                                   'location': '', 'web': '', 
                                   'following': []}} 
        spec_list = ['a', 'b']
        filt_dict = {'following': 'c', 'location-includes': 'z'}
        actual = twitterverse_functions.get_filter_results(twitterverse_dict,
                                                                   spec_list,
                                                                   filt_dict)
        expected = ['a']
        self.assertEqual(actual, expected)        
        
        
    def test_get_filter_case_sensitivity(self):
        """ Test case sensitivity for 'name-includes' and 'location-includes' 
        filters. Result does not depend on letter cases."""
        
        twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                   'location': 'Alaporta', 'web': '', 
                                   'following': ['c','b']}, 
                             'b': {'bio': '', 'name': 'Baba Rahman', 
                                   'location': 'Lviv', 'web': '', 
                                   'following': []}, 
                             'c': {'bio': '', 'name': 'Carles Puyol', 
                                   'location': 'LA', 'web': '', 
                                   'following': []}}
        spec_list = ['a', 'b', 'c']
        filt_dict = {'name-includes': 'an', 'location-includes': 'LA'}
        actual = twitterverse_functions.get_filter_results(twitterverse_dict,
                                                           spec_list,
                                                           filt_dict)
        expected = ['a']
        self.assertEqual(actual, expected)
    
    def test_get_filter_no_users_before(self):
        """ Test get_filter_results if spec_list is empty (i.e no user 
        presented after get_search_result)."""
        
        twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                           'location': 'Alaporta', 'web': '', 
                                           'following': ['c','b']}, 
                                     'b': {'bio': '', 'name': 'Baba Rahman', 
                                           'location': 'Lviv', 'web': '', 
                                           'following': ['c']}, 
                                     'c': {'bio': '', 'name': 'Carles Puyol', 
                                           'location': 'LA', 'web': '', 
                                           'following': []}}  
        spec_list = []
        filt_dict = {'following': 'c','location-includes': 'Lviv'}
        actual = twitterverse_functions.get_filter_results(twitterverse_dict,
                                                                   spec_list,
                                                                   filt_dict)
        expected = []
        self.assertEqual(actual, expected)
        
    def test_get_filter_no_users_after(self):
        """ Test get_filter_results when there are no users left after applying
        all filters."""
        
        twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                   'location': 'z', 'web': '', 
                                   'following': ['c','b']}, 
                             'b': {'bio': '', 'name': 'Baba Rahman', 
                                   'location': 'j', 'web': '', 
                                   'following': ['c']}, 
                             'c': {'bio': '', 'name': 'Carles Puyol', 
                                   'location': '', 'web': '', 
                                   'following': []}}  
        spec_list = ['a','b','c']
        filt_dict = {'following': 'c','location-includes': 'j','follower': 'c'}
        actual = twitterverse_functions.get_filter_results(twitterverse_dict,
                                                                   spec_list,
                                                                   filt_dict) 
        expected = []
        self.assertEqual(actual, expected)        
        
        
unittest.main(exit=False)