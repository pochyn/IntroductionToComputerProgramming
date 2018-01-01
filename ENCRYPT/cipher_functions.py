# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.

def clean_message(plaintext):
    """ (str) -> str
    
    Precondition: works only with 26 character English alphabet.
    
    Return copy of plaintaxt only with alphabetical characters, where every
    character is converted to uppercase character.
    
    >>> clean_message('I am 1st year student!')
    'IAMSTYEARSTUDENT'
    >>> clean_message('124 + 16 = 140')
    ''
    """
    
    message = ''
    for ch in plaintext:
        if ch.isalpha():
            message = message + ch
    return message.upper()



def encrypt_letter(letter, keystream):
    """ (str, int) -> str
    
    Precondition: works only with 26 character English alphabet. Our program
    uses only uppercase letters. Alphabet is treated as circular.
    
    Return new encrypted letter recieved by adding keystream to value of 
    correspondig original letter.
    
    >>> encrypt_letter('Z', 2)
    'B'
    >>> encrypt_letter('C', 0)
    'C'
    """
    
    letter_value = ord(letter) - ord('A')
    encrypted_value = (letter_value + keystream) % 26
    return chr(encrypted_value + ord('A'))
    


def decrypt_letter(letter, keystream):
    """ (str, int) -> str
    
    Precondition: works only with 26 character English alphabet. Our program
    uses only uppercase letters. Alphabet is treated as circular.
    
    Return the original letter by substracting the keystream from the value of 
    corresponding encrypted letter.
    
    >>> decrypt_letter('A', 17)
    'J'
    >>> decrypt_letter('T', 124)
    'Z'
    """
    
    letter_value = ord(letter) - ord('A')
    decrypted_value = (letter_value - keystream) % 26
    return chr(decrypted_value + ord('A'))    
    


def swap_cards(deck_of_cards,index):
    """ (list of ints, int) -> NoneType
    
    Precondition: treat deck as circular
    
    Swap the card at the index with the card that follows it.
    
    >>> deck_of_cards = [1, 2, 3, 4]
    >>> swap_cards(deck_of_cards, 3)
    >>> deck_of_cards
    [4,2,3,1]
    
    >>> deck_of_cards = [1, 2, 3]
    >>> swap_cards(deck_of_cards, 0)
    >>> deck_of_cards
    [2,1,3]
    """
    
    change_letter = deck_of_cards[index]
    if deck_of_cards[index] == deck_of_cards[-1]:
        deck_of_cards[index] = deck_of_cards[0]
        deck_of_cards[0] = change_letter
    else:
        deck_of_cards[index] = deck_of_cards[index + 1]
        deck_of_cards[index + 1] = change_letter
        
        

def get_big_joker_value(deck_of_cards):
    """ (list of int) -> int
    
    Return the big joker (the highest value card) of deck_of_cards.
    
    >>> get_big_joker_value([4, 6, 5, 2, 1, 3])
    6
    >>> get_big_joker_value([2, 1, 0])
    2
    """
    
    return max(deck_of_cards)



def get_small_joker_value(deck_of_cards):
    """ (list of int) -> int
       
    Return the small joker (the second highest value card) of deck_of_cards.
       
    >>> get_small_joker_value([4, 6, 5, 2, 1, 3])
    5
    >>> get_small_joker_value([2, 1, 0])
    1
    """   
    
    return get_big_joker_value(deck_of_cards) - 1



def get_index(deck_of_cards, value):
    """ (list of int, int) -> int
    
    Return the index of value in deck_of_cards.
    
    >>> get_index([2, 1, 3], 2)
    0
    >>> get_index([2, 1, 3, 5, 4], 4)
    4
    """
    
    index = 0
    while deck_of_cards[index] != value: 
        index = index + 1
    return index    
        
        

def move_small_joker(deck_of_cards):
    """ (list of int) -> NoneType
    
    Precondition: treat deck_of_cards as circular
    
    Swap the small joker (the second highest value) of deck_of_cards with the
    card that follows it. Step 1 of algorithm.
    
    >>> deck_of_cards = [1, 2, 3, 4]
    >>> move_small_joker(deck_of_cards)
    >>> deck_of_cards
    [1,2,4,3]
    
    >>> deck_of_cards = [3, 1, 2]
    >>> move_small_joker(deck_of_cards)
    >>> deck_of_cards
    [2,1,3]
    """
    
    index = get_index(deck_of_cards, get_small_joker_value(deck_of_cards))
    swap_cards(deck_of_cards,index)
    
    

