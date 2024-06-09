def process_line(line):
    # Strip newline characters
    line = line.strip()
    
    # Remove the first letter and capitalize the second letter
    if len(line) < 2:
        return "12!"
    modified_line = line[1].upper() + line[2:]

    # Ensure the line is 12 characters minimum
    if len(modified_line) < 11:
        remaining_length = 11 - len(modified_line)
        modified_line += '1234567890'[:remaining_length]

    modified_line += '!'
    
    return modified_line

def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():  # Process only non-empty lines
                modified_line = process_line(line)
                outfile.write(modified_line + '\n')

# Usage example
input_file = 'input.txt'
output_file = 'output.txt'
process_file(input_file, output_file)
