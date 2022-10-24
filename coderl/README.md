# How to use the generate python script to invoke the CodeRL language model for program synthesis

The generate python script loads a pre-trained version of the CodeRL language model (Salesforce/codet5-large-ntp-py) into an in-memory model and allows the usage of said model for program synthesis.

## Usage
Invoke the python script in a python command line with the path to the .zip archive containing the json prompts as the first parameter.
Two optional parameters:
Second command line argument is the path to the output zip archive to be created, if ommitted, the archive will be placed in the script directory and named 'generated_programs.zip'.
The Third command line argument is an optional DEBUG flag, if the third argument equals "DEBUG" the debug mode will be used, including more output for each synthesis.






## Troubleshooting
`JSONDecodeErrors` can possible occur when zipping json files together on MACOSX, due to the OS adding a `_MACOSX` directory to the zip file.
If you are using the zipping feature on MacOS, you need to clean the zip from this meta folder by using the command `zip -d prompts.zip __MACOSX/\*` on the zip file.


## Example call
python generate.py ../../NatLangSet/data/py.zip
