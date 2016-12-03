inventory = []

def initgame():
  global inventory
  torches = ["torch", "torch", "torch"]
  inventory.append(torches)

def listinventory():
  print "[INVENTORY]\n"
  for item in inventory:
    print item[0] + " x" + str(len(item))
  print " "

def useitem(item):
  found = False
  for entry in inventory:
    if item in entry:
      entry.pop()
      if len(entry) < 1:
        inventory.pop(inventory.index(entry))
      found = True
      print "You used the " + str(item) + "."
      break
  if not found:
    print "You don't have any " + str(item) + " to use."
  return found

def additem(item):
  global inventory
  newentry = []
  newentry.append(item.lower())
  inventory.append(newentry)
  print "The " + item.lower() + " was added to your inventory."

#This function serves as input validation for the game.
def take_action(useraction, valid_args):
  action = useraction.lower()
  if action.startswith("go"):
    place = action.replace("go ", "")
    if place in valid_args:
      return True
    else:
      print str(place) + " isn't a destination."
      return False
  elif action.startswith("list"):
    listinventory()
    return True
  elif action.startswith("use"):
    used = action.replace("use ", "")
    if used in valid_args:
      return useitem(used)
    else:
      print str(used) + " can't be used here."
      return False
  elif action.startswith("take"):
    taken = action.replace("take ", "")
    if taken in valid_args:
      additem(taken)
      return True
    else:
      print str(taken) + " can't be taken with you."
      return False
  elif action in ["leave", "quit", "exit"]:
    raise SystemExit
  else:
    print "That action can't be done."