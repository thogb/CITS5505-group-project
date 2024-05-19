# Perform CSS validation

Combine all .css file in this project into a single .css file called all.css

cd into this directory

find ../app -name "\*.css" -exec cat {} >> all.css \;

Goto https://jigsaw.w3.org/css-validator/

Select By file upload and upload the all.css
