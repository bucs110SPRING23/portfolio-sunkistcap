import requests

class ipcheck:

    def __init__(self):
        '''
        obtains url to find IP
        '''
        self.url= "https://1.1.1.1/cdn-cgi/trace"

    def get(self):
        '''
        obtains neccessary info from the API
        return:
            ip (str): returns the ip line from the API
        '''
        url = self.url
        trace = requests.get(url)
        data = trace.text.split('\n')
        for line in data:
            if "ip=" in line:
                ip = line.strip()[3:]
                return ip