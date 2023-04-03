import sys
import os
import re

def replace_strings(file_path, prefix):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regular expression to find strings of the form ![[a|b]]
    regex = r'!\[\[(.*?)\|(.*?)\]\]'
    matches = re.findall(regex, content)

    # Loop through matches and replace with desired format
    for match in matches:
        a = match[0]
        b = match[1]
    
        # Replace whitespace with %20 in string a
        c = a.replace(' ', '%20')
    
        # Replace string with desired format
        str = '![|{0}]('+prefix+'{1})'
        replace_str = str.format(b, c)
        content = content.replace('![[{0}|{1}]]'.format(a, b), replace_str)

    # Write updated content back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


args = sys.argv
arg1 = args[1]

# Loop through all files in current directory and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)

        # Only process files with .txt extension
        if file_path.endswith('.md'):
            replace_strings(file_path, arg1)
