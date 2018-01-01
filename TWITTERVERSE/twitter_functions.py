"""
Type descriptions of Twitterverse and Query dictionaries
(for use in docstrings)

Twitterverse dictionary:  dict of {str: dict of {str: object}}
    - each key is a username (a str)
    - each value is a dict of {str: object} with items as follows:
        - key "name", value represents a user's name (a str)
        - key "location", value represents a user's location (a str)
        - key "web", value represents a user's website (a str)
        - key "bio", value represents a user's bio (a str)
        - key "following", value represents all the usernames of users this 
          user is following (a list of str)
       
Query dictionary: dict of {str: dict of {str: object}}
   - key "search", value represents a search specification dictionary
   - key "filter", value represents a filter specification dictionary
   - key "present", value represents a presentation specification dictionary

Search specification dictionary: dict of {str: object}
   - key "username", value represents the username to begin search at (a str)
   - key "operations", value represents the operations to perform (a list of str)

Filter specification dictionary: dict of {str: str}
   - key "following" might exist, value represents a username (a str)
   - key "follower" might exist, value represents a username (a str)
   - key "name-includes" might exist, value represents a str to match (a case-insensitive match)
   - key "location-includes" might exist, value represents a str to match (a case-insensitive match)

Presentation specification dictionary: dict of {str: str}
   - key "sort-by", value represents how to sort results (a str)
   - key "format", value represents how to format results (a str)
       
"""




def process_data(data_file):
    """ (file open for reading) -> Twitterverse dictironary
        
    Read the data_file and return it's data in Twitterverse dictionary format.
        
    """    
    
    #create main dictionary where all data will be placed, as keys we use 
    #usernames
    twitterverse_dict = {}
    
    
    check = ''
    #check variable will check if we reach the last username. If so than we 
    #collected all data.
    
    while check != 'END':    
        
        username = data_file.readline().strip()
        name = data_file.readline().strip()
        location = data_file.readline().strip()
        site = data_file.readline().strip()
        
        #create key in main twitterverse_dict using username
        twitterverse_dict[username] = {}
        
        #add username information in dictionary of username
        twitterverse_dict[username]['name'] = name
        twitterverse_dict[username]['location'] = location
        twitterverse_dict[username]['web'] = site
        
        #add biography of username
        bio = ''
        line = data_file.readline()
        if line != 'ENDBIO\n':
            while line != 'ENDBIO\n':
                bio = bio + line
                line = data_file.readline()
            bio = bio.rstrip()    
        twitterverse_dict[username]['bio'] = bio
        
        #add all users username is following
        following = []
        follow = data_file.readline()
        if follow != 'END\n' and follow != 'END':
            while follow != 'END\n':
                following.append(follow.strip())
                follow = data_file.readline()  
                if follow == 'END':
                    check = 'END'
                    follow = 'END\n'
        else:
            if follow == 'END':
                check = 'END'
        twitterverse_dict[username]['following'] = following
        
                    
    return twitterverse_dict
    
    

def process_query(query_file):
    """ (file open for reading) -> query dictionary
        
    Read the query_file and return the query in the query dictionary format.
        
    """
    
    #create main query_dictionary where all data from query files will be placed
    query_dict = {}
    query_file.readline()
    
    
    #add SEARCH specification to query_dict
    query_dict['search'] = {}
    operations = []
    
    username = query_file.readline().strip()
    operation = query_file.readline()
    
    if operation != 'FILTER\n':
        while operation != 'FILTER\n':
            operations.append(operation.strip())
            operation = query_file.readline()
        query_dict['search']['username'] = username
        query_dict['search']['operations'] = operations
    else:
        query_dict['search']['username'] = username
        query_dict['search']['operations'] = operations
    
    
    #add FILTER specification to query_dict
    query_filter = query_file.readline()
    query_dict['filter'] = {}
    if query_filter != 'PRESENT\n':
        while query_filter != 'PRESENT\n':
            filter_list = query_filter.split()
            query_dict['filter'][filter_list[0]] = filter_list[1]
            query_filter = query_file.readline()
    
    #add PRESENT specification to query_dict       
    sort_list = query_file.readline().split()
    query_dict['present'] = {}
    query_dict['present'][sort_list[0]] = sort_list[1]  
    format_list = query_file.readline().split()
    query_dict['present'][format_list[0]] = format_list[1]
    
    return query_dict


twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', \
                                   'location': '', 'web': '', \
                                   'following': ['c','b']}, \
                             'b': {'bio': '', 'name': 'Baba Rahman', \
                                   'location': '', 'web': '', \
                                   'following': ['c']}, \
                             'c': {'bio': '', 'name': 'Carles Puyol', \
                                   'location': '', 'web': '', \
                                   'following': []}}
