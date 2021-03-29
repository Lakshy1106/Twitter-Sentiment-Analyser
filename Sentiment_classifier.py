def strip_punctuation(text):
    ''' A function to remove all the punctuation from the text'''
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']                                                                                                                        # Punctuation marks to remove.
    new_text = ''                                                                                                                                                                                                      # Variable to hold new generated text.
    for char in text:
        if char not in punctuation_chars:                                                                                                                                                           # If character is not in punctuation marks add it to the new text
            new_text = new_text + char
    return new_text

def get_pos(text):
    ''' Function to get a score for positive text in the tweet. '''
    
    text = strip_punctuation(text)                                                                                                                                                                   # Removing punctuation
    positive_words = []                                                                                                                                                                                        # List to hold the positive words.  
    with open("positive_words.txt") as pos_f:                                                                                                                                            # Function to extract all positive words from a text file.
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    counter = 0                                                                                                                                                                                                      # Initialising counter to count the positive words.
    text_list = text.split()
    for word in text_list:                                                                                                                                                                                    # Finding all positive words using comparison in a for loop. 
        if word.lower() in positive_words:
            counter = counter + 1
    return counter

def get_neg(text):
    ''' Function to get a score for negative text in the tweet'''
    
    text = strip_punctuation(text)                                                                                                                                                                  # Removing punctuation
    negative_words = []                                                                                                                                                                                     # List to hold the negative words.
    with open("negative_words.txt") as pos_f:                                                                                                                                         # Function to extract all negative words from a text file.
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    counter = 0                                                                                                                                                                                                     # Initialising counter to count the negative words.
    text_list = text.split()
    for word in text_list:                                                                                                                                                                                  # Finding all negative words using comparison in a for loop. 
        if word.lower() in negative_words:
            counter = counter + 1
    return counter

def data_extractor(file_name):
    ''' Function to extract tweet data from the csv file'''
    
    tweet_text_list = []                                                                                                                                                                                     # Creating three lists to hold tweet text, retweet counts, reply counts.
    retweet_count_list = []
    reply_count_list = []
    with open(file_name, 'r') as data:                                                                                                                                # Opening csv file and reading data 
        for each_line in data.readlines():
            text_content = each_line.split(',')
            tweet_text_list.append(text_content[0])
            retweet_count_list.append(text_content[1])
            reply_count_list.append(text_content[2])    
    
    del tweet_list[0]                                                                                                                                                                                         # Removing headers from each column.
    del retweet_list[0]
    del reply_list[0]
    reply_list = [x[:-1] for x in reply_list]                                                                                                                                                    # Removing endline character - \n 
    return tweet_text_list, retweet_count_list, reply_count_list

def analyser(tweet_list):
    ''' Function to analyse each tweet text. '''
    
    positive_score = []                                                                                                                                                                                      # Creating 3 lists to hold positive, negative and net score for each tweet. 
    negative_score = []
    net_score = []
    for tweet in tweet_list:                                                                                                                                                                            # For every tweet in the tweet list this loop will generate positive, negative,net scores.
        positive_score.append(get_pos(tweet))
        negative_score.append(get_neg(tweet))
        # Calculating again for net score
        positive = get_pos(tweet)
        negative = get_neg(tweet)
        net_score.append(positive - negative)
    return positive_score, negative_score, net_score                                                                                                                          # Returning this data back in form of list.

def data_writer(retweet_list,reply_list,positive_score_list,negative_score_list,net_score_list,file_name = "output.csv"):
    ''' Function to write data into a csv file.'''
    
    with open(file_name,"w") as my_file:                                                                                                                                                # Opening the csv file in write mode.
        my_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")                  # Writing file header
        my_file.write("\n")
        for index in range(0, len(retweet_list)):                                                                                                                                       # Writing data line by line using a for loop.
            my_file.write(str(retweet_list[index]) + ',' + str(reply_list[index]) + ',' + str(positive_score_list[index]) + ','+ str(negative_score_list[index]) + ',' + str(net_score_list[index]))
            my_file.write("\n")
    return print("Data written successfully!")

data_file = input("Input the name of your file here. (please make sure the file is located in the same folder with this code.) :  ")
output_file = input("Input the name of the output file with extension. (The default filename is output.csv) : ")

tweet_list ,retweet_list ,reply_list = data_extractor(data_file)                                                                                            # Calling Extractor to Extract Data from csv

positive_score_list, negative_score_list, net_score_list = analyser(tweet_list)                                                              # Calling analyser to analyse the data and generate the result lists.

data_writer(retweet_list,reply_list,positive_score_list,negative_score_list,net_score_list, output_file)             # Calling Data Writer to write data.
