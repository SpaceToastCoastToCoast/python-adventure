import config

def entercave():
  print "The cave is dimly lit. You can barely make out the surface of the wall. There is a sconce where a torch was once lit, but it has calcified over from years of disuse."
  resp = raw_input("ACTION: ")
  if resp.lower().startswith("use"):
    used = resp.lower().strip("use ")
    success = config.useitem(used)
    if used == "torch":
      if success:
        print "The cave is illuminated."
        return cave_lit()
      else:
        print "You weren't prepared enough for this expedition. You have no torches. You turn back."
  elif resp.lower().startswith("list"):
    config.listinventory()
  return entercave()

def cave_lit():
  print "Now that the cave is lit, you can more clearly see its contents. A rusty knife rests on the cave floor."
  resp = raw_input("ACTION: ")
  if resp.lower().startswith("take"):
    print "You take the knife."
    config.additem("knife")
    return config.listinventory()
  elif resp.lower().startswith("list"):
    config.listinventory()
  return cave_lit()