def all_followers(twitterverse_dict, username):
    """ (Twitterverse dictionary, str) -> list of str
    
    Return list of  all the usernames that are following the user specified by
    the second parameter (username).
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '',
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> all_followers(twitterverse_dict, 'c')
    ['a', 'b']
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> all_followers(twitterverse_dict, 'b')
    ['a']
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> all_followers(twitterverse_dict, 'a')
    []
    
    """
    
    followers = []        
    for key in twitterverse_dict:
        if username in twitterverse_dict[key]['following']:
            followers.append(key)
    return followers




def get_search_results(twitterverse_dict, spec_dict):
    """(Twitterverse dictionary, search specification dictionary) -> list of str
    
    Perform the specified search according to specification_dict on the given 
    twitterverse_dict, and return a list of strings representing usernames that 
    match the search criteria.
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> specification_dict = {'username': 'c', 
                              'operations' : 
                              ['followers','following','following']}
    >>> get_search_results(twitterverse_dict, spec_dict)
    ['c']
    
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> specification_dict = {'username': 'a', 'operations' : []}
    ['a']
    
    """
    
    processed_list = []
    spec_list = []
    spec_list.append(spec_dict['username'])
    operations = spec_dict['operations']
    
    i = 0 
    #perform all operation in specification_dict
    while i < len(operations):
        if operations[i] == 'following':
            processed_list = []
            for user in spec_list:
                processed_list.extend(twitterverse_dict[user]['following'])
        elif operations[i] == 'followers':
            processed_list = []
            for user in spec_list:
                processed_list.extend(all_followers(twitterverse_dict, user))
                
        #create new list with and get rid of duplicates        
        spec_list = []
        spec_list.extend(list(set(processed_list)))
        i = i + 1
        
        
    return spec_list



twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial', 
                                   'location': 'z', 'web': '', 
                                   'following': []}}  
spec_list = ['a']
filt_dict = {'following': 'c','follower': 'c'}

def get_filter_results(twitterverse_dict, spec_list, filt_dict):
    """ (Twitterverse dictionary, list of str, 
        filter specification dictionary) -> list of str
    
    Apply the specified filters from filt_dict to the given spec_list to 
    determine which usernames to keep, and return the resulting list of 
    usernames.
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> spec_list = ['a', 'b']
    >>> filt_dict = {'following': 'b'}
    ['a']
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> spec_list = ['a', 'b']
    >>> filt_dict = {'following': 'c', 'location-includes': 'z'}
    ['a']
    
    """
    
    filter_list = []
    filter_list.extend(spec_list)
    
    
    for key in filt_dict:
        # apply filter 'name-includes'
        if key == 'name-includes':
            for user in spec_list:
                if twitterverse_dict[user]['name'].upper() == '':
                    if user in filter_list:
                        filter_list.remove(user)                    
                elif filt_dict[key].upper() not in twitterverse_dict[user]['name'].upper():
                    print(filt_dict[key])
                    if user in filter_list:
                        filter_list.remove(user)
        
        # apply filter 'location-includes'
        elif key == 'location-includes' :
            for user in spec_list:
                if twitterverse_dict[user]['location'].upper() == '':
                    if user in filter_list:
                        filter_list.remove(user)                      
                elif filt_dict[key].upper() not in twitterverse_dict[user]['location'].upper():
                    if user in filter_list:
                        filter_list.remove(user)
        
        # apply filter 'follower'
        elif key == 'follower':
            for user in spec_list:
                if user not in twitterverse_dict[filt_dict[key]]['following']:
                    if user in filter_list:
                        filter_list.remove(user) 
                        
        # apply filter 'following'
        elif key == 'following':
            for user in spec_list:
                if filt_dict[key] not in twitterverse_dict[user]['following']:
                    if user in filter_list:
                        filter_list.remove(user)                    
        
    return filter_list



