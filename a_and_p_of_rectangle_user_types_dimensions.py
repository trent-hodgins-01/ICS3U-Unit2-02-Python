# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/13/20
# This program calculates the area and perimeter of a rectangle
# The user enters in the dimensions


def main():
    # this function calculates area and perimeter

    # input
    length = int(input("Enter length of the rectangle (mm): "))
    width = int(input("Enter width of the rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {0}mm².".format(area))
    print("Perimeter is {0}mm.".format(perimeter))


if __name__ == "__main__":
    main()
