# List Comprehensions

if __name__ == '__main__':
    x = int(input('Enter the number of rows: '))
    y = int(input('Enter the number of columns: '))
    z = int(input('Enter the number of stars: '))
    n = int(input('Enter the number of spaces: '))
    print([[i, j, k] 
    for i in range(x + 1) 
        for j in range(y + 1) 
            for k in range(z + 1) 
                if i + j + k != n])
