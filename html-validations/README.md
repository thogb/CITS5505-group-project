# Perform html validation

Combine all .html file in this project into a single .html file called all.html

cd into this directory

find ../app -name "\*.html" -exec cat {} >> all.html \;

Goto https://validator.w3.org/

Select By file upload and upload the all.html or select direct input and 
copy paste all contents of all.html into the textarea.

## Existing Validation Output
Inside the same folder there is a file called html_validation.html which contains 
the output from the validation performed with the existing all.html.

All the errors seems to be related to Jinja.