import re

def main():
    try:
        print('Exit with Ctrl-C\n')

        while True:
            print('Please enter your article:')
            input_text = input()

            # Remove pronounciation, language origin, date of birth, etc.
            simplified_text = re.sub('[\(\[].*?[\)\]]', '', input_text)

            # Split the term and it's definition around 'is' or 'was'
            is_split = simplified_text.partition(' is ')
            was_split = simplified_text.partition(' was ')

            text_before_is = is_split[0]
            text_before_was = was_split[0]


            # Found the keyword 'is' first
            if len(text_before_is) < len(text_before_was) and is_split[1]:

                # Strip surrounding whitespace from the term and it's definition
                term = text_before_is.strip()
                definition = is_split[2].partition('.')[0].strip()
                # Process the completed term and definition
                handle_phrase(term + ': ' + definition + '.')


            # Found the keyword 'was' first
            elif len(text_before_is) > len(text_before_was) and was_split[1]:

                # Strip surrounding whitespace from the term and it's definition
                term = text_before_was.strip()
                definition = was_split[2].partition('.')[0].strip()
                # Process the completed term and definition
                handle_phrase(term + ': ' + definition + '.')


            # Handle incomplete entry
            else:
                print("\nA definition was not created because an 'is' or 'was' could not be found.\n")


    # Allow loop to end gracefully
    except KeyboardInterrupt:
        pass

    # For debugging
    except Exception as e:
        print(e)


# Process the final phrase
def handle_phrase(full_phrase):
    print('\nDefinition created:')
    print(full_phrase + '\n')

    with open('definitions.txt', 'a') as text_file:
        text_file.write(full_phrase + '\n\n')


# Run this code if being executed directly
if __name__ == '__main__':
    main()