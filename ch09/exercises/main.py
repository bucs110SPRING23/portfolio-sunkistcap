# Network programming

# Build any porgram that asks trivia questions

# Server: any computer listening for incoming network connections

# Request: a incoming conneciton that asks for some resource from the server

# - Images, Videos, Music
# - Text
# - JSON 
# - HTML

# Types of Requests

# - GET - read operation 
# visiting, downloading a file , etc.
# - PUT - write operation (requires security)
# login, deleting , etc

# Headers
# sent with request and the response

# - status codes:
#   - 200: ok, everything went fine
#   - 400: resource cannot be delivered
#   - 500: bad code server
# - ip address
# - system information (geolocation)

## urllib

# Requests

# API - Application Programmer's interface
# APIS can return data in any formate,
# usually returned in JSON

#URL Parameters

# ?, &

# binghamton.edu/cs?var1=100&var2="Hello"

import requests
import random

class TriviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=2&category=18"

    def get(self):
        #function can be named data / get
        url = self.url + self.varstr
        response = requests.get(url)
        data = response.json()
        return data ['results']

    def csquestions(self):
        self.varstr = "amount=2&category=18"
        return self.get()
    
    def general(self):
        self.varstr = "amount=2"
        return self.get()



def main():
    tp = TriviaProxyAPI()
    results = tp.csquestions()

    for r  in results:
        print(r['question'])
        possibles = [r["correct_answer"], *r["incorrect_answers"]]
        random.shuffle(possibles)
        print("Make your selection:")
        for i, p in enumerate(possibles):
            print(f"{i}) ({p})")
        
        selection = int(input(": "))
        if possibles[selection] == r["correct_answer"]:
            print("You are correct")
        else:
            print (f"Study!!!!, the right answer is: {r['correct_answer']}")

    results = tp.general()
if __name__ == main():
    main()