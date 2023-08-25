# -*- coding: utf-8 -*-
import textblob
import string
import nltk
import re
from nltk.corpus import cmudict

# nltk.download('punkt')
# nltk.download('cmudict')

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if word.endswith("le"):
        count += 1
    if count == 0:
        count += 1
    return count


def analysis(text):
    # TextBlob object
    blob = textblob.TextBlob(text)

    # Sentiment analysis
    polarity, subjectivity = blob.sentiment

    # Positive/negative sentiment
    positive_score = round(max(polarity, 0), 2)
    negative_score = round(max(-polarity, 0), 2)

    # Tokenize the text into sentences and words
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text.lower())

    # Average sentence length
    avg_sentence_length = round(len(words) / len(sentences), 2)

    # Count the number of complex words
    d = cmudict.dict()
    complex_words = [word for word in words if len(d.get(word, [])) > 2]

    # Percentage of complex words
    percent_complex_words = round(len(complex_words) / len(words) * 100, 2)

    # Fog index
    fog_index = round(0.4 * (avg_sentence_length + percent_complex_words), 2)

    # Average number of words per sentence
    avg_words_per_sentence = round(len(words) / len(sentences), 2)

    # Complex word count
    complex_word_count = len(complex_words)

    # Word count
    word_count = len(words)

    # Syllables per word
    words = re.findall(r'\b\w+\b', text)
    syllables = [count_syllables(word) for word in words]
    total_syllables = sum(syllables)
    total_words = len(words)
    average_syllables = round((total_syllables/total_words), 3)

    # Personal pronouns
    pronoun_regex = re.compile(r'\b(i|we|my|ours|(?-i:us))\b',re.I)
    personal_pronouns = pronoun_regex.findall(text)
    personal_pronouns_count = len(personal_pronouns)

    # Average word length
    avg_word_length = round(sum(len(word) for word in words) / len(words), 2)


    # Output
    print(f"Positive score: {positive_score}")
    print(f"Negative score: {negative_score}")
    print(f"Polarity score: {round(polarity, 3)}")
    print(f"Subjectivity score: {round(subjectivity, 3)}")
    print(f"Average sentence length: {avg_sentence_length}")
    print(f"Percentage of complex words: {percent_complex_words}%")
    print(f"Fog index: {fog_index}")
    print(f"Average number of words per sentence: {avg_words_per_sentence}")
    print(f"Complex word count: {complex_word_count}")
    print(f"Word count: {word_count}")
    # print(f"Syllables per word: {syllables}")
    # for i, word in enumerate(words):
    #     print(f"{word}: {syllables[i]} syllable(s)")
    print(f"Average Syllables: {average_syllables}")
    print(f"Personal pronouns: {personal_pronouns}")
    print(f"Personal pronouns count: {personal_pronouns_count}")
    print(f"Average word length: {avg_word_length}")


text = """ paste the article text here, that you extracted from the webpage or from anywhere """

analysis(text)

# In the variable 'text', you just need to paste the article text that you extracted from the given link or from anywhere and run the code to perform Data Analysis.



