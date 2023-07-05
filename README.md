# Sentiment News CAIS 


# What do we have ?
- Caio's news headline sentiment annotated dataset
  - No body sentiment

# What do we want to do ?
## Part 1 
### Entities and Sentiment
- [ ] Find most relevant entities using NERC within the news articles.
- [ ] Qualitative analysis of the extracted entities
  - [ ] **Hypothesis** : Simple entities extracted from NER are less significant then the extracte Co-occurence entities (Wikifier).
  - [ ] Targeted sentiment for the selected specific entities.
- [ ] Calculate the sentiment of the document based on the sentiment of the entities and compare this with
  - [ ] Document level-sentiment analysis
  - [ ] Headline-sentiment analysis(CAIO's previous work).
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
