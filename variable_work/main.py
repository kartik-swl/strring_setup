import os
import shutil

# Define file paths
original_parameter_file = "original_parameter.txt"
changed_parameter_file = "changed_parameter.txt"
backup_directory = "backup_parameters"

# Check if the original parameter file exists
if os.path.isfile(original_parameter_file):
    with open(original_parameter_file, "r") as file:
        original_parameter = file.read()
else:
    original_parameter = input("Enter the original parameter: ")
    with open(original_parameter_file, "w") as file:
        file.write(original_parameter)

# Ask the user if they want to change the parameter
change_option = input("Do you want to change the parameter? ((y) for yes/(n) for no): ")

if change_option.lower() == "y":
    new_parameter = input("Enter a new parameter: ")

    # Save the changed parameter in a new file
    with open(changed_parameter_file, "w") as file:
        file.write(new_parameter)

    # Move the old original parameter to the backup directory
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
    backup_file = os.path.join(backup_directory, f"original_parameter_{original_parameter_file}")
    shutil.move(original_parameter_file, backup_file)

    # Update the original parameter with the new value
    original_parameter = new_parameter

# Print the parameter
print("Parameter: " + original_parameter)
