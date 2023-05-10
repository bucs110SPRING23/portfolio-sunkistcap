import requests

class JokeGen:
    def __init__(self):
        '''
        initizalies url that will be made within get method
        '''
        self.url = "https://random-stuff-api.p.rapidapi.com/joke/puns"
        self.headers = {
        "Authorization": "fNeIOlZkVgW2",
        "X-RapidAPI-Key": "e4559b15fcmshbbcc465f05bd11fp1799d7jsn722eb9035409",
        "X-RapidAPI-Host": "random-stuff-api.p.rapidapi.com"
    }
        self.querystring = {"exclude":"sex"}

    def get(self):
        '''
        used to obtain joke to be used within imagegenerator file
        return:
            joke(str): returns one randomly chosen joke from API
        '''
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        joke = response.json()["message"]
        return (joke)