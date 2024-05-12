
# **Step 1** : Text cleaning

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('read.txt', encoding='utf-8').read()
# convert the text to lowercase
lower_case_text = text.lower()
# remove punctuation
cleaned_text = lower_case_text.translate(str.maketrans('','',string.punctuation))

# **Step 2** : Tokenzition and Stop Words

tokenized_words = word_tokenize(cleaned_text,'english')
# remove stop words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# **Step 3a** : Emotion Analysis (Algorithm)

#loop through each line of the emotions file and clean it
emotions_list = []
with open('emotions.txt','r') as emotions_file:
    for line in emotions_file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        #print('Word : '+word+' - Emotion : '+emotion)
        if word in final_words:
            emotions_list.append(emotion)

#Count emotions
emotions_counter = Counter(emotions_list)

# **Step 3b** : Emotion Analysis (NLTK)

def analyze(text_to_analyze):
    # convert the text to lowercase
    lower_case_text = text_to_analyze.lower()
    # remove punctuation
    cleaned_text = lower_case_text.translate(str.maketrans('','',string.punctuation))

    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    print(score)
    positive_score = score['pos']
    negative_score = score['neg']
    if positive_score > negative_score:
        return 'Positive sentiment'
    elif negative_score > positive_score:
        return 'Negative sentiment'
    else:
        return 'Neutral sentiment'

print(analyze(text))