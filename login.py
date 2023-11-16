import time
import webbrowser

# Define approved users and their corresponding passwords in a dictionary
approved_users = {
    "dkasp": "qweqweqwe",
    "jbarr": "qweqweqwe"
}

# Initialize login attempt counter w/  maximum allowed login attempts
login_attempts = 0
max_attempts = 4

# Timeout duration in seconds
timeout_duration = 30  # .5 minute

while login_attempts < max_attempts:
    # Input username and password from the user
    input_user = input("Enter username: ")
    input_pass = input("Enter password: ")

    # Check if the input username exists in the dictionary and if the password is correct
    if input_user in approved_users and input_pass == approved_users[input_user]:
        print("Login successful")
        
        # Open in a web browser- just a random redirect to a tab I had open 101
        webbrowser.open("https://www.w3schools.com/python/python_lists.asp")
        
        break  # Exit the loop if login is successful
    
    else:
        print("Incorrect username or password")
        login_attempts += 1

        # Check if the maximum attempts have been reached
        if login_attempts == max_attempts:
            print(f"Maximum login attempts reached. Please try again in {timeout_duration} seconds.")
            time.sleep(timeout_duration)
