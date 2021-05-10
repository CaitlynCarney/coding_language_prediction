import pandas as pd
import numpy as np

import re
import unicodedata
import nltk

import matplotlib.pyplot as plt
import seaborn as sns

import acquire
import prepare

from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


#-----------------------------------------------------------------------------
# Percents and counts

def show_counts_and_ratios(dw):
    '''takes in the dataframe
    shows the number of times each language is used
    shows the percentage of the readmes are in each coding language'''
    # create languages df to hold number and percent
    languages = pd.concat([dw.language.value_counts(),
                    dw.language.value_counts(normalize=True)], axis=1)
    # rename columns
    languages.columns = ['n', 'percent']
    # return new df
    return languages

def plot_count_and_percent(dw):
    '''plots the number of times each language is used
    plot the percent that each language has been used'''
    # set the subplot information
    plt.subplots(1, 2, figsize=(55,16), sharey=True)
    sns.set(style="darkgrid")
    # create the count subplot
    plt.subplot(1,2,1)
    plt.title("Count of Coding Languages Used", size=20, color='black')
    sns.countplot(x='language', data=dw,
                   palette='Blues_d', edgecolor='black')
    # create the percentage subplot
    plt.subplot(1,2,2)
    plt.title("Percent of Coding Languages Used", size=20, color='black')
    sns.barplot(y=languages.percent, x=languages.index, palette='Blues_d', edgecolor='black')

#-----------------------------------------------------------------------------
# Create needed values

def seperate_top_six(dw):
    ''' takes in specified dataframe
    separates each language into their own string of words
    returns everything the top 6 languages'''
    # Separate the top 6 languages
    # Separate Java Script Words
    js_words = ' '.join(dw[dw.language == 'JavaScript'].all_clean)
    js_words = js_words.split()
    # Separate HTML Words
    html_words = ' '.join(dw[dw.language == 'HTML'].all_clean)
    html_words = html_words.split()
    # Separate Java Words
    java_words = ' '.join(dw[dw.language == 'Java'].all_clean)
    java_words = java_words.split()
    # Separate Python Words
    python_words = ' '.join(dw[dw.language == 'Python'].all_clean)
    python_words = python_words.split()
    # Separate C# Words
    cpound_words = ' '.join(dw[dw.language == 'C#'].all_clean)
    cpound_words = cpound_words.split()
    # Separate CSS Words
    css_words = ' '.join(dw[dw.language == 'CSS'].all_clean)
    css_words = css_words.split()
    return js_words, html_words, java_words, python_words, cpound_words, css_words
    
def string_for_all(dw):
    ''' takes in specified dataframe
    returns a string of all words found through all langages'''
    # create one for all words
    all_words = ' '.join(dw.all_clean)
    all_words = all_words.split()
    return all_words

