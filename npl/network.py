import nltk
nltk.download()

sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tokens

#from npl.read_letters import read_letter
#name = 'hino-clube-regatas-flamengo.txt'
#read_letter(name)

f = open('npl/hino-clube-regatas-flamengo.txt', "r")
print(f.readlines())