import random


possible_colors = ["Blue", "Brown", "Black", "Green", "Grey"]
class GameObject:
    def __init__(self, name, color):
        self.name = name
        self.color = color

def get_Perfect_objects():
    objects = [
        GameObject("Water tank", "Blue"),
        GameObject("Plant", "Brown"),
        GameObject("Tire", "Black"),
        GameObject("Bottle", "Green"),
        GameObject("Trash can", "Grey")
    ]
    return objects

def removeObject(list, object):
    list_updated = []
    for object_ in list:
        if object.name != object_.name:
            list_updated.append(object_)
    return list_updated

def generate_deck_unperfect_deck():
    deck = []
    possible_objects = get_Perfect_objects()
    for object in possible_objects:
        list_of_secondary_objects = get_Perfect_objects()
        list_of_secondary_objects = removeObject(list_of_secondary_objects, object)
        for second_object in list_of_secondary_objects:
            print(f'{object.name} {object.color}')
            list_of_secondary_objects_redux = removeObject(list_of_secondary_objects, second_object)
            for item in list_of_secondary_objects_redux:
                quartenary_list = removeObject(list_of_secondary_objects_redux, item)
                for quartenary_item in quartenary_list:
                    firstObject = GameObject(object.name, second_object.color)
                    newObejct = GameObject(item.name , quartenary_item.color)
                    deck.append([
                        firstObject,
                        newObejct
                    ])
    return deck

def generate_deck_perfect_deck():
    deck = []
    possible_objects = get_Perfect_objects()
    for object in possible_objects:
        list_of_secondary_objects = get_Perfect_objects()
        list_of_secondary_objects = removeObject(list_of_secondary_objects, object)
        for second_object in list_of_secondary_objects:
            print(f'{object.name} {object.color}')
            list_of_secondary_objects_redux = removeObject(list_of_secondary_objects, second_object)
            for item in list_of_secondary_objects_redux:
                quartenary_list = removeObject(list_of_secondary_objects_redux, item)
                for quartenary_item in quartenary_list:
                    newObejct = GameObject(item.name , quartenary_item.color)
                    print(f"Card: {object.name} ({object.color}) - {newObejct.name} ({newObejct.color})")
                    deck.append([
                        object,
                        newObejct
                    ])
    return deck

def remove_duplicate_cards(deck):
    seen_cards = set()
    unique_deck = []

    for card in deck:
        sorted_card = tuple(sorted(((card[0].name, card[0].color), (card[1].name, card[1].color))))
        if sorted_card not in seen_cards:
            seen_cards.add(sorted_card)
            unique_deck.append(card)

    return unique_deck

def main():
    objects = get_Perfect_objects()
    deck_unperfect = generate_deck_unperfect_deck()
    deck_perfect = generate_deck_perfect_deck()
    deck_perfect = remove_duplicate_cards(deck_perfect)
    deck = remove_duplicate_cards(deck_unperfect)

    # the perfect deck is all the cards where there is a object witha correct color
    # the unperfect deck is all the cards that doesn't have a perfect object, thus -> the correct object is the one that' is not there.
    print(len(deck_perfect))
    print(len(deck))

    print("Object Colors:")
    for obj in objects:
        print(f"{obj.name}: {obj.color}")

    print("\nGenerated Perfect Card Deck:")
    for card in deck_perfect:
        if card[0].color != card[1].color:
            print(f"Card: {card[0].name} ({card[0].color}) - {card[1].name} ({card[1].color})")

    print("\nGenerated UN-Perfect Card Deck:")
    for card in deck:
        if card[0].color != card[1].color:
            print(f"Card: {card[0].name} ({card[0].color}) - {card[1].name} ({card[1].color})")

if __name__ == "__main__":
    main()
