from socialMedia import SocialMedia

class Instagram(SocialMedia): 
    def __init__(self, Name):
        super().__init__(Name)
        self.posts = []

    def publishNewPost(self):
        x = input("your new post: ")
        if(len(x)<= 2200):
          self.posts.append(x)
        else :
            return False
    def getPosts(self):
        for post in self.posts: 
            print(post)
  
insta = Instagram(Instagram)
insta.publishNewPost()
insta.getPosts()