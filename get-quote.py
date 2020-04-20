def primary():

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    for i in quotes:
        print(i)
    
if __name__== "__main__":
  primary()
