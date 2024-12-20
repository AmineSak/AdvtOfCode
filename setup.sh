#!/bin/bash

# Prompt user for the day number
read -p "Enter the day number: " x

# Ensure x is valid
if [[ ! $x =~ ^[0-9]+$ ]]; then
  echo "Error: Please enter a valid numeric day."
  exit 1
fi

# Create the directory structure and files
mkdir -p ~/documents/adventOfCD/2024/$x
cd ~/documents/adventOfCD/2024/$x 

# Create the files
touch test.txt
touch input.txt
touch day$x.py

echo "Setup complete for Day $x!"