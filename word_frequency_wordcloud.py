
f = open("input.txt", 'r')
lines_file = f.readlines()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
words_dict={}

#for each line Remove punctuation marks. check isalpha()
#Split words

for line in lines_file:
    words_in_line=line.split()
    for word in words_in_line:
        if(word.isalpha()==False):
            #print("Word   ",word)
            for punct in punctuations:
                word = word.replace(punct,"")
                #print(word)
#remove uninteresting words (a, the ,to , if)             
        if word not in uninteresting_words:
            #print(word)
            try:
                words_dict[word]+=1
            except KeyError as e:
                words_dict[word]=1
                
print(words_dict)

import wordcloud
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(words_dict)
cloud.to_file("wordcloud.jpg")