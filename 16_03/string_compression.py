# Program to do strin compression

def compress_string(input_string):
    finalstr = ""
    count = 0
    current_char = input_string[0]
    for i in range(len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            finalstr += current_char+str(count)
            current_char = input_string[i]
            count = 1
    finalstr += current_char + str(count)

    return finalstr if len(finalstr) < len(input_string) else input_string

if __name__ == '__main__':
    print( compress_string('ab') == 'ab')