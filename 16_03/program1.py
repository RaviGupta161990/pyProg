#WAP to find the maximun length of consecutive 0's in a binary string
def max_zeros(input_string):
    count = 0
    max_count = []
    for i in range(len(input_string)):
        if input_string[i] == '0':
            count += 1
        else:
            max_count.append(count)
            count = 0
    max_count.append(count)
    return max(max_count)
if __name__ == "__main__":
    input_string = "00001000001"
    maxzeros = max_zeros(input_string)
    print("Max continuous zeros are len: ",maxzeros)
    print("start index is:", input_string.index('0'* maxzeros))



