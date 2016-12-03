import config

def entercave():
  print "The cave is dimly lit. You can barely make out the surface of the wall. There is a sconce where a torch was once lit, but it has calcified over from years of disuse."
  resp = raw_input("ACTION: ")
  success = config.take_action(resp, ["torch"])
  if resp.lower().startswith("use"):
    if success:
      print "The cave is illuminated."
      return cave_lit()
    else:
      print "You can't seem to understand the concept of a torch. You turn back."
      return
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