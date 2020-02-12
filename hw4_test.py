import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        c1 = cards.Card(1, 12)
        self.assertEqual(c1.rank, 12)
        self.assertEqual(c1.rank_name, "Queen")

    def test_2_clubs(self):
        c2 = cards.Card(1, 1)
        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")

    def test_3_str(self):
        c3 = cards.Card(3, 13)
        self.assertEqual(c3.__str__(), "King of Spades")

    def test_4_deck(self):
        c4 = cards.Deck()
        self.assertEqual(len(set(c4.cards)), 52)

    def test_5_deal(self):
        c5 = cards.Deck()
        dealt_card = c5.deal_card()
        self.assertTrue(isinstance(dealt_card, cards.Card))

    def test_6_afterdeal(self):        
        c6 = cards.Deck()
        dealt_card = c6.deal_card()
        self.assertEqual(len(set(c6.cards)), 51)

    def test_7_replace(self):
        c7 = cards.Deck()
        dealt_card = c7.deal_card()
        c7_afterdeal = len(set(c7.cards))
        c7.replace_card(dealt_card)
        c7_afterrepalce = len(set(c7.cards))
        self.assertEqual(c7_afterrepalce - c7_afterdeal, 1)

    def test_8_notaffected(self):
        c8 = cards.Deck()
        dealt_card = c8.deal_card()
        c8.replace_card(dealt_card)
        c8_first_replace = len(set(c8.cards))
        self.assertEqual(c8_first_replace, 52)
        c8.replace_card(dealt_card)
        c8_second_replace = len(set(c8.cards))
        self.assertEqual(c8_second_replace, 52)

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
