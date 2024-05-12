#!/bin/bash

# Directory containing the files
DIRECTORY="C:/Directory/Real Data"
# Prefix to add to each file
PREFIX=1
# Change to the directory
cd "$DIRECTORY"

# Loop through all files in the directory
for FILE in *; do
    # Check if it's a regular file (not a directory)
    if [ -f "$FILE" ]; then
        # Rename the file by adding a prefix
        mv "$FILE" "${PREFIX}_${FILE}"
	((PREFIX++))
    fi
done

