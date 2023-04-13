def players_who_play_both_sports(arr1, arr2):
    """Find players who exist in both arrays and return in an array, O(N + M)"""

    result = []
    sport1_players = {}
    for player in arr1:
        full_name = f"{player['first_name']} {player['last_name']}"
        sport1_players[full_name] = True

    for player in arr2:
        full_name = f"{player['first_name']} {player['last_name']}"
        if sport1_players.get(full_name):
            result.append(full_name)
    
    return result

def main():
    basketball_players = [
        { 'first_name': "Jill", 'last_name': 'Huang', 'team': 'Gators' },
        { 'first_name': 'Janko', 'last_name': 'Barton', 'team': 'Sharks' },
        { 'first_name': 'Wanda', 'last_name': 'Vakulskas', 'team': 'Sharks' },
        { 'first_name': 'Jill', 'last_name': 'Maloney', 'team': 'Gators' },
        { 'first_name': 'Luuk', 'last_name': 'Watkins', 'team': 'Gators' },
    ]

    football_players = [
        { 'first_name': 'Hanzla', 'last_name': 'Radosti', 'team': '32ers' },
        { 'first_name': 'Tina', 'last_name': 'Watkins', 'team': 'Barleycorns' },
        { 'first_name': 'Alex', 'last_name': 'Patel', 'team': '32ers' },
        { 'first_name': 'Jill', 'last_name': 'Huang', 'team': 'Barleycorns' },
        { 'first_name': 'Wanda', 'last_name': 'Vakulskas', 'team': 'Barleycorns' },
    ]

    print(players_who_play_both_sports(basketball_players, football_players))

if __name__ == '__main__':
    main()