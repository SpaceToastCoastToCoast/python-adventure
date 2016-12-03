import level1,config

def intro():
  print """
  ################################
  #                              #
  #  ###  ###  #   # ##### ####  #
  # #    #   # #   # #     #   # #
  # #    #####  # #  ###   ####  #
  # #    #   #  # #  #     #   # #
  #  ### #   #   #   ##### #   # #
  #                              #
  #  A text adventure in Python  #
  ################################
  """
  resp = raw_input("Press Q to exit or press any other key to begin. ")
  if resp.lower().startswith("q"):
    return
  else:
    config.initgame()
    return startgame()

def startgame():
  print "\nLIST=list inventory\nGO=move in a direction\nTAKE=pick up item\nUSE=use item\nQUIT=exit game\n"
  print "You stand at the mouth of a large cave. What action will you take?"
  resp = raw_input("ACTION: ")
  if resp.lower().find("enter") != -1:
    print "You have entered the cave.\n"
    return level1.entercave()
  elif resp.lower().find("go in") != -1:
    print "You have entered the cave.\n"
    return level1.entercave()
  elif resp.lower().find("list") != -1:
    config.listinventory()
    return startgame()
  else:
    print "You decide to turn back, forgoing the possibility of adventure.\nAs you look back at the mouth of the cave, it seems to close behind you."

intro()