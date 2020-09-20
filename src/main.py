import os

from brute import brute


def begin():
    # The path to the cppcryptfs executable
    # Example: C:/Users/User/cppcryptfs.exe
    exe = ''
    # Add the path to the encrypted directory between the empty quotes
    # Example: C:\\Users\\User\\some-folder
    arg = ' --mount="" --drive=a --password='

    for temp in brute(length=50, letters=True, numbers=True, symbols=True):
        # If you know the beginning of the password
        begin = ''
        # If you know the ending of the password
        end = ''
        password = begin + temp + end
        command = exe + arg + '\"' + password + '\"'
        print(command)
        os.system(command)


def main():
    begin()


if __name__ == '__main__':
    main()
