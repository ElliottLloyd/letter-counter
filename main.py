def letterFrequency(fileName, letter):
    file = open(fileName, 'r')
    text = file.read()
    return text.count(letter)

file = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","-",",","'",".","/",]

for character in file:
    print ("the character '",character, "' appears",letterFrequency('task-3-words.txt', character),"times")