def seperate_leftovers(dw):
    # seperate the remaining just in case
    ''' takes in specified dataframe
    separates each language into their own string of words
    returns everything but the top 6 languages'''
    # Separate CSS Words
    swift_words = ' '.join(dw[dw.language == 'Swift'].all_clean)
    swift_words = swift_words.split()
    # Separate CSS Words
    c_words = ' '.join(dw[dw.language == 'C'].all_clean)
    c_words = c_words.split()
    # Separate CSS Words
    dart_words = ' '.join(dw[dw.language == 'Dart'].all_clean)
    dart_words = dart_words.split()
    # Separate CSS Words
    jupyter_words = ' '.join(dw[dw.language == 'Jupyter Notebook'].all_clean)
    jupyter_words = jupyter_words.split()
    # Separate CSS Words
    script_words = ' '.join(dw[dw.language == 'TypeScript'].all_clean)
    script_words = script_words.split()
    # Separate CSS Words
    arduino_words = ' '.join(dw[dw.language == 'Arduino'].all_clean)
    arduino_words = arduino_words.split()
    # Separate CSS Words
    ruby_words = ' '.join(dw[dw.language == 'Ruby'].all_clean)
    ruby_words = ruby_words.split()
    # Separate CSS Words
    tsql_words = ' '.join(dw[dw.language == 'TSQL'].all_clean)
    tsql_words = tsql_words.split()
    # Separate CSS Words
    kotlin_words = ' '.join(dw[dw.language == 'Kotlin'].all_clean)
    kotlin_words = kotlin_words.split()
    # Separate CSS Words
    r_words = ' '.join(dw[dw.language == 'R'].all_clean)
    r_words = r_words.split()
    # Separate CSS Words
    lua_words = ' '.join(dw[dw.language == 'Lua'].all_clean)
    lua_words = lua_words.split()
    # Separate CSS Words
    php_words = ' '.join(dw[dw.language == 'PHP'].all_clean)
    php_words = php_words.split()
    # Separate CSS Words
    go_words = ' '.join(dw[dw.language == 'Go'].all_clean)
    go_words = go_words.split()
    # Separate CSS Words
    vue_words = ' '.join(dw[dw.language == 'Vue'].all_clean)
    vue_words = vue_words.split()
    # return them
    return swift_words, c_words, dart_words, jupyter_words, script_words, arduino_words, ruby_words, tsql_words, kotlin_words, r_words, lua_words, php_words, go_words, vue_words
    
#-----------------------------------------------------------------------------
# Create frequency values

def top_six_freq(js_words, html_words, java_words, python_words, cpound_words, css_words):
    ''' takes in specified dataframe
    separates each language into their own string of words
    returns everything the top 6 languages'''
    # Separate the top 6 languages
    js_freq = pd.Series(js_words).value_counts()
    html_freq = pd.Series(html_words).value_counts()
    java_freq = pd.Series(java_words).value_counts()
    python_freq = pd.Series(python_words).value_counts()
    cpound_freq = pd.Series(cpound_words).value_counts()
    css_freq = pd.Series(css_words).value_counts()
    return js_freq, html_freq, java_freq, python_freq, cpound_freq, css_freq
    
    
def all_freq(all_words):
    ''' takes in specified dataframe
    returns a string of all freq found through all langages'''
    # create one for all freq
    all_freq = pd.Series(all_words).value_counts()
    return all_freq

def leftovers_freq(swift_words, c_words, dart_words, jupyter_words, script_words, arduino_words, ruby_words, tsql_words, kotlin_words, r_words, lua_words, php_words, go_words, vue_words):
    ''' takes in specified dataframe
    separates each language into their own string of freq
    returns everything but the top 6 languages'''
    # seperate the remaining just in case
    swift_freq = pd.Series(swift_words).value_counts()
    c_freq = pd.Series(c_words).value_counts()
    dart_freq = pd.Series(dart_words).value_counts()
    jupyter_freq = pd.Series(jupyter_words).value_counts()
    script_freq = pd.Series(script_words).value_counts()
    arduino_freq = pd.Series(arduino_words).value_counts()
    ruby_freq = pd.Series(ruby_words).value_counts()
    tsql_freq = pd.Series(tsql_words).value_counts()
    kotlin_freq = pd.Series(kotlin_words).value_counts()
    r_freq = pd.Series(r_words).value_counts()
    lua_freq = pd.Series(lua_words).value_counts()
    php_freq = pd.Series(php_words).value_counts()
    go_freq = pd.Series(go_words).value_counts()
    vue_freq = pd.Series(vue_words).value_counts()
    # return them
    return swift_freq, c_freq, dart_freq, jupyter_freq, script_freq, arduino_freq, ruby_freq, tsql_freq, kotlin_freq, r_freq, lua_freq, php_freq, go_freq, vue_freq
    
#-----------------------------------------------------------------------------
# see the top 20 words for the top 4 languages

def top_20_js(js_words):
    'print the top 20 words used in java script'
    # print top 20
    print(js_words[:20])
    
