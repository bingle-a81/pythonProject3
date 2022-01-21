# -*- coding: utf-8 -*-
def binarySearch(List, Start, End, Number):
    if List[Start] == Number:
        return Start
    elif List[End] == Number:
        return End
    elif End <= Start:
        return -1
    else:
        middle = (Start+End)//2
        if List[middle] > Number:
            return binarySearch(List, Start, middle-1, Number)
        elif List[middle] < Number:
            return binarySearch(List, middle+1, End, Number)
        elif List[middle] == Number:
            return middle

if __name__ == "__main__":
    List = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
    print("If you want to stop print \"-1\"")
    ownList = input("Do you want to input your own list? (y,n): ")


    if ownList == 'y':
        List.clear()
        n = int(input("Input the lenght of your new list: "))

        for i in range(n):
            List.append(int(input("Element number " + str(i) +" - ")))

        List.sort()
        print("\n", List)

    elif ownList == 'n':
        pass
    else:
        pass

    while True:
        numberForSearch = int(input("Input your number for searching: "))
        if numberForSearch == -1:
            break
        position = binarySearch(List, 0, len(List)-1, numberForSearch)
        if position!=-1:
            print("Position of", numberForSearch,"is", position)
        else:
            print("Number", numberForSearch,"is not in list")

    print("The programm was stopped")