# Write a function called `cleanup` which takes a string as input and returns a "cleaned string" meaning:
#  - remove any ? , . or !
#  - strip off the whitespace from the ends
#  - return text in lower case
 
#  write code to call your function and test it




def cleanup(text: str) -> str:
    '''
    This function takes a string as input and returns a cleaned string by removing any ?, ., or !,
    stripping off whitespace from the ends, and converting the text to lower case.
    '''
    # Remove unwanted characters
    cleaned_text = text.replace('?', '').replace('.', '').replace('!', '')
    # Strip whitespace from the ends
    cleaned_text = cleaned_text.strip()
    # Convert to lower case
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text

# Test the cleanup function
test_string = "  Hello, World!  "
result = cleanup(test_string)
print(result)

#test function with a couple of calls
text = "  This is a test string!  "
expected_output = "this is a test string"
cleaned_text = cleanup(text)
print(cleaned_text)  # Output: "this is a test string"
print(expected_output == cleaned_text)  # Output: True

