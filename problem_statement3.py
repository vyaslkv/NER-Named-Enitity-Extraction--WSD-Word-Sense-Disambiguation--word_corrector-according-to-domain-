import nltk
raw = open('samplewifi_q.txt').read()
tokens = nltk.word_tokenize(raw)
pairs = nltk.bigrams(tokens)
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(pairs)  # note the difference here!
finder.apply_freq_filter(30)
scored = finder.score_ngrams(bigram_measures.raw_freq)
text_pairs=finder.nbest(bigram_measures.pmi, 10)
text_pair_list=[]
for tup_pair in text_pairs:
    tup_pair_1, tup_pair_2 = tup_pair
    text_pair_list.append(tup_pair_1)
    text_pair_list.append(tup_pair_2)
print("text pair list",text_pair_list)
print('\n')
text = 'i want to connect wife'
tokens = nltk.wordpunct_tokenize(text)
finder = nltk.BigramCollocationFinder.from_words(tokens)
scored = finder.score_ngrams(bigram_measures.raw_freq)
# print(scored)
query_pairs=finder.nbest(bigram_measures.pmi, 20)
print("query pairs",query_pairs)
out_of_domain_list=[]
for pair in query_pairs:
    if pair not in text_pair_list:
        out_of_domain_list.append(pair)
print('\n')
print("pair which is out of the domain",out_of_domain_list)
set_intersection_dict={}
for out_of_domain_pair in out_of_domain_list:
    out_of_domain_pair1 = ''.join(out_of_domain_pair)
    out_of_domain_pair2=set(out_of_domain_pair1)
    for pair in text_pair_list:
        pair1=''.join(pair)
        pair2=set(pair1)
        set_intersection_dict[pair]=len(pair2.intersection(out_of_domain_pair2))
print('\n')
print("pair which got the highest common letters from the faulted pair",set_intersection_dict)
correct_pair=max((value, key) for key, value in set_intersection_dict.items())[1]
print('\n')
print("the corrected pair",correct_pair)
