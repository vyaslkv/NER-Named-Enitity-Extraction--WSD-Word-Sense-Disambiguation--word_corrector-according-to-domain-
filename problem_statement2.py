from pywsd.lesk import simple_lesk
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from pywsd.lesk import cached_signatures
from pywsd import disambiguate
from pywsd.similarity import max_similarity as maxsim
from nltk.corpus import wordnet
# a2=disambiguate('How much deposit i can deposit to my deposit?', algorithm=maxsim, similarity_option='wup', keepLemmas=True)
def lesk_nltk_wsd(context_sentence, ambiguous_word, pos=None, synsets=None):

    context = set(context_sentence)
    # operators = set(('and', 'or', 'not','How','i','can','?','my'))
    # context = context-operators
    if synsets is None:
        synsets = wordnet.synsets(ambiguous_word)

    if pos:
        synsets = [ss for ss in synsets if str(ss.pos()) == pos]

    if not synsets:
        return None
    cosinesimilarity_list=list(((get_cosine_sim(context_sentence,str(ss.definition())),ss)) for ss in synsets)
    sense_list= list(((get_cosine_sim(context_sentence,str(ss.definition())),ss)) for ss in synsets)
    import heapq
    top_3 = heapq.nlargest(5, sense_list)#zip(score, name))
    # print("top 3",top_3)
    top_3_sense_list=[]
    for (i,j) in top_3:
        top_3_sense_list.append(j)
    # _, sense = max((len(context.intersection(ss.definition().split())), ss) for ss in synsets)

    return top_3_sense_list
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import more_itertools
def get_cosine_sim(*strs):
    vectors = [t for t in get_vectors(*strs)]
    # print("vectors",vectors)
    result= cosine_similarity([vectors[0]],[vectors[1]])
    # print("result",result)
    return result
def get_vectors(*strs):
    text = [t for t in strs]
    vectorizer = CountVectorizer(text)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()
print("results of lesk nltk wsd")
sense_nltk = lesk_nltk_wsd('I want to deposit money in my deposit How much deposit i can deposit to my deposit?'.replace('.',','),'deposit')
for sense in sense_nltk:
    print(sense.definition())
"""


BELOW ARE SOME OTHER MEHTODS I TRIED BUT DID'T GIVE PROPER RESULTS





"""
def simple_lesk_algo():
    sent = 'How much deposit i can deposit to my deposit?'
    ambiguous = 'deposit'
    answer = simple_lesk(sent, ambiguous, pos='v')
    print (answer)
    # Synset('depository_financial_institution.n.01')
    print (answer.definition())
def pywsd_algo():
    a1=disambiguate('How much deposit i can deposit to my deposit?')
    print("a1",a1)
    print("a1-def-1",a1[2][1].definition())
    print("a1-def-2",a1[5][1].definition())
    print("a1-def-3",a1[8][1].definition())

def lex_algo():
    deposit_pos = [(s, s.pos()) for s in wn.synsets('deposit')]
    print("deposit pos",deposit_pos)
    sent= 'How much deposit i can deposit to my deposit?'
    word_token_sent = nltk.word_tokenize(sent)
    word_token_pos = nltk.pos_tag(word_token_sent)
    print("word token pos",word_token_pos)
    tags_to_look=[]
    for (wor, tag) in word_token_pos:
        if wor.lower()=='deposit':
            if tag=='NN':
                tags_to_look.append('n')
            elif tag=="VB":
                tags_to_look.append('v')
            else:
                continue

    for tag in tags_to_look:
        deposit_pos_v= lesk(sent, 'deposit', pos=tag)
    # deposit_pos_n= lesk(sent, 'deposit', pos='n')
        print("deposit pos "+str(tag),deposit_pos_v.definition())
