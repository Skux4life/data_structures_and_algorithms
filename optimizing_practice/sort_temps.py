def sort_temps(arr):
    """Temps can be between 97.0 and 99.0 degrees Fahrenheit (1 decimal place)
    O(N)"""

    temps = {}
    for temp in arr:
        if temps.get(temp):
            temps[temp] += 1
        else:
            temps[temp] = 1
    
    sorted_arr = []
    possible_temps = (x / 10 for x in range(970, 991))

    for num in possible_temps:
        print(num)
        if temps.get(num):
            for i in range(temps[num]):
                sorted_arr.append(num)

    return sorted_arr

def main():
    arr = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    print(sort_temps(arr))

if __name__ == '__main__':
    main()