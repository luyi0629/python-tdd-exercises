
def reverse_list(l):
    """
    Reverses order of elements in list l.
    """
    reverse = l[::-1]
    # or l.reverse()
    return reverse

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5,4,3,2,1]


# ------------------------------------------------------------------------------

def reverse_string(s):
    """
    Reverses order of characters in string s.
    """
    reverse = s[::-1]
    return reverse


def test_reverse_string():
    assert reverse_string("foobar") == "raboof"


# ------------------------------------------------------------------------------

def is_english_vowel(c):
    """
    Returns True if c is an english vowel
    and False otherwise.
    """
    vowels=['a','e','i','o','u','A','E','I','O','U']
    if c in vowels:
       out=True
    else:
       out=False
    return out


def test_is_english_vowel():
    assert is_english_vowel('a')
    assert is_english_vowel('e')
    assert is_english_vowel('i')
    assert is_english_vowel('o')
    assert is_english_vowel('u')
    assert not is_english_vowel('y')
    assert is_english_vowel('A')
    assert is_english_vowel('E')
    assert is_english_vowel('I')
    assert is_english_vowel('O')
    assert is_english_vowel('U')
    assert not is_english_vowel('Y')
    assert not is_english_vowel('k')
    assert not is_english_vowel('z')
    assert not is_english_vowel('?')


# ------------------------------------------------------------------------------

def count_num_vowels(s):
    """
    Returns the number of vowels in a string s.
    """
    # use previous function is_english_vowel()
    l = []
    for c in s:
        if is_english_vowel(c): 
            l.append(True)
    totnum = l.count(True) # or totnum = sum(l)
    return totnum


def test_count_num_vowels():
    sentence = "hey ho let's go"
    assert count_num_vowels(sentence) == 4
    sentence = "HEY ho let's GO"
    assert count_num_vowels(sentence) == 4
    paragraph = """She told me her name was Billie Jean,
                   as she caused a scene
                   Then every head turned with eyes
                   that dreamed of being the one
                   Who will dance on the floor in the round"""
    assert count_num_vowels(paragraph) == 52


# ------------------------------------------------------------------------------

def histogram(l):
    """
    Converts a list of integers into a simple string histogram.
    """
    out = []  # initialise!
    for i in l:
       out.append('#'*i)
    return "\n".join(out)  # turn the list into string with format!


def test_histogram():
    assert histogram([2, 5, 1]) == '##\n#####\n#'


# ------------------------------------------------------------------------------

def get_word_lengths(s):
    """
    Returns a list of integers representing
    the word lengths in string s.
    """
    out = []
    for i in s.split():  # s.split(): splits the string into list
        out.append(len(i))
    return out


def test_get_word_lengths():
    text = "Three tomatoes are walking down the street"
    assert get_word_lengths(text) == [5, 8, 3, 7, 4, 3, 6]


# ------------------------------------------------------------------------------

def find_longest_word(s):
    """
    Returns the longest word in string s.
    In case there are several, return the first.
    """
    # use previous function get_word_lengths()
    w_length = get_word_lengths(s)
    lengthmax = sorted(w_length)[-1]  # sorted(): returns a new sorted list while leaving the source unaltered
    for i in s.split():
        if len(i) == lengthmax:  # if the length of current element  equals to the max length, 
           firstmax = i
           break      # add 'break' to ensure the first one!
    return firstmax


def test_find_longest_word():
    text = "Three tomatoes are walking down the street"
    assert find_longest_word(text) == "tomatoes"
    text = "foo foo1 foo2 foo3"
    assert find_longest_word(text) == "foo1"


# ------------------------------------------------------------------------------

def validate_dna(s):
    """
    Return True if the DNA string only contains characters
    a, c, t, or g (lower or uppercase). False otherwise.
    """
    # define the dna seq first
    dna = 'atcgATCG'    
    # idea: for each character in the string - test whether the character is dna - append the initialised list with T/F - after reading all characters, if sum(list) equals the length of string, then T, else F.
    l = []
    for c in s:
        if c in dna:
          l.append(True)
        else:
          l.append(False)
    if sum(l) == len(s):
        out=True
    else:
        out=False
    return out


def test_validate_dna():
    assert validate_dna('CCGGAAGAGCTTACTTAGccggaagagcttacttag')
    assert not validate_dna('xCCGGAAGAGCTTACTTAGccggaagagcttacttag')


# ------------------------------------------------------------------------------

