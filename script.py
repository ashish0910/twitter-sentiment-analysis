from textblob import TextBlob
import sys , tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)

consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

auth = tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api = tweepy.API(auth)

searchItem = input("Enter Hashtag to search about -> ")
intSearchTerms = int(input("Enter number of tweets you want to analyze ->"))

tweets = tweepy.Cursor(api.search ,q = searchItem , lang = "English").items(intSearchTerms)

polarity = 0
negativity = 0
positivity = 0
neutrality = 0

for tweet in tweets :
    analysis = TextBlob(tweet.text)
    print(tweet.text)
    temp = analysis.sentiment.polarity
    polarity = polarity + temp
    
    if(temp == 0):
        neutrality = neutrality + 1
    
    elif(temp < 0):
        negativity = negativity + 1    
    
    elif(temp > 0):
        positivity = positivity + 1
        
        
        
positivity = percentage(positivity,intSearchTerms)
negativity = percentage(negativity,intSearchTerms)
neutrality = percentage(neutrality,intSearchTerms)
polarity = percentage(polarity,intSearchTerms)

neutrality = format(neutrality, '.2f')
negativity = format(negativity, '.2f')
positivity = format(positivity, '.2f') 

print("resultant emotion is ->")      

if(polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positive") 
    
labels = ['Positive('+str(positivity)+'%)','Negative('+str(negativity)+'%)','Neutral('+str(neutrality)+'%)']
sizes = [positivity,negativity,neutrality]  
colors = ['red','green','blue']
patches , texts = plt.pie(sizes,colors = colors , startangle = 90) 
plt.legend(patches,labels,loc="best")  
plt.title("Analysis")
plt.axis('equal')
plt.tight_layout()
plt.show()





        
        