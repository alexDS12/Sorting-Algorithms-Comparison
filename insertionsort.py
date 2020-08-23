def sort(numberlist):
  n = len(numberlist)
  for i in range(1, n):
    j = i
    value = numberlist[j]

    while j > 0 and numberlist[j] < numberlist[j-1]:
      numberlist[j], numberlist[j-1] = numberlist[j-1], numberlist[j]
      j -= 1
  
  return numberlist

def count_instructions(size):
  return 3 * (size ** 2) + 4 * size + 3