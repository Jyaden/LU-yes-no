show_instructions = ""
while show_instructions.lower() != "stop":

    show_instructions = input("Have you played this game before? ").lower() 

    # If they say yes, output 'program continues'
    #Answer Yes
    if show_instructions =="yes" or show_instructions == "y":
      print("program continues")

    # Answer No
    elif show_instructions == "no" or show_instructions == "n":
      print("display instructions")


    # If they say no, output "display instructions"
    else:
      print("Please answer yes/no")
    
