with open("Input.txt", "tr") as F:
    lines = F.read().splitlines()

type_ranking = {"5": 0, "4": 1, "FH": 2, "3": 3, "2P": 4, "1P": 5, "H": 6}
card_order = ["A", "K", "Q", "T"] + [str(x) for x in list(range(9, 1, -1))] + ["J"]

class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        hand_dict = {}
        joker_count = 0
        for char in hand:
            if char == "J":
                joker_count += 1
            elif char in hand_dict:
                hand_dict[char] += 1
            else:
                hand_dict[char] = 1
        match len(hand_dict), joker_count:
            case (0, _) | (1, _):
                self.type = "5"
            case (2, _):
                highest_val = max(hand_dict.values()) + joker_count
                if highest_val == 4:
                    self.type = "4"
                else:
                    self.type = "FH"
            case (3, 1) | (3, 2):
                self.type = "3"
            case (3, 0):
                for val in hand_dict.values():
                    if val + joker_count == 3:
                        self.type = "3"
                        break
                else:
                    self.type = "2P"
            case (4, _):
                self.type = "1P"
            case (5, _):
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