def top_20_html(html_words):
    '''print out top 20 words used in html'''
    # pritn top 20
    print(html_words[:20])
    
def top_20_java(java_words):
    '''print out the top 20 words used in java script'''
    # print top 20
    print(java_words[:20])
    
def top_20_python(python_words):
    '''print top 20 words used in html'''
    # print top 20
    print(python_words[:20])
    
def top_20_of_all(all_words):
    '''print top 20 words out of all langages'''
    # print top 20
    print(all_words[:20])
#-----------------------------------------------------------------------------
# see the top 20 words for the top 4 languages bigrams

def top_20_js_bi(js_words):
    '''print the top 20 bigrams used in java script'''
    # change to string format
    js_words = ' '.join(js_words)
    # make bigram
    js_bigrams = (pd.Series(nltk.ngrams(js_words.split(), 2)).value_counts().head(30))
    # print the top 20
    print(js_bigrams[:20])
    
def top_20_html_bi(html_words):
    '''print out top 20 word combos used in html'''
    # turn into string format
    html_words = ' '.join(html_words)
    # create bigram
    html_bigrams = (pd.Series(nltk.ngrams(html_words.split(), 2)).value_counts().head(30))
    # print top 20
    print(html_bigrams[:20])
    
def top_20_java_bi(java_words):
    '''print top 20 word combos used in java'''
    # string format
    java_words = ' '.join(java_words)
    # create bigram
    java_bigrams = (pd.Series(nltk.ngrams(java_words.split(), 2)).value_counts().head(30))
    # print top 20
    print(java_bigrams[:20])
    
def top_20_python_bi(python_words):
    '''print top 20 word combos used in pandas'''
    # string format
    python_words = ' '.join(python_words)
    # create bigrams
    python_bigrams = (pd.Series(nltk.ngrams(python_words.split(), 2)).value_counts().head(30))
    # print top 20
    print(python_bigrams[:20])
    
def top_20_of_all_bi(all_words):
    '''print top 20 word combos used throughtout all coding languages'''
    # string format
    all_words = ' '.join(all_words)
    # create bigrams
    all_bigrams = (pd.Series(nltk.ngrams(all_words.split(), 2)).value_counts().head(30))
    # print top 20
    print(all_bigrams[:20])
    
#-----------------------------------------------------------------------------
# word clouds that feed into final word cloud for presentation

def js_words_cloud(js_words):
    '''takes in words found in java script readme files
    creates a word cloud out of the words on their own'''
    # make js_words into string format
    js_words = ' '.join(js_words)
    #plt.figure(figsize=(16,8))
    # set the mask to change the shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/cyber_sil.jpeg'))
    # create the word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=70,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(js_words)
    plt.imshow(img)
    plt.axis('off')
    
def html_words_cloud(html_words):
    '''create word cloud to hold html words'''
    # change to string
    html_words = ' '.join(html_words)
    #plt.figure(figsize=(16,8))
    # set mask to change shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/dalek_sil.jpeg'))
    # create word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=20,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(html_words)
    plt.imshow(img)

    plt.axis('off')
    
def java_words_cloud(java_words):
    '''create word cloud for words foudn in java'''
    # string format
    java_words = ' '.join(java_words)
    # make mask to change shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/k9.jpeg'))
    # create word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000,
                    contour_color='white', contour_width=20,
                    stopwords=STOPWORDS, max_font_size=256,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(java_words)
    plt.imshow(img)
    plt.axis('off')
    
def python_words_cloud(python_words):
    ''''''
    python_words = ' '.join(python_words)
    #plt.figure(figsize=(16,8))
    mask = np.array(Image.open('/Users/caitlyncarney/masks/angel_sil.jpeg'))
    image_colors = ImageColorGenerator(mask)
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=50,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(python_words)
    plt.imshow(img)

    plt.axis('off')

