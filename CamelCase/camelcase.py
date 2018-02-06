def camelcase(string):
    # separate by word
    # found .title @stackoverflow while looking for way to make all lowercase
    word_list = string.title().split()
    # first letter of first word should be lower case
    word_list[0] = word_list[0].lower()
    # join words into single word
    new_name = ''.join(word_list)
    return new_name
