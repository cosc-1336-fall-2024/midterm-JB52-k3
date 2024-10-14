import question_d

def main():
    print('How much is your property tax?!')
    prompt = int(input ('Enter the assessment value on your property. '))
    assess = question_d.get_assessment_value(prompt)
    tax = question_d.get_tax_assessed(assess)
    print(f'Your assessment value is ${assess} and your taxes owed are ${tax}.')
    esc = input("Press 'Q' to quit or hit any other key to continue.")
    if esc == 'Q' or esc == 'q':
        pass
    else:
        main()
main()