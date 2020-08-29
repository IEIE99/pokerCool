# Dummy file to make this directory a package.

def Profit (WinRate, Buyin, Fee):

    
    return WinRate *(Buyin-Fee)- (1-WinRate)*Buyin



increment = 0.01
x=0
while x<1:
    x=x+increment
    print (int(x*100),Profit (x,3.5,0.18))#print(x+' '+Profit (x, 3.5, 0.18))
    #print (int(x*100),Profit (x,15,0.61))