def base_pair(c):
    """
    Return the corresponding character (lowercase)
    of the base pair. If the base is not recognized,
    return 'unknown'.
    """
    # make a dictionary
    map = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'t','T':'a', 'C':'g','G':'c'}
    for k in map:
       if k == c:
          out = map[k] # note here out is not a list, so the value is replaced at each iteration. to ensure no replacement after a key is matched, add the next line to break the loop. 
          break
       else: 
          out='unknown'  # loop until the last one, and if no match, the last value will be 'unknown'.
    return out


def test_base_pair():
    assert base_pair('a') == 't'
    assert base_pair('t') == 'a'
    assert base_pair('c') == 'g'
    assert base_pair('g') == 'c'
    assert base_pair('A') == 't'
    assert base_pair('T') == 'a'
    assert base_pair('C') == 'g'
    assert base_pair('G') == 'c'
    assert base_pair('x') == 'unknown'
    assert base_pair('foo') == 'unknown'


# ------------------------------------------------------------------------------

def transcribe_dna_to_rna(s):
    """
    Return string s with each letter T replaced by U.
    Result is always uppercase.
    """
    map = {'t':'U', 'T':'U'}
    out = []
    for c in s: 
        if c in ['t', 'T']:
            out.append(map[c])
        else:
            out.append(c.upper())  # list.upper() returns the uppercase
    return "".join(out)   # again, turn the list into string with format


def test_transcribe_dna_to_rna():
    dna = 'CCGGAAGAGCTTACTTAGccggaagagcttacttag'
    assert transcribe_dna_to_rna(dna) == 'CCGGAAGAGCUUACUUAGCCGGAAGAGCUUACUUAG'


# ------------------------------------------------------------------------------

def get_complement(s):
    """
    Return the DNA complement in uppercase
    (A -> T, T-> A, C -> G, G-> C).
    """
    # use previous function base_pair()
    out = []
    for c in s:
        out.append(base_pair(c).upper())
    return "".join(out) # again, turn the list into string with format
# or in one line, use map function, apply the function to each element in the function.
#     return ''.join(map(base_pair(s))).upper()

def test_get_complement():
    assert get_complement('CCGGAAGAGCTTACTTAG') == 'GGCCTTCTCGAATGAATC'
    assert get_complement('ccggaagagcttacttag') == 'GGCCTTCTCGAATGAATC'


# ------------------------------------------------------------------------------

def get_reverse_complement(s):
    """
    Return the reverse complement of string s
    (complement reversed in order).
    """
    # use two functions defined earlier: get_complement() and reverse_string()
    string = "".join(get_complement(s))
    r_string = reverse_string(string)
    return r_string


def test_get_reverse_complement():
    assert get_reverse_complement('CCGGAAGAGCTTACTTAG') == 'CTAAGTAAGCTCTTCCGG'
    assert get_reverse_complement('ccggaagagcttacttag') == 'CTAAGTAAGCTCTTCCGG'


# ------------------------------------------------------------------------------

def remove_substring(substring, string):
    """
    Returns string with all occurrences of substring removed.
    """
    out = string.replace(substring, "") # note the replace() method!
    return out


def test_remove_substring():
    assert remove_substring('GAA', 'CCGGAAGAGCTTACTTAG') == 'CCGGAGCTTACTTAG'
    assert remove_substring('CCG', 'CCGGAAGAGCTTACTTAG') == 'GAAGAGCTTACTTAG'
    assert remove_substring('TAG', 'CCGGAAGAGCTTACTTAG') == 'CCGGAAGAGCTTACT'
    assert remove_substring('GAA', 'GAAGAAGAA') == ''


# ------------------------------------------------------------------------------

def get_position_indices(triplet, dna):
    """
    Returns list of position indices for a specific triplet (3-mer)
    in a DNA sequence. We start counting from 0
    and jump by 3 characters from one position to the next.
    """
    # first split the seq by triplets
    # use range(start, stop, step) to jump 
    out = []
    out_index = []
    for i in range(0, len(dna), 3):
        out.append(dna[i:i+3])
    for j in range(0,len(out)):
        if out[j] == triplet:
            out_index.append(j)
    return out_index
#    l = []
#    for i in range(len(dna)//3):  # // gives integer 
#       if triplet == i   ....

def test_get_position_indices():
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAG') == [1]
    assert get_position_indices('GAA', 'CCGGAAGAGCTTACTTAGGAAGAA') == [1, 6, 7]


# ------------------------------------------------------------------------------

