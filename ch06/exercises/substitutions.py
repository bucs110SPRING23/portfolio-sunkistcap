import json

file= open('news.txt', 'r')
sub=open("subs.json",'r')
rewrite= open('betternews.txt', 'w')
article = file.read()
subs = json.load(sub)
for key in subs:
    article = article.replace(key, subs[key])
rewrite.write(article)
file.close()
rewrite.close()
sub.close()