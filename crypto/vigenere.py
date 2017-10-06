from helpers import alphabet_position, rotate_character, is_upper_or_lower, is_upper, is_lower

def repeat_key(text,key):
    new_text_of_key = ''
    k = 0
    for i in range(len(text)):
        upper_lower = is_upper_or_lower(text[i])
        if k == (len(key)):
            k = 0
        if text[i] == " ":
            new_text_of_key += " "
        elif (not(upper_lower)): 
            new_text_of_key += text[i]
        else:
            new_text_of_key += key[k]
            k += 1

    return new_text_of_key



def encrypt(text,key):
    encryption_key = repeat_key(text,key)
    new_text = ''
    for char in range(len(text)):
        position = alphabet_position(encryption_key[char])

        new_text = new_text +  (rotate_character(text[char],position))
    return new_text

    
def main():
   # message = input("Enter a message:\n")
   # rotation = int(input("Rotate by:\n" ))
   # print(encrypt(message,rotation))

   st = 'Sailing <3 ships thru br0ken harbors'
   print(encrypt(st,"NeilYoung"))
   print(st)
   print(repeat_key(st,"NeilYoung"))
   
if __name__ == "__main__":
    main()
