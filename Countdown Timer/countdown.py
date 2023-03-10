import time  # importing for the sleep command
import os    # importing for the cls command, as well as attempting color changes

# First function sets the teas and prompts selection. Four presets and one manual, uses a loop within a loop for error checks


def tea_type():
    types_of_tea = {"White": 270, "Green": 210, "Oolong": 240, "Black": 210}
    duration = 0
    while True:
        t = input('Please select type of tea: {} or Other '.format(','.join(types_of_tea)))
        if t.title() in types_of_tea:
            duration = types_of_tea[t.title()]
            break
        elif t.title() == 'Other':
            while True:
                try:
                    duration = int(input('Please enter manual tea timer in seconds '))
                    break
                except ValueError:
                    print('Please enter a valid integer response in seconds (1-999)')
            break
    return duration

# Second function formats and prints the countdown timer as well as added cleaning functionality with os and ascii


def countdown(t):
    while t:
        mins,secs = divmod(t, 60)
        timer = 'Your tea is brewing\n{:02d}:{:02d}'.format(mins,secs)
        os.system('cls')
        print(timer, end="\n")
# \r is an ascii moves the 'carriage' back, allowing python to print over what was printed before
# \n is being used to replace \r as we are importing os which has a clear line function 'cls'
        time.sleep(1)
        t -= 1


# countdown function calls upon tea_type function
countdown(tea_type())
# '\a' is an ascii bell call, works in CMD
print("Timer completed!\a")