def get_present_string(twitterverse_dict, filter_list, present_dict):
    """ (Twitterverse dictionary, list of str,
        presentation specification dictionary) -> str
    
    Format the filter_list for presentation based on the given present_dict,
    and return the formatted string. 
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> filter_list = ['b', 'a']
    >>> present_dict = {'sort-by': 'name', 'format': 'long'}
    >>> get_present_string(twitterverse_dict, filter_list, present_dict)
    "----------\na\nname: Anthony Martial\nlocation: \nweb: \nbio: \nfollowing :['c', 'b']\n----------\nb\nname: Baba Rahman\nlocation: \nweb: \nbio: \nfollowing :['c']\n----------" 
    
    >>> twitterverse_dict = {'a': {'bio': '', 'name': 'Anthony Martial',
                                   'location': '', 'web': '', 
                                   'following': ['c','b']},
                             'b': {'bio': '', 'name': 'Baba Rahman',
                                   'location': '', 'web': '', 
                                   'following': ['c']},
                             'c': {'bio': '', 'name': 'Carles Puyol',
                                   'location': '', 'web': '', 
                                   'following': []}}
    >>> filter_list = []
    >>> present_dict = {'sort-by': 'name', 'format': 'long'}
    >>> get_present_string(twitterverse_dict, filter_list, present_dict)
    '----------\n----------'
    
    """
    
    sort_list = []
    format_list = []
    for key in present_dict:
        if key == 'sort-by':
            sort_list.append(present_dict[key])
        elif key == 'format':
            format_list.append(present_dict[key])
    i = 0
    if len(filter_list) > 1:        
        if sort_list[0] == 'username':
            tweet_sort(twitterverse_dict, filter_list, username_first)
        if sort_list[0] == 'name':
            tweet_sort(twitterverse_dict, filter_list, name_first)
        if sort_list[0] == 'popularity':
            tweet_sort(twitterverse_dict, filter_list, more_popular)
            
   
    if format_list[0] == 'short':
        return str(filter_list)
    
    return_list = ''
    if len(filter_list) > 0:
        if format_list[0] == 'long':
            i = 0
            while i < len(filter_list):
                return_list = return_list + '----------\n' + filter_list[i] + '\n' + 'name: ' + twitterverse_dict[filter_list[i]]['name'] + '\n' + 'location: ' +\
                    twitterverse_dict[filter_list[i]]['location'] + '\n' + 'website: ' + twitterverse_dict[filter_list[i]]['web'] + '\n' + 'bio:'+'\n' +\
                    twitterverse_dict[filter_list[i]]['bio'] + '\n' + 'following: ' + str(twitterverse_dict[filter_list[i]]['following']) + '\n' 
                i = i + 1
            return_list.rstrip()
            return_list = return_list + '----------\n' 
    else:
        return_list = '----------\n----------'
    
    return return_list


     
# --- Sorting Helper Functions ---
def tweet_sort(twitter_data, results, cmp):
    """ (Twitterverse dictionary, list of str, function) -> NoneType
    
    Sort the results list using the comparison function cmp and the data in 
    twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> result_list = ['c', 'a', 'b']
    >>> tweet_sort(twitter_data, result_list, username_first)
    >>> result_list
    ['a', 'b', 'c']
    >>> tweet_sort(twitter_data, result_list, name_first)
    >>> result_list
    ['b', 'a', 'c']
    """
    
    # Insertion sort
    for i in range(1, len(results)):
        current = results[i]
        position = i
        while position > 0 and cmp(twitter_data, results[position - 1], current) > 0:
            results[position] = results[position - 1]
            position = position - 1 
        results[position] = current  
            
def more_popular(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return -1 if user a has more followers than user b, 1 if fewer followers, 
    and the result of sorting by username if they have the same, based on the 
    data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> more_popular(twitter_data, 'a', 'b')
    1
    >>> more_popular(twitter_data, 'a', 'c')
    -1
    """
    
    a_popularity = len(all_followers(twitter_data, a)) 
    b_popularity = len(all_followers(twitter_data, b))
    if a_popularity > b_popularity:
        return -1
    if a_popularity < b_popularity:
        return 1
    return username_first(twitter_data, a, b)
    
def username_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
    
    Return 1 if user a has a username that comes after user b's username 
    alphabetically, -1 if user a's username comes before user b's username, 
    and 0 if a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':['b']}, \
    'b':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> username_first(twitter_data, 'c', 'b')
    1
    >>> username_first(twitter_data, 'a', 'b')
    -1
    """
    
    if a < b:
        return -1
    if a > b:
        return 1
    return 0

def name_first(twitter_data, a, b):
    """ (Twitterverse dictionary, str, str) -> int
        
    Return 1 if user a's name comes after user b's name alphabetically, 
    -1 if user a's name comes before user b's name, and the ordering of their
    usernames if there is a tie, based on the data in twitter_data.
    
    >>> twitter_data = {\
    'a':{'name':'Zed', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'b':{'name':'Lee', 'location':'', 'web':'', 'bio':'', 'following':[]}, \
    'c':{'name':'anna', 'location':'', 'web':'', 'bio':'', 'following':[]}}
    >>> name_first(twitter_data, 'c', 'b')
    1
    >>> name_first(twitter_data, 'b', 'a')
    -1
    """
    
    a_name = twitter_data[a]["name"]
    b_name = twitter_data[b]["name"]
    if a_name < b_name:
        return -1
    if a_name > b_name:
        return 1
    return username_first(twitter_data, a, b)