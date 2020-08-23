def sort(numberlist):
  n = len(numberlist)

  swap = True
  while swap:
    swap = False

    for i in range(n-1):
      if(numberlist[i] > numberlist[i+1]):
        swap = True
        numberlist[i], numberlist[i+1] = numberlist[i+1], numberlist[i]

    if not swap:
      break

    swap = False

    for i in range(n-2, -1, -1):
      if(numberlist[i] > numberlist[i+1]):
        swap = True
        numberlist[i], numberlist[i+1] = numberlist[i+1], numberlist[i]
    
  return numberlist

def count_instructions(size):
  return 10 * (size ** 2) + 2 * size + 4