def move_big_joker(deck_of_cards):
    """ (list of int) -> NoneType
    
    Precondition: treat deck_of_cards as circular
    
    Move the big joker (the highest value) of deck_of_cards two cards down the 
    deck. Step 2 of algorithm.
    
    >>> deck_of_cards = [3, 1, 2]
    >>> move_big_joker(deck_of_cards)
    >>> deck_of_cards
    [1, 2, 3]
    
    >>> deck_of_cards = [1, 2, 3, 4]
    >>> move_big_joker(deck_of_cards)
    >>> deck_of_cards
    [2, 4, 3, 1]
    """
    
    i = 0
    while i < 2:
        index = get_index(deck_of_cards, get_big_joker_value(deck_of_cards))
        swap_cards(deck_of_cards,index) 
        i = i + 1



def triple_cut(deck_of_cards):
    """ (list of ints) -> NoneType
    
    Do the triple cut on deck_of_cards: everything above the first joker 
    (either big or small) in deck_of_cards  goes to the bottom of the 
    deck_of_cards, and everything under the second joker in the deck_of_cards
    goes to the top. Step 3 of the algorithm.
    
    >>> deck_of_cards = [3, 1, 2, 7, 11, 5, 6, 8, 10, 12, 9, 4]
    >>> triple_cut(deck_of_cards)
    >>> deck_of_cards
    [9, 4, 11, 5, 6, 8, 10, 12, 3, 1, 2, 7]
    
    >>> deck_of_cards = [11, 1, 2, 7, 3, 5, 6, 8, 10, 4, 9, 12]
    >>> triple_cut(deck_of_cards)
    >>> deck_of_cards
    [11, 1, 2, 7, 3, 5, 6, 8, 10, 4, 9, 12]
    """
    
    big_joker_index = get_index(deck_of_cards,
                                get_big_joker_value(deck_of_cards))
    small_joker_index = get_index(deck_of_cards,
                                get_small_joker_value(deck_of_cards))
    if big_joker_index > small_joker_index:
        bottom_deck = deck_of_cards[big_joker_index + 1:]
        middle_deck = deck_of_cards[small_joker_index:big_joker_index+1]
        top_deck = deck_of_cards[:small_joker_index]
    else:
        bottom_deck = deck_of_cards[small_joker_index + 1:]
        middle_deck = deck_of_cards[big_joker_index:small_joker_index+1]
        top_deck = deck_of_cards[:big_joker_index]    
    deck_of_cards[:] = []
    deck_of_cards.extend(bottom_deck)
    deck_of_cards.extend(middle_deck)
    deck_of_cards.extend(top_deck)    



def insert_top_to_bottom(deck_of_cards):
    """ (list of int) -> NoneType
    
    Precondition: if the bottom card is the big joker, we use the value of the 
    small joker as the number of cards.
    
    Examine the value of the bottom card (last value of deck_of_cards) of the 
    deck_of_cards; move that many cards from the top of the deck to the bottom, 
    inserting them just above the last item in list. Step 4 of algorithm.
    
    >>> deck_of_cards = [3, 1, 2, 7, 11, 5, 6,  8, 10, 12, 9, 4]
    >>> insert_top_to_bottom(deck_of_cards)
    >>> deck_of_cards
    [11, 5, 6, 8, 10, 12, 9, 3, 1, 2, 7, 4]
    
    >>> deck_of_cards = [11, 1, 2, 7, 3, 5, 8, 10, 4, 6, 9, 12]
    >>> insert_top_to_bottom(deck_of_cards)
    >>> deck_of_cards
    [11, 1, 2, 7, 3, 5, 8, 10, 4, 6, 9, 11]
    """
    
    if deck_of_cards[-1] != get_big_joker_value(deck_of_cards):
        number_of_cards = deck_of_cards[-1]
        top_deck = deck_of_cards[:number_of_cards]
        remain_deck = deck_of_cards[number_of_cards:-1]
        deck_of_cards[:] = []
        deck_of_cards.extend(remain_deck)
        deck_of_cards.extend(top_deck)
        deck_of_cards.append(number_of_cards)
    else:
        number_of_cards = get_small_joker_value(deck_of_cards)
        top_deck = deck_of_cards[:number_of_cards]
        last_card = get_big_joker_value(deck_of_cards)
        deck_of_cards[:] = []
        deck_of_cards.extend(top_deck)
        deck_of_cards.append(last_card)
        
        
        
def get_top_card(deck_of_cards):
    """ (list of int) -> int
    
    Return top card of deck_of_cards (i.e the first element of deck_of_cards).
    
    >>> get_top_card([11, 1, 2, 7, 3, 5, 8, 10, 4, 6, 9, 12])
    11
    
    >>> get_top_card([2,1,3])
    2
    """
    
    top_card = deck_of_cards[0]
    if top_card == get_big_joker_value(deck_of_cards):
        top_card = get_small_joker_value(deck_of_cards) 
    return top_card
        


