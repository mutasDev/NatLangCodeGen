from contextlib import nullcontext
import fileinput
from importlib.resources import path
from re import I
import zipfile
import json
from transformers import AutoTokenizer, T5ForConditionalGeneration
import sys


def synthesise(text):
    if (debug_mode):
        print("Text: " + text + "\n")
    prompt = text + "\n Generated Code for the Program above: \n"
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=128)
    if (debug_mode):
        print(
            "GEN:" + tokenizer.decode(generated_ids[0], skip_special_tokens=True) + "\n")
    return

# Print iterations progress
# Taken from https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


# Function that takes a path string and parses the zip file located
# under that path to get all json files from it and store their string
# representation in a list
# RETURNS: list of parsed files
def get_promptfiles_from_file(path):
    prompts = []
    with zipfile.ZipFile(path, 'r') as zip_file:
        for name in zip_file.infolist():
            if ((not name.is_dir()) and name.filename.__contains__('json')):
                with zip_file.open(name, 'r') as prompt_file:
                    file_bytes = prompt_file.read()
                    file_string = file_bytes.decode('UTF-8')
                    fileinfo = json.loads(file_string)
                    prompts.append(fileinfo)
    return prompts


if __name__ == "__main__":
    # Setup pretrained model from salesforce data
    print("Setting up model, this can take a few minutes at max")
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-large-ntp-py")
    model = T5ForConditionalGeneration.from_pretrained(
        "Salesforce/codet5-large-ntp-py")

    # parse prompts from input file
    path_to_prompts = sys.argv[1]
    prompts = get_promptfiles_from_file(path_to_prompts)

    # parse optional debug parameter
    print(len(sys.argv))
    print(sys.argv)
    if (len(sys.argv) >= 3):
        debug_mode = sys.argv[3] == "DEBUG"
    else:
        debug_mode = False

    # Start program synthesis for all prompts
    gen = []
    progress = 0
    for prompt in prompts:
        gen.append((prompt, synthesise(prompt['text'])))
        progress = progress+1
        printProgressBar(iteration=progress, total=prompts.__len__())

    # Store results in zipfile
    with zipfile.ZipFile('generated_programs.zip', 'w') as output_file:
        for entry in gen:
            output_file.writestr(entry[0]['name'], str(entry[1]))
            output_file.writestr(str(entry[0]['name']).replace(
                ".c", ".json").replace(".py", ".json"), json.dumps(str(entry[0])))
