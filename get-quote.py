import random

def primary():
  # open the quotes.txt file and
  # run the read().splitlines() to fetch data
  # and remove any newlines
  f = open("quotes.txt")
  quotes = f.read().splitlines()
  f.close()
  
  # set up process to generate a random integer
  # within the range of the list index, to return that index
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd], quotes[rnd - 1], end = "")

  # ask the user if they would like to append a quote
  ans = input("\nwould you like to add a quote? (y/n)")

  if ans == "y":
    text = input("enter your text: ")
    # open the quotes.txt file but
    # this time, append a quote
    f = open("quotes.txt", "a")
    f.write(text + "\n")
    f.close()
  elif ans == "n":
    print("Okay! Exiting..")

if __name__== "__main__":
  primary()
