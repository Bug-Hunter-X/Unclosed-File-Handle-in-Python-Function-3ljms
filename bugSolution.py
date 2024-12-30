def function_with_closed_file(filepath):
    try:
        with open(filepath, 'r') as f:
            # ... some code that processes the file ... 
            contents = f.read()
            # Process contents
            return contents
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

function_with_closed_file("myfile.txt") 