<a name="top"></a>
![name of photo](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/title.jpg?raw=true)

***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Acquire & Prep](#acquire_and_prep)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
[[Recreate This Project](#recreate)]
___


## <a name="project_description"></a> 
![desc](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/project_desc.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Description
- Using web-scraping techniques scrape githubs doctor who repositories to take the text from the readme files and the primary coding language; to build a data set. Then transform the new dataset into a form that can be used in a natural language processing machine learning model (NLP)., and choosing the best one for predicting the coding language based on the text from readme files.

### Goals
- Create a NLP model to predict the programming language used in a github repository based on the words and word combinations found in the readme files.
    
### Where did you get the data?
- Web scrapping github with the search term "Doctor Who"

    
    
    
### Resume Write Up

Project Name: Predicting Coding Language
    
explain the project for resume:
    

</details>
    
    
## <a name="planning"></a>
![plan](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/project_plan.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Projet Outline:
    
- Acquisiton of data
    - Search for Doctor who repos on git hub
    - Web scrape to gather data
- Prepare and clean data with python - Jupyter Labs
    - Drop nulls
    - Make all text lowercase
    - Tokenize the data
    - Stem/Lemmatize
    - Remove stopwords
- Explore data:
    - How often are words used?
        - Count
        - Percentage
    - Check out word clouds for top 4 languages
        - Is ther anything that stands out?
    - Check out bar graphs using bigrams for top 4 languages
        - Is there anything of importance?
    - Check out word clouds using bigrams for top 4 languages
        - What di you notice?
- Modeling:
    - Make multiple models.
    - Pick best model.
    - Test Data.
    - Conclude results.
    
### Target variable
- Language

</details>

    
## <a name="findings"></a>
![find](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/key_findings.png?raw=true)

[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Explore:
- There were no commonalities between the languages and their top 20 words/phrases.
- Java script is the most commonly used coding language and makes up the top 10 most frequent words of all languages together.
- There are specific phrases/words that are used more often in each coding language.
    
### Modeling:
- Baseline:
    - 29.5%
- Models Made:
    - Logistic Regression
    - Balanced Logistic Regression
    - KNN
    - Decision Tree
    - Random Forest
    - Ridge Classifier
    - SDG Classifier
- Best Model:
    - SDG Classifier
- Model testing:
    - Train
        - 97.7%
    - Validate
        - 57.9%
- Performance:
    - Test
        - 43.8%

***

    
</details>

## <a name="dictionary"></a> 
![dict](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/data_dict.png?raw=true)

[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Data Used
    
| Attribute | Definition | Data Type |
| ----- | ----- | ----- | 
| all_clean_lemma | all cleaning stages done using lemmatizing | string |    
| all_clean_stem | all cleaning stages done using stemming | string | 
| cleaned_content | contents of REASME file ran through a basic clean funciton | string |
| language* | coding language primarily used in the repository | string |
| lemma_content | tozenized_content ran through a lemmatizing funciton | string |
| no_stopwords_lemma | stopwords removed from lemma_content | string |
| no_stopwords_stem | stopwords removed from stemmed_content | string |
| readme_contents | contents of README file directly from repository | string |
| repo | name of repository | string |
| stemmed_content | tokenized_content ran through a stemming funciton | string |
| tokenized_content | cleaned_content ran through tokenized funciton | string |

\*  Indicates the target feature in this Zillow data.

***
</details>

## <a name="acquire_and_prep"></a>
![acquire_prep](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/acquire_prepare.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Acquire Data:
1. I went to https://github.com/ 
2. Typed "Doctor Who" into the search bar
3. I then created a function to scrape all the repos that came up with this search
4. These functions then went into webscraping functions to create a csv containing the repo file name, primary coding language used, and the contents of the README files.

*To see all funcitons used in the data acquisition stage please see the acquire.py file in my github repository*
    
### Prepare Data
1. Drop all null values in language and readme_content
2. Make all characters in readme_content lowercase
3. Tokenize the strings in readme_content
4. Stem/Lemmatize the strings
5. Remove stopwords inludeing some new stopwords of my choosing.

- Please note that:
    - I chose to create a new column for each step of the cleaning process.
        - I did this because if I wanted to come back and add in repos later on, I may need to use stemming process instead of the lemmatizing process.d.

*For functions used in the cleaning process please see my prepare.py in my github repository*

***

</details>



## <a name="explore"></a> 
![dict](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/explore.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>
    

### Findings:
- There were no commonalities between the languages and their top 20 words/phrases.
- Java script is the most commonly used coding language and makes up the top 10 most frequent words of all languages together.
- There are specific phrases/words that are used more often in each coding language.

***

</details>    


## <a name="model"></a> 
![model](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/model.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

Summary of modeling choices...
        
    
### Models:
- Logistic Regression
- Balanced Logistic Regression
- KNN
- Decision Tree
- Random Forest
- Ridge Classifier
- SDG Classifier

    
### Baseline Accuracy  
- 29.5%

### Logistic Regression Model
Model Train Accuracy:  
    - 95.5%
    
### Balanced Logistic Regression Model
Model Train Accuracy:  
    - 97.7%
    
### KNN Model
Model Train Accuracy: 
    - 61.4%
    
### Decisiion Tree Model 
Model Train Accuracy: 
    - 52.3%
 
### Rndom Forest Model
Model Train Accuracy: 
    - 43.2
    
### Ridge Classifier Model
Model Train Accuracy: 
    - 54.5%
    
### SDG Classifier Model
Model Train Accuracy: 
    - 97.7%


## Selecting the Best Model:
- SDG Classifier Model
    - Model Validate Accuracy
        - 57.9%
   
## Testing the Model
    - 43.8% accuracy


***

</details>  

## <a name="conclusion"></a> 
![conclusion](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/conc.png?raw=true)
[[Back to top](#top)]
<details>
  <summary>Click to expand!</summary>

I found that there are no commonalities in frequent words or phrases between the top 4 coding languages. I also found the Java script is the most commonly used out of the languages and makes up for the most common top 10 most common words out af all of the langauges.
    
With more time I would love to gether more repos and see if I can improve the model by obtaining more observations.

I recommend using this model to predict the primary coding language used based on github readme files. 


</details>  


## <a name="Recreate This Project"></a>
![recreate](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/re-create.png?raw=true)
[[Back to top](#top)]

<details>
  <summary>Click to expand!</summary>

### Getting started

1. Go to https://github.com/
2. Type "Doctor Who" into the search bar
3. Use first 2 funcitons in the acquire file in my git hub repository to get the list of repos.
4. Copy and past this list into the list named REPOS in the acquire.py file
5. Run the last funciton in acquire.py file
6. Run this new dataframe through each funciton in the pepare.py file in my github repository to clean the data.
    
Good luck I hope you enjoy your project!

</details>
    


## 

![Folder Contents](https://github.com/CaitlynCarney/coding_language_prediction/blob/main/photos/for_readme/file_outline.jpg?raw=true)


>>>>>>>>>>>>>>>
.
