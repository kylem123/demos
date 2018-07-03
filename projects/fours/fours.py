import random


class Fours(object):
    def __init__(self):
        self.board = [[], [], [], []]
        self.deck = Deck()
        self.deck.shuffle()
        self.final_cards = None

    def __repr__(self):
        biggest = max([len(thing) for thing in self.board])
        out = ""
        for x in range(biggest):
            out += "| "
            for y in self.board:
                try:
                    out += "%s | " % str(y[x])
                except IndexError:
                    out += "     | "
            out += "\n"
        return out

    def count_game(self):
        self.final_cards = sum([len(thing) for thing in self.board])

    def draw_card(self):
        try:
            for stack in self.board:
                stack.append(self.deck.draw())
            self.count_game()
            return self
        except OutOfCards:
            self.count_game()
            return self.final_cards

    def clear_card(self, column):
        for thing in self.board:
            if thing != []:
                if thing[-1:][0].value > self.board[column][-1:][0].value \
                        and thing[-1:][0].suit == self.board[column][-1:][0].suit:
                        self.board[column].pop()
                        self.count_game()
                        return self
        return False

    def move_card(self, start, end):
        if self.board[end] == [] and self.board[start] != []:
            self.board[end].append(self.board[start].pop())
            return self
        else:
            return False


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __repr__(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if self.suit == "Spades":
            pic = u"♠"
        elif self.suit == "Hearts":
            pic = u"♥"
        elif self.suit == "Diamonds":
            pic = u"♦"
        elif self.suit == "Clubs":
            pic = u"♣"
        else:
            raise ValueError  # Invalid suit

        if self.value == 8:
            return "%s %s" % (values[self.value], pic)
        else:
            return "%s  %s" % (values[self.value], pic)

    def __hash__(self):
        return ("%s:%s" % (self.suit, self.value)).__hash__()


class Deck(object):
    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        self.cards = []
        for suit in suits:
            self.cards += [Card(suit, value) for value in range(13)]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise OutOfCards()


class OutOfCards(Exception):
    pass
