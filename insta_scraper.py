import instaloader
import numpy as np

class InstagramScraper:

    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.profile = None
        self.followers_list = []
        self.following_list = []


    def create_session(self):

        L = instaloader.Instaloader()
        L.login(self.username, self.password) # Login or load session
        self.profile = instaloader.Profile.from_username(L.context, self.username) # Obtain profile metadata

    def scrape_followers(self):
        for follower in self.profile.get_followers():
            self.followers_list.append(follower.username)

    def scrape_following(self):

        for followee in self.profile.get_followees():
            self.following_list.append(followee.username)

    def generate_unfollowers_list(self):

        unfollow_list = np.setdiff1d(self.following_list, self.followers_list) # unfollow people who are only in following list and not in followers list
        #print("People to unfollow: ", unfollow_list)

        ydfb_list = []
        for a in self.followers_list:
            if a not in self.following_list:
                ydfb_list.append(a)

        filename = "user_list.txt"
        file = open(filename, "w")
        file.write("\n\nTHEY DON'T FOLLOW BACK\n\n")
        for person in unfollow_list:
            file.write(person + "\n")
        file.write("\n\nYOU DONT FOLLOW BACK\n\n")
        for person in ydfb_list:
            file.write(person + "\n")
        file.close()

