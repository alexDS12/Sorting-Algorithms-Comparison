def sort(numberlist):
  n = len(numberlist)

  if n > 1:
    left = sort(numberlist[:n//2])
    right = sort(numberlist[n//2:])
    
    numberlist.clear()
    while len(left) > 0 and len(right) > 0:
      if left[0] > right[0]:
        numberlist.append(right[0])
        right.pop(0)

      else:
        numberlist.append(left[0])
        left.pop(0)
    
    for i in range(len(right)):
      numberlist.append(right[i])
    
    for i in range(len(left)):
      numberlist.append(left[i])
  
  return numberlist

def count_instructions(size):
  return 6 * size + 7