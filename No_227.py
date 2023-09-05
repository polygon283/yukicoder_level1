def count_cards(cards):
    card_count = {}
    
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] =1
    return card_count

def check_cards(cards):
    card_count = count_cards(cards)
    counts = list(card_count.values())
    
    if counts.count(3) == 1 and counts.count(2) == 1:
        return "FULL HOUSE"
    if counts.count(3) == 1:
        return "THREE CARD"
    if counts.count(2) == 2:
        return "TWO PAIR"
    if counts.count(2) == 1:
        return "ONE PAIR"
    else:
        return "NO HAND"



        

input_card = input()
split_card = input_card.split()
cards = []
for card in split_card:
    cards.append(int(card))
result = check_cards(cards)
print(result)