#-----------------------------------------------------------------------------
# For presentation (single word word cloud)

def compare_single_clouds(js_words, html_words, java_words, python_words):
    plt.subplots(1, 4, figsize=(40,16), sharey=True)
    sns.set(style="darkgrid")

    plt.subplot(1,4,1)
    js_words_cloud(js_words)

    plt.subplot(1,4,2)
    html_words_cloud(html_words)

    plt.subplot(1,4,3)
    java_words_cloud(java_words)

    plt.subplot(1,4,4)
    python_words_cloud(python_words)
    
#-----------------------------------------------------------------------------
# For presentation (all words word cloud)

def all_words_cloud(all_words):
    all_words = ' '.join(all_words)
    plt.figure(figsize=(16,8))
    mask = np.array(Image.open('/Users/caitlyncarney/masks/all_docs.jpg'))
    image_colors = ImageColorGenerator(mask)
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=5,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate(all_words)
    plt.imshow(img)

    plt.axis('off')
    
#-----------------------------------------------------------------------------
# bigram word clouds that feed into final bigram word cloud for presentation

def js_bi_cloud(js_words):
    '''create word clouds out of the top bigrams'''
    # make into string
    js_words = ' '.join(js_words)
    # create bigrams
    js_bigrams = (pd.Series(nltk.ngrams(js_words.split(), 2)).value_counts().head(30))
    # make the plot
    #plt.figure(figsize=(16,8))
    # set bigrams to a value
    data = {k[0] + ' ' + k[1]: v for k, v in js_bigrams.to_dict().items()}
    # make the mask to change the shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/cyber_sil.jpeg'))
    # make the wordcloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=70,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate_from_frequencies(data)
    plt.imshow(img)
    plt.axis('off')
    
def html_bi_cloud(html_words):
    '''create word cloud to hold most frequent word combos'''
    # change to string
    html_words = ' '.join(html_words)
    # create bigrams
    html_bigrams = (pd.Series(nltk.ngrams(html_words.split(), 2)).value_counts().head(30))
    # create plot
    #plt.figure(figsize=(16,8))
    # set bigrams to value
    data = {k[0] + ' ' + k[1]: v for k, v in html_bigrams.to_dict().items()}
    # make mask to change the shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/dalek_sil.jpeg'))
    # create word cloud
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=20,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate_from_frequencies(data)
    plt.imshow(img)
    plt.axis('off')

def java_bi_cloud(java_words):
    '''make wordloud for words found in java language'''
    # string format
    java_words = ' '.join(java_words)
    # create bigrams
    java_bigrams = (pd.Series(nltk.ngrams(java_words.split(), 2)).value_counts().head(30))
    # set bigram as a variable
    data = {k[0] + ' ' + k[1]: v for k, v in java_bigrams.to_dict().items()}
    # set mask to change shape
    mask = np.array(Image.open('/Users/caitlyncarney/masks/k9.jpeg'))
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=20,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate_from_frequencies(data)
    plt.imshow(img)
    plt.axis('off')
    
def python_bi_cloud(python_words):
    python_words = ' '.join(python_words)
    python_bigrams = (pd.Series(nltk.ngrams(python_words.split(), 2)).value_counts().head(30))
    #plt.figure(figsize=(16,8))
    data = {k[0] + ' ' + k[1]: v for k, v in python_bigrams.to_dict().items()}
    mask = np.array(Image.open('/Users/caitlyncarney/masks/angel_sil.jpeg'))
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=20,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate_from_frequencies(data)
    plt.imshow(img)
    plt.axis('off')

#-----------------------------------------------------------------------------
# For presentation (all bigram words word cloud)

