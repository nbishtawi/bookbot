def get_num_words(file_contents):
    words = file_contents.split()
    return(len(words))

def get_num_character(file_contents):
    counts = {}
    for ch in file_contents.lower():
        counts[ch] = counts.get(ch,0)+1
    return counts

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for key, value in dictionary.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            dictionary_list.append(new_dict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list