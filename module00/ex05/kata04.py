# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == '__main__':
    new_string = "module_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}"
    print(new_string.format(kata[0], kata[1], kata[2], kata[3], kata[4]))
