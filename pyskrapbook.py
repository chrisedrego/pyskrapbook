import pyperclip
import os

data = []
pyperclip.copy('')
temp = ''

f = open("notes.txt","w+")

def raw_input(listex):
    strx = ''
    for i in range(len(listex)):
        strx = strx + str(listex[i]) + '\n'
    return strx;

def main():
    while True:
        input = pyperclip.paste()
        if input == 'boom':
            SystemExit()
            break
        elif input != '':
            if(temp!=input):
                data.append(input)
                print(data)
            elif input == '^C' or input == 'exit':
                print("Dumping the Data Exiting System")
                print(data)
                f.write(str(raw_input(data)))
                f.close()
                break
        temp = str(input)
        input = ''
        continue

if __name__== "__main__":
    main()