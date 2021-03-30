from sys import stdin


def ans(string):
  result = len(string)

  list_str=list(string)

  croatian_no_3char=['c=','c-','d-','lj','nj','s=','z=']

  i=0
  while i < len(string):
    if string[i:i+3] =='dz=':
      # string=string[:i]+'X'+string[i+3:]
      string='X'.join([string[:i],string[i+3:]])
      result-=2
      i=0
    else :
      i+=1

  
  result-=sum(string.count(x) for x in croatian_no_3char)

  print(result)

string = str(stdin.readline().rstrip('\n'))
ans(string)
