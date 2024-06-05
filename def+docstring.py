def get_user_input():
    """
    Get user input for noun, verb, and adjective.

    """
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    return noun, verb, adjective

def fill_in_blanks(noun, verb, adjective):
    """
    Fill in the blanks in the story with provided words.

    Returns:
    story (str): Story with blanks filled in.
    """
    story = "Once upon a time, there was a {} {} who loved to {}. " \
            "But one day, they realized they had lost their {}! " \
            "They searched high and low, but couldn't find it. " \
            "So they decided to {} without it."
    return story.format(adjective, noun, verb, noun, verb)

def main():
    """
    Main function to prompt user for input and display the story.
    """
    noun, verb, adjective = get_user_input()
    story = fill_in_blanks(noun, verb, adjective)
    print(story)

""" 
This block ensure that the 'main' function is only executed if the scrip is run directly.
Not is its imported as a modul.
 """
if __name__ == "__main__":
    main()
