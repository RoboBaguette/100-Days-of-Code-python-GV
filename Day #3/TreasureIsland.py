"""
Treasure island is a maze that the user has to navigate
by inputing left or right
if the user enter the right combination they reach the end of the maze
"""
print("welcome to Treasure island.")
a= input('enter "left" or "right"\n')
if a=="left":
  b = input('enter "left" or "right"\n')
  if b=="left":
    c= print('you have reached the end, game has ended')
  elif b=="right":
    c= print('you died, game has ended')
elif a=="right":
  b= input('enter "left" or "right"\n')
  if b=="left":
    c= print('you died, game has ended')
  elif b=="right":
    c= print('you died, game has ended')

