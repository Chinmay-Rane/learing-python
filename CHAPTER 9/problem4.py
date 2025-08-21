#reads and censors the text donkey


word="Donkey"

with open("CHAPTER 9/censor.txt","r") as f:
    content=f.read()
    content=content.lower()


contentNew=content.replace(word.lower(),"######")

with open("CHAPTER 9/censor.txt","w") as f:
    f.write(contentNew)

print("The text has been censored")