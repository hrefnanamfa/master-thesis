#!/bin/bash

# Directory containing the files
DIRECTORY="C:/Directory/Anonymous Data"
# Change to the directory
cd "$DIRECTORY"

# Loop through all files in the directory
for FILE in *; do
    # Check if it's a regular file (not a directory)
    if [ -f "$FILE" ]; then
        # Split the file name on "_" and use the first item as the new file name
        NEW_FILENAME=$(echo "$FILE" | cut -d'_' -f1)
        
        # Add the ".pdf" extension to the new file name
        NEW_FILENAME="$NEW_FILENAME.pdf"
        
        # Rename the file
        mv "$FILE" "$NEW_FILENAME"
    fi
done
