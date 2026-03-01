# spam words detection
word1 = "Make a lot of money"
word2 = "buy now"
word3 = "subscribe"
word4 = "click this"

comment = str(input("Enter your comment:- "))
if((word1 in comment) or (word2 in comment) or (word3 in comment) or (word4 in comment)):
    print("This is an scam comment, pls do not click on spam links or do anything.")
else:
    print("This is not an scam")


# Hi , I am Manpreet KAur , pls reach out to me for learning online money , for this click this - www.mnsnb.com
# Hi , I am Manpreet KAur , pls reach out to me for learning online money , for this "Make a lot of money" on our site - www.mnsnb.com