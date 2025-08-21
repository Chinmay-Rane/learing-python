#program to find identical files

with open("CHAPTER 9/this.txt") as f:
    content1=f.read()

with open("CHAPTER 9/this_copy.txt") as f:
    content2=f.read()

if (content1==content2):
    print("Content is identical")
else:
    print("Content is not identical")

