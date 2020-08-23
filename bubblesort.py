def sort(numberlist):
  n = len(numberlist)                                             
  for i in range(1, n):                        
    for j in range(n-1):                        
      if numberlist[j] > numberlist[j+1]:
        numberlist[j], numberlist[j+1] = numberlist[j+1], numberlist[j] 

  return numberlist

def count_instructions(size):
  return 3 * (size ** 2) + 2 * size