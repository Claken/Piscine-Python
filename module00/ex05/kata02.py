# Put this at the top of your kata02.py file
kata = (2019, 9, 2, 2, 30)

if __name__ == '__main__':
    new_string = "{:02d}/{:02d}/{:04d} {:02d}:{:02d}"
    print(new_string.format(kata[1], kata[2], kata[0], kata[3], kata[4]))
