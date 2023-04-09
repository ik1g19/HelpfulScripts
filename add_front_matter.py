import os
import yaml

# Define the YAML front matter template
front_matter_template = "---\n" + "title: {}\n" + "---\n"

# Define the function to add YAML front matter to a file
def add_front_matter_to_file(filepath):
    # Get the file's name without the extension
    filename = os.path.splitext(os.path.basename(filepath))[0]
    
    # Create the YAML front matter
    front_matter = front_matter_template.format(filename)
    
    # Read the file's contents
    with open(filepath, 'r', encoding='utf-8') as f:
        contents = f.read()
    
    # Add the YAML front matter to the contents
    new_contents = front_matter + contents
    
    # Write the new contents back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_contents)

# Define the function to recursively loop through all directories and subdirectories
def recursive_dir_loop(directory):
    # Loop through all files and directories in the current directory
    for name in os.listdir(directory):
        # Get the full path of the file/directory
        path = os.path.join(directory, name)
        
        # If the path is a directory, recurse into it
        if os.path.isdir(path):
            recursive_dir_loop(path)
        # If the path is a markdown file, add the YAML front matter
        elif os.path.isfile(path) and path.endswith('.md'):
            add_front_matter_to_file(path)

# Start the recursive loop at the current directory
recursive_dir_loop('.')
