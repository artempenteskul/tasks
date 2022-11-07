def count_highest_earnings(fights_earnings: list):
    
    if len(fights_earnings) == 0:
        return 0
    
    if len(fights_earnings) == 1:
        return fights_earnings[0]

    earnings = 0
    while len(fights_earnings) != 0:
        match1_earnings = fights_earnings.pop(0)
        match2_earnings = fights_earnings.pop(0)
        earnings += max(match1_earnings, match2_earnings)
    
    return earnings


if __name__ == '__main__':
    matches_prices = [1, 2, 4, 5, 56, 6]
    print(count_highest_earnings(matches_prices))
