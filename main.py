N = [3, 1, 6, 8 ,9, -1, 1, 0, 19]
 
i = 1
 
while i < len(N):
  if N[i-1] < N[i]: i+= 1
  else: N.remove(N[i])
 
print(N)