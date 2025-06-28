#!/bin/bash

# Check for exactly two arguments
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <week-number> <on|off>"
  exit 1
fi

WEEK_NUM=$1
MODE=$2

# Validate week number
if ! [[ "$WEEK_NUM" =~ ^[0-9]+$ ]]; then
  echo "Error: Week number must be a positive integer."
  exit 1
fi

# Validate mode
if [[ "$MODE" != "on" && "$MODE" != "off" ]]; then
  echo "Error: Second argument must be 'on' or 'off'."
  exit 1
fi

# Target directories
DIRS=("labs" "studios" "homework")

for DIR in "${DIRS[@]}"; do
  # Check if directory exists
  if [ -d "$DIR" ]; then
    for FILE in "$DIR"/*.md; do
      if [[ "$MODE" == "off" ]]; then
        echo "$FILE"
        # Turn visibility off for all files
        sed -i '' 's/visible:\ true/visible:\ false/' "$FILE"
	sed -i '' 's/nav_exclude:\ false/nav_exclude:\ true/' "$FILE"
      else
        # Extract parent week number
        PARENT_LINE=$(grep -m1 "^parent: Week " "$FILE")
        if [[ "$PARENT_LINE" =~ Week[[:space:]]+([0-9]+) ]]; then
          FILE_WEEK=${BASH_REMATCH[1]}
          if [ "$FILE_WEEK" -le "$WEEK_NUM" ]; then
            sed -i 's/visible: false/visible: true/' "$FILE"
          fi
        fi
      fi
    done
  fi
done
