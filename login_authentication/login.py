#!/usr/bin/python3

"""
Login Authentication

A small script that handles login with a backoff timer
"""

import time
import webbrowser

# Define approved users and their corresponding passwords in a dictionary
APPROVED_USERS: dict = {"dkasp": "qweqweqwe", "jbarr": "qweqweqwe"}

# Timeout duration in seconds
TIMEOUT: int = 30
MAX_ATTEMPTS: int = 4

DEST_LINK: str = "https://www.w3schools.com/python/python_lists.asp"


def main():
    """The main method"""

    # Initialize login attempt counter w/  maximum allowed login attempts
    login_attempts: int = 0

    while True:
        # Input username and password from the user
        input_user: str = input("Enter username: ")
        input_pass: str = input("Enter password: ")

        # Check if the input username exists in the dictionary and if the password is correct
        if input_user in APPROVED_USERS and input_pass == APPROVED_USERS[input_user]:
            print("Login successful")

            # Open in a web browser- just a random redirect to a tab I had open 101
            webbrowser.open(DEST_LINK)

            break  # Exit the loop if login is successful

        else:
            print("Incorrect username or password")
            login_attempts += 1

            # Check if the maximum attempts have been reached
            if login_attempts >= MAX_ATTEMPTS:
                print(
                    f"Maximum login attempts reached. Please try again in {TIMEOUT} seconds."
                )
                time.sleep(TIMEOUT)


if __name__ == "__main__":
    main()
