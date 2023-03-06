userInput=input("triangle or rectangle ? : ")
if(userInput=="triangle"):
    edge1=abs(int(input("edge 1 : ")))
    edge2=abs(int(input("edge 2 : ")))
    edge3=abs(int(input("edge 3 : ")))
    if((edge1+edge2)>edge3 and (edge2+edge3)>edge1 and (edge3+edge1)>edge2):
        if(edge1==edge2==edge3):
            print("equilateral triangle")
        elif(edge1==edge2 or edge2==edge3 or edge3==edge1):
            print("twin-edged triangle")
        else:
            print("normal triangle")
    else:
        print("it is not a triangle")
    
elif(userInput=="rectangle"):
    edge1=abs(int(input("edge 1 : ")))
    edge2=abs(int(input("edge 2 : ")))
    edge3=abs(int(input("edge 3 : ")))
    edge4=abs(int(input("edge 4 : ")))
    if(edge1==edge2==edge3==edge4):
        print("square rectangle")
    elif((edge1==edge2 and edge3==edge4)or(edge2==edge3 and edge1==edge4)or(edge1==edge3 and edge2==edge4)):
        print("oblong rectangle")
    else:
        print("normal rectangle")
else:
    print("wrong input!")