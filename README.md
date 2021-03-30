Description.

This repository stores the code for my self guided project on Twitter sentiment analysis.
You can use this code for analysing twitter data stored in a csv file and determine the net score of many tweets at a single time.
Here Net score means how positive a tweet is, if the net score is negative the tweet sentiment is negative.
The output file contains the number of retweets and replies each tweet got with number of positive words or negative words each tweet has used.

Instructions for use.
1) Make sure your input csv file containing the tweet data is sored in same folder as your code.
2) The input tweet data file must have tweet text, retweet count and reply count for each tweet.
3) The output file is generated in csv format and contains retweet count, reply count, positive score, negative score and net score for each tweet in your input file.

Known Issues.
1) Not giving any input to output fle name causes an error which should not be the case as default value is defined. 
Remedy - Please make sure you always give an output file name as an input and dont rely on default value until I fix this issue. 
