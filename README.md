# Twitter Hate Speech detection

We collect and sort out the Twitter datasets use the paper, official API and hatebase API.  
Then we use these dataset and deep learning methods, such as SVM, LSTM, bi-LSTM to train the model for the Twitter hate speech detection.

## 1. Under the dataset collection folder:

DownloaderCode folder is to reconstruct the dataset for the paper Ayme Arango, Jorge P ´ erez, and Barbara Poblete. 2019. Hate Speech
Detection is Not as Easy as You May Think: A Closer Look at Model Validation https://github.com/aymeam/User_distribution_experiments.  
Download_Data.py is the update version of the original code. It is to download Tweets base on the Twitter user ID and labels.
TwitterAPICode folder is the Twitter official API that we implemented to capture the Tweets with the hateful keyword.  
Dataset.html is the datasets list that we collected for the research.

## 2. Under the HateBaseAPICode folder:

The hateBaseAPI.py (https://hatebase.org/) is to capture the hateful terms of 7 categories. The results are in the hateType folder.  
The Load_Json.py is to filter out those hateful terms from the previous hatebase result that the probability of a hateful context is larger than 60 percent.  
The results are in the resultCSV folder.  
The wordCloud.py uses those hateful terms to generate a word cloud image for one year. The results are in the wordCloud -> trialImage folder.  
The WordcloudAll.py uses those hateful terms to generate a word cloud image(wordcloud.png) for 5 years(2015-2020).

## 3. Under the HatespeechDeepLearning folder:

The HatespeechDeepLearning includes the code we implement for SVM, LSTM, bi-LSTM methods, the results with these models also included in this folder.
We use the dataset we collect from the dataset collection folder and HateBaseAPICode folder to train the model.
The original version of this code is from https://github.com/srishb28/Hate-Speech-Detection-on-Twitter-Data.
