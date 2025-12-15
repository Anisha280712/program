str=input("enter the word:")
char=input("enter the character who's occurence you want to know:")
i=0
count=0
while(i<len(str)):
    if (str[i]==char):
        count=count+1
    i=i+1
print("total number of time character occured:",count)