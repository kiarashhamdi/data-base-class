from socialMedia import SocialMedia

class twitter(SocialMedia):
    def __init__(self, Name):
        super().__init__(Name)
        self.tweets = []
    
    def createNewTweet(self):
        x = input("your new tweet: ")
        if(len(x)<= 280):
          self.tweets.append(x)
        else :
            return False
        

    def getTweets(self):
        for tweet in self.tweets: 
            print(tweet)

tw = twitter(twitter)
tw.createNewTweet()
tw.getTweets()
