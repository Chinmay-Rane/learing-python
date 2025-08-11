#detect spam
p1="Make a lot of money"
p2="click this"
p3="subscribe this"
p4="buy now"


message=input("Enter your comment: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("This comments is a spam")
else:
    print("This comments is not a spam")
    