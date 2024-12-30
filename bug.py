def function_with_unclosed_file(filepath):
    f = open(filepath, 'r')
    # ... some code that processes the file ... 
    # Missing: f.close() 
    return

function_with_unclosed_file("myfile.txt")