from subprocess import check_call

def main():
    check_call(['pyinstaller', '-y', 'app.spec'])

if __name__ == '__main__':
    main()