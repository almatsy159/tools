s1 = "hi guys, i'm just trying to put those words in an array"

def put_in_array(sentence):
    x=0
    a1=[]
    for i in range(len(sentence)):
        if sentence[i] == " ":
            a1.append(sentence[x:i])
            x = i +1
        elif i == len(sentence)-1:
            a1.append(sentence[x:])
            #print(x)
    return a1

a=put_in_array(s1)
print(a,": size = ",len(a))
#print(a1[5])
