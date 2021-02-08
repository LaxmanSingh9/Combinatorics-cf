#longest prefix with same chracter=>cntl
#longest suffix with same charcter=>cntr
#there will be two cases
 #for exact two charcter=>
 #for more than two charcter

n=int(input());s=input();cntl,cntr=0,0
for i in range(n):
 if s[0]==s[i]:cntl+=1
 else:break
for i in range(n-1,-1,-1):
  if s[n-1]==s[i]:cntr+=1
  else:break
if s[0]==s[n-1]:print((cntl+1)*(cntr+1)%998244353 )
else:print((cntl+cntr+1)%998244353 )
