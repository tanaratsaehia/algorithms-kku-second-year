def bubble_sort(data:list, inverse:bool=False) -> list:
    for _ in range(len(data)):
        for j in range(len(data)):
            if j < len(data)-1 and (data[j] < data[j+1] if inverse else data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    return data

def bi_search(data, key):
    found = False
    low = 0
    hi = len(data)-1
    round_ = 0
    while (low <= hi) and not found:
        mid = int((low+hi)/2)
        if key == data[mid]:
            found = True
            round_+=1
        else:
            if key<data[mid]:
                hi=mid-1
                round_+=1
            else:
                low=mid+1
                round_+=1
    if found:
        index = mid
    else:
        index = -1
    return index

while True:
    print("Select menu")
    print("\t1.add data")
    print("\t2.search")
    print("\ttype 'e' for exit")
    try:
        selected_option = input("type '1' or '2' here: ")
        if selected_option == 'e':
            break
        selected_option = int(selected_option)
    except:
        print("please input 1 or 2")
    
    if selected_option == 1:
        data = input("fill number separate by space bar (2 3 1) :")
        data = data.split(" ")
        data = [int(i) for i in data]
        data = bubble_sort(data)
        print("sorted data:", data)
    elif selected_option == 2:
        key = input("fill number to find in data: ")
        try:
            key = int(key)
        except:
            print("input int only")
        
        result_index = bi_search(data, key)
        if result_index == -1:
            print(f"\ndata '{key}' not found\n")
        else:
            print(f"\ndata '{key}' found at index '{result_index}'\n")
    else:
        print("please input 1 or 2")