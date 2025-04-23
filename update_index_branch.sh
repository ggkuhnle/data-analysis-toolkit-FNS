#!/bin/bash

# Script to update Colab badge URLs in index.qmd files
# Replaces '/blob/groks-revisions/' with '/blob/main/'
# Usage: ./update_index_branch.sh

# Define the directory to search for index.qmd files
NOTEBOOKS_DIR="notebooks"

# Check if the notebooks directory exists
if [ ! -d "$NOTEBOOKS_DIR" ]; then
    echo "Error: Directory $NOTEBOOKS_DIR not found. Please run this script from the repository root."
    exit 1
fi

# Find all index.qmd files and update the branch reference
find "$NOTEBOOKS_DIR" -type f -name "index.qmd" | while read -r file; do
    # Check if the file contains the old branch reference
    if grep -q "/blob/groks-revisions/" "$file"; then
        # Perform the replacement
        # On macOS, sed requires an empty string '' after -i for in-place editing without backup
        sed -i '' 's|/blob/groks-revisions/|/blob/main/|g' "$file"
        echo "Updated $file: Replaced /blob/groks-revisions/ with /blob/main/"
    else
        echo "Skipped $file: No /blob/groks-revisions/ found"
    fi
done

echo "Update complete! Please review changes and commit them to git."