def get_3mer_usage_chart(s):
    """
    This routine implements a 'sliding window'
    and extracts all possible consecutive 3-mers.
    It counts how often they appear and returns
    a list of tuples with (name, occurrence).
    The list is alphabetically sorted by the name
    of the 3-mer.
    """
    # compared to the above, here no need to define the step because moving the character one by one. but note the stop should be len(s)-2, otherwise the last two elements in the list would have < 3-mers. 
    mylist = []
    mylist2 = []
    for i in range(0, len(s)-2):
        mylist.append(s[i:i+3])
    # use list(set()) to get the unique elements only:
    uniqlist = list(set(mylist))
    for j in sorted(uniqlist):
        c = mylist.count(j)        
        mylist2.append((j,c))
    return mylist2
#  can use dictionary instead! in the end, convert the dictionary to list using items() method.
#  use += 1 to add to the counter! 
# d = {}
# for i in range(len(s)-2):
#   kmer = s[i:i+3]
#   if kmer in d: 
#      d[kmer] += 1 
#   else: 
#      d[kmer] = 1 
# l = list(d.iterms())
# l.sort()
# return l


def test_get_3mer_usage_chart():
    s = 'CCGGAAGAGCTTACTTAGGAAGAA'
    result = []
    result.append(('AAG', 2))
    result.append(('ACT', 1))
    result.append(('AGA', 2))
    result.append(('AGC', 1))
    result.append(('AGG', 1))
    result.append(('CCG', 1))
    result.append(('CGG', 1))
    result.append(('CTT', 2))
    result.append(('GAA', 3))
    result.append(('GAG', 1))
    result.append(('GCT', 1))
    result.append(('GGA', 2))
    result.append(('TAC', 1))
    result.append(('TAG', 1))
    result.append(('TTA', 2))
    assert get_3mer_usage_chart(s) == result


# ------------------------------------------------------------------------------

def read_column(file_name, column_number):
    """
    Reads column column_number from file file_name
    and returns the values as floats in a list.
    """
    out = []
    with open(file_name, 'r') as f: # r is read, w is write 
       for line in f:
          parts = line.split() # this will also create a first empty line!
          if len(parts) > 0: 
             out.append(float(parts[column_number-1])) # add float 
    return out


def test_read_column():

    import tempfile
    import os

    text = """
1   0.1  0.001
2   0.2  0.002
3   0.3  0.003
4   0.4  0.004
5   0.5  0.005
6   0.6  0.006"""
# this way the first line is empty.
# if text = """1 0.1 .... , then it will not be a problem.

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:  # open it and write in text
        f.write(text)

    # and now we pass the file name to the function which will read the column
    assert read_column(file_name, 2) == [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def character_statistics(file_name):
    """
    Reads text from file file_name, then
    lowercases the text, and then returns
    a tuple (x, y), where x is the most abundant
    and y is the least abundant character found.
    Use the isalpha() method to figure out
    whether the character is in the alphabet.
    """
    d = {}  
    with open(file_name, 'r') as f:
      for c in f.read().lower():
         if c.isalpha():
            if c in d: # d is adding up! not just empty dictionary
                d[c] += 1
            else: 
                d[c] = 1
    l = list(d.items())
    # then sort on the value, not the key!
    l = sorted(l, key=lambda x: x[1], reverse = True) 
    most = l[0][0]
    least = l[-1][0]    
    return (most, least)


def test_character_statistics():

    import tempfile
    import os

    text = """
To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd."""

    # we save this text to a temporary file
    file_name = tempfile.mkstemp()[1]
    with open(file_name, 'w') as f:
        f.write(text)

    # and now we pass the file name to the function which will get the stats
    (most_abundant, least_abundant) = character_statistics(file_name)
    assert (most_abundant, least_abundant) == ('e', 'q')  # here q and z are least abundant.

    # we remove the temporary file
    os.unlink(file_name)


# ------------------------------------------------------------------------------

def pythagorean_triples(n):
    """
    Returns list of all unique pythagorean triples
    (a, b, c) where a < b < c <= n.
    """
    l = []
    # loop over all a < b < c <= n
    for c in range(1, n + 1):
        for b in range(1, c):
            for a in range(1, b):
                if a*a + b*b == c*c:
                    l.append((a, b, c))
    return l


# ------------------------------------------------------------------------------

def test_pythagorean_triples():
    assert pythagorean_triples(12) == [(3,4,5), (6,8,10)]
#    pass  # so far we do not test anything, check also test coverage

# in an interactive python session, can import this script.
# import exercises 
# then, just write the function name to run the funciton:
# e.g. excercises.pythagorean_triples(200)
