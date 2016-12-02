inventory = []

def initgame():
  global inventory
  torches = ["torch", "torch", "torch"]
  inventory.append(torches)

def listinventory():
  for item in inventory:
    print item[0] + " x" + str(len(item))

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