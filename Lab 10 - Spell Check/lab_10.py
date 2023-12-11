import re


# split lines into singular words with regex
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    # Open the file, and store it in a variable
    dictionary_file = open("dictionary.txt")

    # instantiate empty list to store dictionary words in
    dictionary_list = []
    # for loop through dictionary file and push each word to the list
    for line in dictionary_file:
        # remove whitespace
        line = line.strip()
        dictionary_list.append(line)

    # close file
    dictionary_file.close()

    # track line number
    line_num = 0

    # step 8 to know what search method we are doing
    print("--- Linear Search ---")

    # open file and store in variable to iterate through
    file = open("AliceInWonderLand200.txt")

    # for loop through file
    for line in file:

        # increase line number
        line_num += 1

        # strip whitespace off line variable
        line = line.strip()

        # call split_line function to separate the words apart
        word_list = split_line(line)

        # for loop through words in the line
        for word in word_list:

            # beginning of the list
            current_list_position = 0

            # upper case word to compare
            upperWord = word.upper()

            # loop through entire list until you find the word
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != upperWord:
                # go to next list variable
                current_list_position += 1

            # if we cant find the word in the dictionary then print the line and misspelled word
            if upperWord not in dictionary_list:
                print("line", line_num, "possible misspelled word:", word)

    dictionary_file.close()

    # print out what search method we are using
    print("")
    print("--- Binary Search ---")

    # open file and store in variable to iterate through
    file = open("AliceInWonderLand200.txt")

    # reset line_num before looping through new file
    line_num = 0

    # for loop through file
    for line in file:

        # increase line number
        line_num += 1

        # strip whitespace off line variable
        line = line.strip()

        # call split_line function to separate the words apart
        word_list = split_line(line)

        # for loop through words in the line
        for word in word_list:

            # upper case word to compare
            upperWord = word.upper()

            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            while lower_bound <= upper_bound:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] == upperWord:
                    break
                elif dictionary_list[middle_pos] < upperWord:
                    lower_bound = middle_pos + 1
                else:
                    upper_bound = middle_pos - 1
            else:

                # if we cant find the word in the dictionary then print the line and misspelled word
                print("line", line_num, "possible misspelled word:", word)

    # close out file
    file.close()


# call the main function to fire it all off
main()
