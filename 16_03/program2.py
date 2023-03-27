def max_zeros(input_string):
    count = 0
    start_max = 0
    maxcount = 0
    for i in range(len(input_string)):

        # print(i)
        if input_string[i] == '0':
            count += 1
            # print(f'count = {count}')

        else:
            #print(f'max count = {maxcount} and count = {count}')
            if maxcount < count:
                print(f'max count = {maxcount}')
                maxcount = count
                count = 0
                print("count = ", count)

            else:
                count = 0
            #print(f'maxcount = {max_count}, count = {count}')'''
            count = 0
    if maxcount < count:
        maxcount = count
    return maxcount


if __name__ == "__main__":
    input_string = "0100000000"
    maxzeros = max_zeros(input_string)
    print("Max continuous zeros are len: ", maxzeros)
    print("start index is:", input_string.index('0' * maxzeros))
