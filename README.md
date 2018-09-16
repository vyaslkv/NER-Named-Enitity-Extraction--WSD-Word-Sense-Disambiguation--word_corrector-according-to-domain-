# NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-
It was really a nice experience for me, solving these problems. Seriously telling these were not easy for me, every problem statement I saw at first nothing came to my mind. But then I started searching what does that problem statement means. So, with the time constrined there were many things, I was not able to go in deep. 

Problem statement 1:
	Framework: Any nlp tool (Preference: spaCy), Python,
	Given a training dataset. Create a NER model for following labels:
	● Loan
	● Home
	● Overseas
	● Renovation
	● Refinancing
	● Property
	For a user query “can i loan for property in philippines?”, the output from your NER
	model is Loan, Property and Overseas.

Solution:
	We need to make or train a model which can point out these custom lables from the user query (Named Entity Extraction), which are given in the problem statement.
As there was no training dataset was provided, I made a small one by myself. But as If I would have made and labeled the training dataset for all the custom lables It would have taken a lot of time, so, really sorry taking time in consideration, I only trained for the LOAN label and labelled some of the   training sentences for that. As shown below:(one more thing in these training examples I forgot to add *get* after *can i* sorry for this mistake, I just realised this while writing this document)
![results](https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/master/result_pics/training_data_prbm1.png)







From the model, we got results as given below:
when the query is:
can i loan for property in philippines?
![res](https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm1_result1.png|alt=octocat)


When the query is:
can i get the allowance for property in philippines?
[[https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm1_result2.png|alt=octocat]]


When the query is:
can i get investment for the place in india?

[[https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm_result3.png|alt=octocat]]

Similary tried other queries as well.

























Problem statement 2:
	Framework: Any nlp tool (Preference: spaCy), Python
	Create a WSD model for identifying the intent of a token in a context
	● Deposit
	○ Deposit is a word which a have three meanings. Deposit is a money,
	Deposit is an account, Deposit is a process.
	Sample query: I want to deposit money in my deposit.
	How much deposit i can deposit to my deposit?
	Your module can disambiguate and identify the sense of each “deposit” word.

Solution:
	For this we need to make a model which can identity the intent of a word used in the sentence.
Approach 1:(in brief)
	In this I got the possible definitions of word “deposit” from the wordnet then used cosine similarity to find out which definition is most similar to the user query. 
The user query is :
I want to deposit money in my deposit How much deposit i can deposit to my deposit?

And the definitions or contexts of every word deposit we got are:
[[https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm2_result1.png|alt=octocat]]


Approach 2:(in brief)
	The above query was complex but for simple queries I there is one solution, for that I copied some text regarding about the diffrent context of word deposit and pasted them in a text file.(not relaible but for simple queries it works which are very simple or common.)
[[https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm2_result_sec.png|alt=octocat]]

Some other approaches for this problem statement I have tried they are all given in the python file.
















Problem statement 3:
	Framework: Any nlp tool (Preference: spaCy), Python
	Create a spell correction module which will correct the words depending on the
	context/domain.
	Domain : IT support
	User query: I want to connect my wife.

Solution:
	This was very difficult one for me, finally I came to a approach where I will add a text document (In which about the domain specific text is given), then I will find the most frequent occuring pairs in from that text file:
what I mean:
	connect-wifi is more frequent  pair than connect-wife in the IT support domain.
	So I got the pairs and got the  pairs from the user query 
	then found which pair is out of the context :

query: i want to connect wife
[[https://github.com/vyaslkv/NER-Named-Enitity-Extraction--WSD-Word-Sense-Disambiguation--word_corrector-according-to-domain-/blob/master/result_pics/prblm3_result1.png|alt=octocat]]

I know this is not the good solution, sorry for that.


