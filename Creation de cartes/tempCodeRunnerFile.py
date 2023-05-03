def create_map(size):
    map_list = []
    # Première ligne
    first_row = [" "] + list(range(1, size+1)) + [""]
    map_list.append(first_row)
    # Lignes du milieu
    for i in range(1, size+1):
        row = [size-i+1] + [""]*(size-1) + [size+i]
        for j in range(1, size//2+1):
            if i == j or i == size-j+1:
                row[j] = "/"
                row[size-j] = "/"
            elif i == size//2+1 and j == size//2:
                row[j] = "L"
        map_list.append(row)
    # Dernière ligne
    last_row = [""] + list(range(size*2, size, -1)) + [""]
    map_list.append(last_row)
    return map_list