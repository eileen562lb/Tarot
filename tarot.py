import sys
import json
import random
import time

deck = json.load(open('deck.json'))
positions = json.load(open('positions.json'))

# ask for an something but print it slowly
def typewriter_input(text):
    for n in range(0,len(text)):
        time.sleep(0.04)
        sys.stdout.write(text[n])
        sys.stdout.flush()
    return input("")

# print a message with some drama
def typewriter_print(text):
    for n in range(0,len(text)):
        time.sleep(0.04)
        sys.stdout.write(text[n])
    print("")

def typewriter_print_slower(name, text):
    for n in range(0,len(name)):
        time.sleep(0.04)
        sys.stdout.write(name[n])
    for n in range(0,len(text)):
        if text[n] == " " or text[n] == ".":
            time.sleep(0.1)
        else:
            time.sleep(0.07)
        sys.stdout.write(text[n])
    print("")
    
    
def main():
    intro()
    name = ask_name()
    reading = ask_reading(name)
    deck = shuffle_cards()
    is_first_card = True
    for position in positions:
        card = deck.pop()
        is_reversed = random.randint(0,1) == 1
        
        if not is_first_card:
            time.sleep(4)
            
        # make sure thecode above only happens after the first card
        is_first_card = False
        
        read_card(name, position, card, is_reversed)
    ending()
        

# use random to randomize
def shuffle_cards():
    typewriter_print("[ The psychic begins to shuffle the cards ]")
    typewriter_print("Miracle: Remember,")
    typewriter_print("Miracle: These are the readings of the card")
    typewriter_print("Miracle: and just like the future")
    typewriter_print("Miracle: the cards may surprise us")
    typewriter_print("Miracle: and tell us things")
    typewriter_print("Miracle: that we're not ready for.")
    print("")
    typewriter_input("[ Press enter to continue. ]")
    random.shuffle(deck)
    return deck

# read a card
def read_card(name, position, card, is_reversed):
    # the psychic speaks
    typewriter_print("[ She flips the " + position['position'] + " card, looking at it for a few moments before she continues the reading ]")
    print("")
    typewriter_print("Miracle: " + name + ", this card is " + card['name'] + ".")
    print("")
    typewriter_print("[ The psychic waves her hand over the card, and puts one finger on the card. ]")
    print("")
    if is_reversed:
        typewriter_print("Miracle: It's reversed.")
        time.sleep(2)
        print("")
        typewriter_print("Miracle: " + card['reverse'])
    else:
        typewriter_print("Miracle: It's upright.")
        time.sleep(2)
        print("")
        typewriter_print("Miracle: " + card['upright'])
    
    print("")
    typewriter_print("Miracle: " + position['description'])
    time.sleep(7)

    print("")

# she needs to introduce herself
def intro():
    typewriter_print("[ Your friend suggested that you go to the psychic on fifth avenue. ]")
    typewriter_print("[ You're here now, in her condo. ]")
    typewriter_print("[ You're sitting in a brightly lit room, on a dark rainy night. ]")
    typewriter_print("[ She begins to speak ]")
    print("")
    typewriter_print("The Psychic: Hello.")
    typewriter_print("The Psychic: My real name is Maria, but everyone calls me Miracle.")
    print("")
    typewriter_print("Miracle: If there's something on your mind,")
    typewriter_print("Miracle: something you need read from the cards,")
    print("")
    typewriter_print("Miracle: I can provide you a reading")
    time.sleep(1)
    print("")
    typewriter_print("Miracle: But remember,")
    time.sleep(1)
    print("")
    
    typewriter_print("Miracle: These are the readings of the card")
    typewriter_print("Miracle: and just like the future")
    typewriter_print("Miracle: the cards may surprise us")
    typewriter_print("Miracle: and tell us things")
    typewriter_print("Miracle: that we're not ready for.")


# give her a theatrical exit
def ending():
    typewriter_print("[ She collects each of the cards into her hand. ]")
    print("")
    
    typewriter_print("[ She places them on top of he deck, ]")
    typewriter_print("[ and places the deck inside of an old wooden box ]")
    time.sleep(3)
    print("")
    
    typewriter_print("[ You feel restless, and you look down at your phone ]")
    time.sleep(5)
    print("")
    
    typewriter_print("[ You hear a cat meow at your side ]")
    typewriter_print("[ and feel something soft brush against your leg. ]")
    print("")
    
    typewriter_print("[ Just as you look up from your phone ]")
    time.sleep(2)
    print("")
    
    typewriter_print("[ Miracle has vanished ]")
    time.sleep(1)
    typewriter_print("[ and the rain has stopped ]")
    time.sleep(2)
    print("")
    typewriter_print("[ You call out for the psychic, but she cannot be found. ]")
    typewriter_print("[ After waiting for a few minutes, you find your way towards the exit. ]")
    time.sleep(2)
    print("")
    typewriter_print("[ You lock the door on your way out. ]")
    time.sleep(2)
    print("")
    typewriter_print("[ You step into the future. ]")
    time.sleep(2)
    print("")
    typewriter_print("[ The future the cards had set for you. ]")
    print("")
    typewriter_print("[ Later that night, as you're sitting in bed, ]")
    typewriter_print("[ just as you're falling asleep, you hear a voice. ]")
    print("")
    
    typewriter_print_slower("Miracle:", " If there's something on your mind, ...")
    typewriter_print_slower("Miracle:", " something you need read from the cards, ...")
    typewriter_print_slower("Miracle:", " I can provide you a reading...")
    time.sleep(2)
    print("")
    
    typewriter_print_slower("Miracle:", " But remember, ...")
    time.sleep(3)
    print("")
    
    typewriter_print_slower("Miracle:", " These are the readings of the card ...")
    typewriter_print_slower("Miracle:", " and just like the future ...")
    typewriter_print_slower("Miracle:", " the cards may surprise us ...")
    typewriter_print_slower("Miracle:", " and tell us things ...")
    typewriter_print_slower("Miracle:", " that we're not ready for...")
    time.sleep(2)
    print("")
    print("[ End ]")
    


#she wants to know your name
def ask_name():
    return typewriter_input("Miracle: What is your name? ")

#ask for what the eading is about
def ask_reading(name):
    typewriter_print("Miracle: Hello, " + name + ", What is this reading about?")
    print("")
    typewriter_print("Miracle: Please be specific.")
    
    return typewriter_input("You: This reading is about: ")
if __name__ == "__main__":
    main()