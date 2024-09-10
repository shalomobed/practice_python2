
def get_v2c_ratio(string1):
    vowels = ['a','e','i','o','u']
    count_vowels = 0
    count_cons = 0
    for letter in string1:
        if letter in vowels:
            count_vowels += 1
    count_cons = len(string1) - count_vowels
    ratio = count_vowels/count_cons
    print(f'{ratio:.2f}')

get_v2c_ratio('abcacdae')

def get_longest_run_length(string2):
    current = 1
    maximum = 1
    for i in range(1, len(string2)):
        if string2[i] == string2[i-1]:
            current += 1
        else:
            if current > maximum:
                maximum = current
                current = 1

    if current > maximum:
        maximum = current
    print(maximum)

get_longest_run_length('abbcccde')
