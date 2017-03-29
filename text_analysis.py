import nltk

## helper function to create a word/count dict from a List of tweets
def wordCount(tweetlist):
    words_dict = {}

    # Remove "common" words
    cw = open('common_words.txt', 'r')
    cw_str = cw.read()
    cw_tokens = nltk.word_tokenize(cw_str)

    for tweet in tweetlist:
        line_words = tweet.split()
        punctuations = '''`!()-[]{};:'"\,<>./?@#$%^&*_~'''

        uncommon_words = [word for word in line_words if word not in cw_tokens]

        ## if we've seen the word before, increment the counter.
        ## else add as a new key in the dict
        for raw_word in line_words:
            ## lower-case each word and strip out punctuation
            cased_word = raw_word.lower()

            # we're dealing with unicode here, so convert as necessary
            word = cased_word.encode('utf-8').translate(None, punctuations)

            if word not in cw_tokens:
                if word in words_dict.keys():
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1

    return words_dict

# Print the raw word list used by this user
def printWords(tweetlist):
    unordered_words = wordCount(tweetlist)

    keylist = unordered_words.keys()
    keylist.sort()
    for key in keylist:
        print "%s: %s" % (key, unordered_words.get(key))

# Print the top 20 words used with their counts
def printTopWords(tweetlist):
    unordered_words = wordCount(tweetlist)
    ordered_values = sorted(unordered_words.values(), reverse=True)

    ## list of the top 20 values in the dict; if there are duplicates,
    ## we would still want to print them
    top_20 = ordered_values[:20]

    for key, value in sorted(unordered_words.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        if value in top_20:
            print key, '-- appears', value, 'times'

# Grab the top 20 words used with their counts, and return them as a dict
def getTopWords(tweetlist):
    unordered_words = wordCount(tweetlist)
    ordered_values = sorted(unordered_words.values(), reverse=True)

    ## list of the top 20 values in the dict; if there are duplicates,
    ## we would still want to print them
    top_20 = ordered_values[:20]
    top_words = {}

    for key, value in sorted(unordered_words.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        if value in top_20:
             top_words["'"+key+"'"] = value

    return top_words


# Parse the tweet text for named entities and returns a List of them
def getNamedEntities(tweetlist):

    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in tweetlist]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    def extract_entity_names(t):
        entity_names = []

        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))

        return entity_names

    entity_names = []
    for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)
        entity_names.extend(extract_entity_names(tree))

    # return unique entity names
    return set(entity_names)

# Function for printing out a nice column-based display of a long list
def fmtcols(mylist, cols):
    maxwidth = max(map(lambda x: len(x), mylist))
    justifyList = map(lambda x: x.ljust(maxwidth), mylist)
    lines = (' '.join(justifyList[i:i+cols])
             for i in xrange(0,len(justifyList),cols))
    print "\n".join(lines)
