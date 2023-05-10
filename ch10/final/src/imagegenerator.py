import requests
import random
import pygame
from src import ipgrabber
from src import jokegenerator
import io

class ImageGenerator:
        
    def __init__(self):
        '''
        intializes all essential items needed to create the image within the get function
        '''
        pygame.init()
        self.ip = False
        self.url = "https://img.bruzu.com/"
        self.font = "&b.color=orange&b.fontFamily=Poppins&b.fontWeight=800"
        self.outline = "&a.color=black&a.fontFamily=Poppins&a.fontWeight=800&a.fontSize=41"
        self.backdrop = self.background()
        self.joke_gen = jokegenerator.JokeGen()
        self.ip_grab = ipgrabber.ipcheck()

    def get(self):
        '''
        this get function puts together the full url that will be displayed in the controller file
        return:
            self.image (Surface): returns the image made within the program
        '''
        if self.ip==False:
            self.text = self.joke_gen.get()
        else:
            self.text = self.ip_grab.get()
        self.image_url = self.url +f"?backgroundImage={self.backdrop}&a.text={self.text}{self.outline}&b.text={self.text}{self.font}"
        self.response=requests.get(self.image_url)
        self.img_data = self.response.content
        self.image = pygame.image.load(io.BytesIO(self.img_data))
        return self.image

    def background(self):
        '''
        allows user to choose from funny or motivational picture, the function then randomly chooses one of the backgrounds


        return:
            pathing (str): the url for the background is returned
        '''
        self.mood=["funny","motivational"]
        funny = [
            "https://img.freepik.com/free-vector/comic-pop-art-cloud-bubble-funny-speech-bubble-trendy-colorful-retro-vintage-background-pop-art-retro-comic-style-illustration-easy-editable_91128-1398.jpg",
            "https://wallpapercave.com/wp/BJ9xAkh.jpg",
            "https://wallpaperset.com/w/full/c/8/9/525448.jpg",
            "https://t3.ftcdn.net/jpg/05/11/86/68/360_F_511866812_PNzfiKtyCRCskrWxqVVf0emszxhAeufK.jpg"
        ]
        motivational = [
            "https://static.vecteezy.com/system/resources/thumbnails/005/205/623/small/silhouette-of-businessman-on-mountain-top-over-sunset-sky-background-business-success-leadership-and-achievement-concept-free-photo.jpg",
            "https://t3.ftcdn.net/jpg/03/88/29/88/360_F_388298845_T1URO6DKys4Aj8abLDRua2ZH72FJ7pMQ.jpg",
            "https://e1.pxfuel.com/desktop-wallpaper/699/101/desktop-wallpaper-motivational-and-inspirational-backgrounds-music-for-videos-motivation-background.jpg",
            "https://thumbs.dreamstime.com/b/relaxing-seascape-wide-horizon-sky-sea-success-meditation-amazing-sunlight-sun-rays-zen-concept-beautiful-calm-139381803.jpg"
        ]
        for i,m in enumerate (self.mood):
            print (f"{i}) ({m})")
        choice = int (input("what kind of image would you like: "))
        if choice == 0:
            pathing = random.choice(funny)
        elif choice == 1:
            pathing = random.choice(motivational)
            self.ip = True
        else:
            print("ERR: please only select one of the available options")
            return 
        return pathing
