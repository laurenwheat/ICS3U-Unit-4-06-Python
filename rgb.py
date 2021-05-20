#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program displays all RGB values

def main():

    print("We will display every RGB value from (0,0,0) to (255,255,255).")

    counter_x = 0
    counter_y = 0
    counter_z = 0

    for counter_x in range(256):
        for counter_y in range(256):
            for counter_z in range(256):
                print("RGB({0},{1},{2})".format(counter_x, counter_y,
                                                counter_z))


if __name__ == "__main__":
    main()
