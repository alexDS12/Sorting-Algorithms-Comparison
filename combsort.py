def sort(numberlist):
  n = len(numberlist)
  gap = n

  swap = True
  while swap or gap > 1:
    swap = False
    gap = int(gap / 1.3)

    for i in range(n-gap):
      if numberlist[i] > numberlist[i+gap]:
        swap = True
        numberlist[i], numberlist[i+gap] = numberlist[i+gap], numberlist[i]

  return numberlist

def count_instructions(size):
  return 4 * (size ** 2) + 2 * size + 5