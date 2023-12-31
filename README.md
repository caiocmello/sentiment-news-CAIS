# Sentiment News CAIS 


# What do we have ?
- Caio's news headline sentiment annotated dataset
  - No body sentiment

# What do we want to do ?
## Part 1 
### Entities and Sentiment
- [x ] Find most relevant entities using NERC within the news articles.
  - **Round 1**
    - [x] We performed NER with Spacy and collected the named entities by count on the files related to London news articles. The file can be found [here](outputs/round1-entities-to-be-analysed.tsv)
    - [x] Sentence splitting and entity detection was also performed and all files under outputs folder with extension .json.csv are the sentence level entity extracted sentences. 
  - **Round 1.5**
    - [x] For each headline in the annotated datasets in Caio's files
      - [x] Check if the headline is subjective or objective
      - [ ] **Hypothesis** : Sentiment classification for subjective headlines are better than objective.
      - [x] Select only headline mentioning entity **MONEY** also check if they are subjective or objective.
        - [ ] And how good the sentiment classifications of subjective and objective sentences is.
        - [ ] Created file with combined datasets (daily & guardian) including subjectivity, money annotation and sentiment obtained with combination of 3 classifiers (vader, amazonBERT and sent140BERT) [here](data/combined_subjectivityfile.csv)
   - **Round 2**
    - NER with entity resolution. **TODO** 
  - [ ] Qualitative analysis of the extracted entities
  - [ ] **Hypothesis** : Simple entities extracted from NER are less significant then the extracte Co-occurence entities (Wikifier).
  - [ ] Targeted sentiment for the selected specific entities.
- [ ] Calculate the sentiment of the document based on the sentiment of the entities and compare this with
  - [ ] Document level-sentiment analysis
  - [ ] Headline-sentiment analysis (CAIO's previous work).
- [ ] **Hypothesis** : Targeted sentiment analysis is more informative than sentence-level sentiment analyis.
  - [ ] News headline.
  - [ ] Body version.
---
## Part 2a
### News and parts : studying the sentiment over the body parts of the news article.
- [ ] Divide the articles into parts
  - [ ] Suppositions:
    - [ ] Head/Lead : Inverted pyramid, when, what, where, who
    - [ ] Body **More objective than subjective with facts**
    - [ ] Tail/Conclusion: takeaway, what do we conclude
  - [ ] Computing sentiment for each part.
  - [ ] **Is there a correlation between the sentiment of parts of the news articles and headline ?**
  - [ ] How sentiment evolves per part over the length of the news article.
---
## Part 2b
### Subjective and objective headlines : tracking mistakes in sentiment
- [ ] Apply a model to the headlines to classify them into subjective or objective.
- [ ] **Hypothesis** : Disagreement with the gold labels happens more with objective statements.

---
## Part 3
### Emotions
- [ ] TBD

# Data
- [News articles](https://github.com/caiocmello/sentiment-news-CAIS/tree/main/json_data_english) - json with title and body: separated by outlet and event covered (London or Rio)
- [Sentiment annotation](https://zenodo.org/record/6323964)
- [NER (Spacy & Wikifier) code](https://github.com/caiocmello/sentiment-news-CAIS/tree/main/news-cartography-analysis-main)
  
# References
- 
