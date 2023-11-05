#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()  # This enables detailed error messages

print("Content-Type: text/html")  # Set the content type to HTML
print()  # Print an empty line to indicate the start of the response body

# Your API logic goes here
print("Hello, this is your API endpoint!")
