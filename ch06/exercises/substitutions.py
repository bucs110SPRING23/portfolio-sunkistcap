import json

with open ('subs.json','r') as sub_file, open('news.txt','r',encoding='utf-8') as old_file:
    article = old_file.read()
    subs=json.load(sub_file)
    for old_word,new_word in subs.items():
        article= article.replace(old_word, new_word)
    with open ('betternews.txt',"w") as new_file:
        new_file.write(article)
sub_file.close()
old_file.close()
new_file.close()