def get_card_at_top_index(deck_of_cards):
    """ (list of int) -> int
    
    Precondition: if the top card is the big joker (highest value card), use the
    value of the small joker(second highest value card) as the index.
    big_joker and small_joker is not valid returned keystreams.
    
    Return the card in the deck at index, using the value of the 
    top card (first item in deck_of_cards) as an index. Step 5 of the algorithm.
    
    >>> get_card_at_top_index([3, 1, 2, 7, 11, 5, 6,  8, 10, 12, 9, 4])
    7
    
    >>> get_card_at_top_index([11, 1, 2, 7, 3, 5, 8, 10, 4, 6, 9, 12])
    3
    """
    
    while deck_of_cards[get_top_card(deck_of_cards)] == \
          get_big_joker_value(deck_of_cards) or \
          deck_of_cards[get_top_card(deck_of_cards)] == \
          get_small_joker_value(deck_of_cards):
        move_small_joker(deck_of_cards)
        move_big_joker(deck_of_cards)
        triple_cut(deck_of_cards)
        insert_top_to_bottom(deck_of_cards)
        get_top_card(deck_of_cards)
    return deck_of_cards[get_top_card(deck_of_cards)]
        
    
    
def get_next_keystream_value(deck_of_cards):
    """ (list of int) -> int
    
    Return the keystream provided by repeating all of 5 steps of the algorithm
    using deck_of_cards
    
    >>> get_next_keystream_value([3, 1, 2, 7, 11, 5, 6,  8, 10, 12, 9, 13, 4])
    2
    
    >>> get_next_keystream_value([13, 1, 11, 2, 7, 3, 5, 8, 10, 4, 6, 9, 12,])
    5
    """
    
    move_small_joker(deck_of_cards)
    move_big_joker(deck_of_cards)
    triple_cut(deck_of_cards)
    insert_top_to_bottom(deck_of_cards)
    return get_card_at_top_index(deck_of_cards) 


def process_messages(deck_of_cards, list_of_messages, encrypt_or_decrypt):
    """ (list of int, list of str, str) -> list of str
    
    Return a list of encrypted or decrypted messages in list_of_messages
    (depending on the third parameter, either ENCRYPT or DECRYPT) using 
    keystreams genereated by applying algorithm on deck_of_cards,in the same 
    order as they appear in the given list of messages
    
    >>> process_messages([1,2,3,4,5], ['a', 'ax'], ENCRYPT)
    ['E', 'EY']
    
    >>> process_messages([1,2,3,4,5], ['KWYBUGKIHJFVNV', ''], DECRYPT)
    ['ITWASDIFFICULT', '']
    """
    
    processed_list = []
    for message in list_of_messages:
        message.strip('\n')
        message = clean_message(message)
        processed_message = ''
        for letter in message:
            if encrypt_or_decrypt == 'e':
                encrypted = encrypt_letter(letter, 
                                        get_next_keystream_value(deck_of_cards))
                processed_message = processed_message + encrypted
            elif encrypt_or_decrypt == 'd':
                decrypted = decrypt_letter(letter,
                                        get_next_keystream_value(deck_of_cards))
                processed_message = processed_message + decrypted
        processed_list.append(processed_message)
    return processed_list


def read_messages(given_file):
    """ (file open for reading) -> list of str
    
    Read and return the contents of the given_file as a list of messages, 
    in the order in which they appear in the file. 
    
    """
    
    list_of_messages = []
    for line in given_file:
        list_of_messages.append(line.strip('\n'))
    return list_of_messages


def is_valid_deck(deck_of_cards):
    """ (list of int) -> bool
    
    Return true iff deck_of_cards is valid (i.e contains every integer from 1 up
    to the number of cards in the deck_of_cards and its length is more than 2)
    
    >>> is_valid_deck([1, 2])
    False
    
    >>> is_valid_deck([8, 7, 1, 5, 2, 9, 6, 4, 3])
    True
    """
    
    if len(deck_of_cards) > 2:
        i = 1
        while i <= max(deck_of_cards):
            if not i in deck_of_cards:
                return False
            i = i + 1
        return True
    else:
        return False

def read_deck(given_file):
    """ (file open for reading) -> list of int
    
    Read and return the numbers that are in the given_file, in the order in 
    which they appear in the file.
    
    """
    
    list_of_lines = []
    list_of_ints = []
    for line in given_file:
        new_line = line.strip('\n')
        new_line = line.split()
        list_of_lines.append(new_line)
    for list in list_of_lines:
        for ch in list:
            list_of_ints.append(int(ch))
    return list_of_ints