def compare_bigram_clouds(js_words, html_words, java_words, python_words):
    plt.subplots(1, 4, figsize=(40,16), sharey=True)
    sns.set(style="darkgrid")
    
    plt.subplot(1,4,1)
    js_bi_cloud(js_words)

    plt.subplot(1,4,2)
    html_bi_cloud(html_words)
    
    plt.subplot(1,4,3)
    java_bi_cloud(java_words)
    
    plt.subplot(1,4,4)
    python_bi_cloud(python_words)
#-----------------------------------------------------------------------------
# For presentation (all words bigram word cloud)

def all_bi_cloud(all_words):
    all_words = ' '.join(all_words)
    all_bigrams = (pd.Series(nltk.ngrams(all_words.split(), 2)).value_counts().head(30))
    plt.figure(figsize=(16,8))
    data = {k[0] + ' ' + k[1]: v for k, v in all_bigrams.to_dict().items()}
    mask = np.array(Image.open('/Users/caitlyncarney/masks/blue_dw.jpeg'))
    img = WordCloud(background_color="black", mask=mask, max_words=2000, 
                    contour_color='white', contour_width=70,
                    stopwords=STOPWORDS, max_font_size=156,
                    random_state=42, width=1000, height=800, colormap='Blues').generate_from_frequencies(data)
    plt.imshow(img)
    plt.axis('off')

#-----------------------------------------------------------------------------
# For presentation (bigram bar plots)

def compare_bigrams(js_words, html_words, java_words, python_words):
    '''takes in words from top 4 coding languages
    makes a bigram for each of the 4 languages
    plots a bar graph to show frequency of each of the top 20 word combos used'''
    # change to string format and create needed bigrams
    js_words = ' '.join(js_words)
    js_bigrams = (pd.Series(nltk.ngrams(js_words.split(), 2)).value_counts().head(20))
    html_words = ' '.join(html_words)
    html_bigrams = (pd.Series(nltk.ngrams(html_words.split(), 2)).value_counts().head(20))
    java_words = ' '.join(java_words)
    java_bigrams = (pd.Series(nltk.ngrams(java_words.split(), 2)).value_counts().head(20))
    python_words = ' '.join(python_words)
    python_bigrams = (pd.Series(nltk.ngrams(python_words.split(), 2)).value_counts().head(20))
    # set up for subplotting
    plt.subplots(1,4, figsize=(20,8), sharey=True)
    sns.set(style="darkgrid")
    # create plot for java script
    plt.subplot(1,4,1)
    js_bigrams.plot.bar(color='darkblue', width=.9)
    plt.title("Java Script Top 20 Bigrams")
    plt.ylabel("Bigram")
    plt.xlabel("Frequency")
    # create plot for HTML
    plt.subplot(1,4,2)
    html_bigrams.plot.bar(color='mediumblue', width=.9)
    plt.title("HTML Top 20 Bigrams")
    plt.ylabel("Bigram")
    plt.xlabel("Frequency")
    # create plot for Java
    plt.subplot(1,4,3)
    java_bigrams.plot.bar(color='dodgerblue', width=.9)
    plt.title("Java Top 20 Bigrams")
    plt.ylabel("Bigram")
    plt.xlabel("Frequency")
    # create plot for Python
    plt.subplot(1,4,4)
    python_bigrams.plot.bar(color='skyblue', width=.9)
    plt.title("Python Top 20 Bigrams")
    plt.ylabel("Bigram")
    plt.xlabel("Frequency")
    # make it shine
    plt.tight_layout()
    plt.show()
    
#-----------------------------------------------------------------------------
# For presentation (all words bigram barchart)

def all_bigrams_bar(all_words):
    all_words = ' '.join(all_words)
    all_bigrams = (pd.Series(nltk.ngrams(all_words.split(), 2)).value_counts().head(20))
    plt.figure(figsize=(16,8))
    sns.set(style="dark")
    all_bigrams.plot.bar(color='lightskyblue', width=.9)
    plt.title("Top 20 Bigrams Over All Languages")
    plt.ylabel("Bigram")
    plt.xlabel("Frequency")
    plt.show()

