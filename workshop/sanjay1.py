def f(n):
  a=1
  while(n>1):
      f=f*a
      n=n-1
  print(n)
  f(10)