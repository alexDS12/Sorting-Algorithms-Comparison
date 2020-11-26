def sort(numberlist):
  n = len(numberlist)
  result = []
  
  if n > 1:
    left = sort(numberlist[:n//2])
    right = sort(numberlist[n//2:])
    
    while len(left) > 0 and len(right) > 0:
      if left[0] > right[0]:
        result.append(right[0])
        right.pop(0)

      else:
        result.append(left[0])
        left.pop(0)
    
    for i in range(len(right)):
      result.append(right[i])
    
    for i in range(len(left)):
      result.append(left[i])
  
  return result

def count_instructions(size):
  return 6 * size + 7