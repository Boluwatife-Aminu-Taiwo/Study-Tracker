# learning os and datetime module
# os is for interacting with the os
import os
from datetime import datetime

# Check if file exists
print(os.path.exists("studylog.txt"))

# Create a new directory (if it doesn't exist)
if not os.path.exists("logs"):
    os.mkdir("logs")

# List all files in current folder
print(os.listdir("."))

# Get full absolute path
print(os.path.abspath("studylog.txt"))

# Delete a file
if os.path.exists("var.py"):
    os.remove("var.py")




# Get current time
now = datetime.now()
print(now)

# Format it nicely
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)

# Use in a filename
filename = now.strftime("log_%Y%m%d_%H%M%S.txt")
print(filename)
