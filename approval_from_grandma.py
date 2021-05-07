#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program determines whether a grandma approves of you dating her
#     grandchild based off your age

import constants


def main():
    # this function determines whether the user is able to date the grandchild

    # input
    age_as_string = input("How old are you? ")

    # process & output
    try:
        age = float(age_as_string)
        if age > constants.MIN_AGE and age < constants.MAX_AGE:
            print("\nYou can date my grandchild!")
        elif age <= constants.MIN_AGE:
            print("\nYou're too young to date my grandchild!")
        elif age >= constants.MAX_AGE:
            print("\nYou're too old to date my grandchild!")
        else:
            print("\nI don't know!")
    except Exception:
        print("\nTell me your real age!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
