
from Deck import Deck
def main():
    #creating deck
    deck = Deck()

    #test shuffling
    deck.shuffle()
    print("Shuffling again")
    deck.shuffle()
    deck.printCards()
    print ("Card Total:"+ str(deck.cards.__len__()))

    # test drawing 
    card  = deck.draw();
    print ("Draw card "+ card.print() )
    card  = deck.draw();
    print ("Draw card "+ card.print() )
    card  = deck.draw();
    print ("Draw card "+ card.print() )



if __name__ == '__main__':
    main()  