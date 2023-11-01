# Define a list of steps amazon ring measurements
steps = [
    "Step 1: Setup DUT in front of speaker",
    "Step 2: Place wind tunnel in a way that all DUT's will be measured in the same way",
    "Step 3: Take wind recording with Speaker close up and wind set to 0.0m/s",
    "Step 4: Take wind recording with with wind set to 3m/s ",
    "Step 5: Take recording with the speaker 1m away and wind set to 0.0m/s",
    "Step 6: Take recording with the speaker 1m away and wind set to 3m/s",
    
]

# Initialize the step counter
current_step = 0

# Start the procedure
while current_step < len(steps):
    # Display the current step
    print(steps[current_step])

    # Ask for user input to move to the next step
    user_input = input("Press Enter to continue to the next step, or type 'exit' to quit: ")

    if user_input.lower() == 'exit':
        print("Exiting the procedure.")
        break  # Exit the loop if the user types 'exit'
    
    current_step += 1

# When all steps are completed
print("Procedure completed.")
