import tempfile
import os

# Create a temporary file
fd, temp_path = tempfile.mkstemp(suffix='.json')


# Write some data to the temporary file
with os.fdopen(fd, 'w') as temp_file:
    temp_file.write("Hello, world!")

print(temp_path)