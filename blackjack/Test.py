
from Deck import Deck
def main():
    #creating deck
    deck = Deck()

    #test shuffling
    deck.shuffle()
    print("Shuffling again")
    deck.shuffle()
    for card in deck.cards:
        print (card.image)
    print ("Card Total:"+ str(deck.cards.__len__()))

    # test drawing 
    card  = deck.draw();
    print ("Draw card "+ card.image )
    card  = deck.draw();
    print ("Draw card "+ card.image )
    card  = deck.draw();
    print ("Draw card "+ card.image )



if __name__ == '__main__':
    main()  