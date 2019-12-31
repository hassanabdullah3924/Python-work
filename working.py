name = input("What is your name? ")
print("Okay", name,"here's the deal sparky")
print("This is your chance to win a grand prize")
chance = 3
print("You have", chance, "chances")
i = ""
name1 = "Write the correct name and win!\n"

while(i != "Joe"):
    i=input(name1) 
    if(i == "Joe"):
        print("You have won")
        else(i != "Joe"):
            chance1= chance - 1
            print("Please try again")
            print("You have", chance1, "chances left")
            i=input(name1)
            else(i != "Joe"):
                chance2 = chance1 - 1
                print("Please try again")
                print("You have", chance2, "chances left")
                i=input(name1)
                else(i != "Joe"):
                    chance3= chance2 - 1
                    print("You have", chance3, "chances left")
                    print("Sorry you have run out of tries, the correct name was Joe Mr.", name)
                    
    
                
                    

                        
                            
                            
                            
                    
    
                

            


    
    