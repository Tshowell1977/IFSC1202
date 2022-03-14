N=int(input("Enter Month: "))
D=int(input("Enter Day: "))
#if N==2:
 #   x=28
#if N==4 or N==6 or N==9 or N==11:
 #   x=30
#if N==1 or N==3 or N==5 or N==7 or N==8 or N==10 or N==12:
 #   x=31
if N==2 and D<=27:
    nd=D+1
    P=N
if N==2 and D==28:
    nd=1 
    P=N+1
if N==4 and D==30 or N==6 and D==30 or N==9 and D==30 or N==11 and D==30:
    nd=1 
    P=N+1
if N==4 and D<=29 or N==6 and D<=29 or N==9 and D<=29 or N==11 and D<=29:
    nd=D+1
    P=N
if N==1 and D==31 or N==3 and D==31 or N==5 and D==31 or N==7 and D==31 or N==8 and D==31 or N==10 and D==31 or N==12 and D==31:
    nd=1
    P=N+1
    if P>=13:
        P=1
if N==1 and D<=30 or N==3 and D<=30 or N==5 and D<=30 or N==7 and D<=30 or N==8 and D<=30 or N==10 and D<=30 or N==12 and D<=30:
    nd=D+1
    P=N
print("Next Day: "+str(P)+"/"+str(nd))