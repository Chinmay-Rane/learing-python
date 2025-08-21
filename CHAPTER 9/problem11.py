#rename a file


with open("CHAPTER 9/old.txt") as f:
    f.read()

with open("CHAPTER 9/renamed_new.txt","w") as f:
    f.write("")

#to delete the old txt file we need to use os or sh-util modules not taught yet 