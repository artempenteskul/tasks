# task number - 649


def predict_party_victory(senate: str) -> str:
    radiant = []
    dire = []

    senate_qty = len(senate)

    for i in range(senate_qty):
        if senate[i] == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        radiant_turn = radiant.pop(0)
        dire_turn = dire.pop(0)

        if radiant_turn < dire_turn:
            radiant.append(radiant_turn + senate_qty)
        else:
            dire.append(dire_turn + senate_qty)

    return 'Radiant' if radiant else 'Dire'


if __name__ == '__main__':
    input_senate = 'RD'
    print(f'Party victory prediction for input senate - {predict_party_victory(input_senate)}')  # Radiant

    input_senate = 'RDD'
    print(f'Party victory prediction for input senate - {predict_party_victory(input_senate)}')  # Dire
