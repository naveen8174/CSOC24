import random
chamber=int(input("enter no.of chambers in the roulette: "))

def load():
  bullet=int(input("load bullet at: "))
  return bullet
def fire():
  die_at=random.randint(1,chamber)
  return die_at
bullet_at=1
while True:
  print("1.load your gun \n2.fire the gun\nother.exit\n")
  opt=int(input("enter the option: "))
  if opt==1:
    bullet_at=load()
  elif opt==2:
    fire_at=fire()
    if fire_at==bullet_at:
      print("you are dead")
    else:
      print("better die next time;)")
  else :
    print("enter valid input!!")