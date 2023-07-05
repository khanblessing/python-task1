menbers = ["Neolla", "Melvis", "Goodness", "Joy", "Mark"]
menbers.insert(0, "Godwill")
menbers.append( "Fadila")
menbers.insert(3, "Bella") #print actual middle item by dividing the list size by 2 even list, for odd list, use math.floor + 1;
print(menbers)
guest = ["Reymond", "Jeff", "Louis"]
print(guest) 
for i in range(len(menbers)):
    print(f"""
Hello {menbers[i]}
           I have found a biger dinner table"""
)
