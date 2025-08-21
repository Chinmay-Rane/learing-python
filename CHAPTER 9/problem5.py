#problem 4 but with list of words

words=["Donkey","bad","mango"]

with open("CHAPTER 9/censor2.txt","r") as f:
    content=f.read()
    content=content.lower()

for word in words:
    content=content.replace(word.lower(),"#"*len(word))

with open("CHAPTER 9/censor2.txt","w") as f:
    f.write(content)

print("The text has been censored")