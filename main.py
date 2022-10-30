
def read_file(path_of_file):
    with open(path_of_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def letter_count(file_contents):
    letters = {}
    file_contents = file_contents.lower()
    nospaces_string = "".join(file_contents.split())
    for char in nospaces_string:
        if char in letters:
            #update the value + 1
            letters[char] += 1 
        else:
            if char.isalpha():
                letters[char] = 1
    return letters           

def formatted_report(path_to_file):
    file_output = read_file(path_to_file)
    total_num_words = word_count(file_output)
    letters = letter_count(file_output)

    print('--- Begin report of {} ---'.format(path_to_file))
    print('{} words found in the document \n'.format(total_num_words))
    
    new_list = []
    for key, val in letters.items():
        new_list.append([val, key])

    list = sorted(new_list, reverse=True)
    for item in list:
        print("The '{}' character was found '{}' times".format(item[1], item[0])) 
    
    print('--- End Report ---')

formatted_report('books/frankenstein.txt') 