
# **Step 1** : Text cleaning

import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt', encoding='utf-8').read()
# convert the text to lowercase
lower_case_text = text.lower()
# remove punctuation
cleaned_text = lower_case_text.translate(str.maketrans('','',string.punctuation))

# **Step 2** : Tokenzition and Stop Words

tokenized_words = cleaned_text.split()
# remove stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

#print(final_words)

# **Step 3** : Emotion Analysis (Algorithm)

#loop through each line of the emotions file and clean it
emotions_list = []
with open('emotions.txt','r') as emotions_file:
    for line in emotions_file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        #print('Word : '+word+' - Emotion : '+emotion)
        if word in final_words:
            emotions_list.append(emotion)

print(emotions_list)
#Count emotions
emotions_counter = Counter(emotions_list)
print(emotions_counter)

# **Step 4 (Optional)** : Emotions Counter Graph

fig, x_axis = plt.subplots()
x_axis.bar(emotions_counter.keys(),emotions_counter.values())
fig.autofmt_xdate()
plt.show()