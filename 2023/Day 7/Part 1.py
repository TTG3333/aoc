with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

type_ranking = {"5": 0, "4": 1, "FH": 2, "3": 3, "2P": 4, "1P": 5, "H": 6}
card_order = ["A", "K", "Q", "J", "T"] + [str(x) for x in list(range(9, 1, -1))]

class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        hand_dict = {}
        for char in hand:
            if char in hand_dict:
                hand_dict[char] += 1
            else:
                hand_dict[char] = 1
        match len(hand_dict):
            case 1:
                self.type = "5"
            case 2:
                first_val = list(hand_dict.values())[0]
                if first_val == 1 or first_val == 4:
                    self.type = "4"
                else:
                    self.type = "FH"
            case 3:
                for val in hand_dict.values():
                    if val == 3:
                        self.type = "3"
                        break
                else:
                    self.type = "2P"
            case 4:
                self.type = "1P"
            case 5:
                self.type = "H"
        self.type_ranking = type_ranking[self.type]
        self.converted_hand = [card_order.index(char) for char in hand]
    
    def __eq__(self, other):
        if type(other) == type(self):
            return self.hand == other.hand
        else:
            return NotImplemented
    
    def __ne__(self, other):
        if type(other) == type(self):
            return self.hand != other.hand
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if type(other) == type(self):
            if self.type_ranking == other.type_ranking:
                return other.converted_hand < self.converted_hand
            else:
                return self.type_ranking > other.type_ranking
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if type(other) == type(self):
            if self.type_ranking == other.type_ranking:
                return other.converted_hand > self.converted_hand
            else:
                return self.type_ranking < other.type_ranking
        else:
            return NotImplemented
    
    def __str__(self):
        return f"{self.hand} {self.bid}"
    
    def __repr__(self):
        return f"Hand({repr(self.hand)}, {self.bid})"

hands = []
for line in lines:
    hand, bid = line.split(" ")
    bid = int(bid)
    hands.append(Hand(hand, bid))

hands = sorted(hands)

print(sum([(i+1)*x.bid for i, x in enumerate(hands)]))