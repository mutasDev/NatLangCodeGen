# Natural Language and Code Generation

This project includes the source code of a web application used for communication with the API endpoints of OpenAI's Playground for accessing the GPT- and Codex-Models.
This web application was used to perform the research described in [this](https://project.mutas.dev) research project.


# Installation and Starting the Web Application
## Requirements: 
   * Node, including npm (https://nodejs.org/en/)
   * Angular (https://angular.io)
      
## Installation:
   1. Check out the repository via `git clone https://github.com/mutasDev/NatLangCodeGen.git`
   2. in the repositories home directory execute `npm install`
   3. in the repositories home directory execute `ng serve`
      This will compile and start the application, access the application in your browser under `localhost:4200`
           

## Configuration 
 To use the OpenAI APIs an API key is needed. Such an API key can be received from the [OpenAI Playground](https://beta.openai.com/playground) after logging into your OpenAI Account and in the API Keys section of the user setting. 
 
 Copy your API key to the [environment file](/src/environments/environment.ts) into the empty string field named *OPENAI_API_KEY*.
 
 **Important: ** Usage of the Codex model requires beta access to the API which has to be requested from OpenAI.
 
 
 In this environment file, the parameters for the requests are also configurable. Parameters without `nl_` before their name refer to the parameters for GPT-3 requests and parameters with the `nl_` prefix are used in the request to the Codex model.
 
 The parameters are explained best in the [OpenAI Playground](https://beta.openai.com/playground) on the right side.
 The two paremeters *pretext* and *posttext* are string fields that are added to each prompt before or after the "main"prompt, respectively.

# Functionality
The web application offers several options for handling requests to and from the OpenAI-API.

Currently, four Features are enabled:

   1. Single Prompt
      + Sends a Single Completion Request to the GPT-3 API and displays the response in the textfield below the input
      + Uses the parameters from the [environment file](/src/environments/environment.ts) 
      
   2. Multi Prompt
      + Sends multiple completion requests to the GPT-3 API sequentially and stores the results in generated source files
      + uses the parameters from the [environment file](/src/environments/environment.ts) 
      + The input is uploaded as a zip archive containing .json files, exact json format see below
      + The *Generate* button starts the sequential handling of the requests
      + After the generation is done (currently only visible in the developer console of the browser) the *save Zip* button saves a zip archive conttaining the generated source files, file format depends on the language field in the respective json entry of the prompt
      
   3. Scenario Translation
      + Sends multiple completion requests to the Codex API sequentially and stores the results in generated json files
      + uses the parameters with nl_ prefix from the [environment file](/src/environments/environment.ts)
      + returns a zip archive containing the generated responses in json formats, exact json format see below
      + The *Generate* button starts the sequential handling of the requests
      + As the Codex API has a different limit than the GPT-3 API, a rate limiting was enabled vie the in browser debugger being called after every 100 requests. When that occurs, wait a little bit (around 1-2 minutes should suffice) and press continue on the debugger window. This will continue the sequential processing of the requests. Not waiting for long enough can result in the crash of the request process and then one needs to restart the process with all requests.
      + After the generation is done (currently only visible in the developer console of the browser) the *save Zip* button saves a zip archive conttaining the generated natural language descriptions as json files in a zip archive.
      
   4. Report Generation
       + Upload a ZIP file received from Scenario Translation to receive a CSV report of all entries in that zip file.
       + The CSV Contains the following fields in their respective order:
           + Programming Language
           + File Name incl. directory path
           + Naturalness Score
           + Expressiveness Score
           + Content Adequacy Score
           + Conciseness Score
           + Vulnerability Flag
           
        For the meaning of those scores and flags, refer to the [project report](https://project.mutas.dev)
        
# JSON Formats
## Input Format of Multi Prompts
The Multiprompt Feature creates completions via the GPT-3 model. It was used to create code snippets from natural language descriptions.
The input json files should contain the following information:
        + *text* : the natural language description of the code to be generated
        + *language* : the programming language the code should be generated in (currently supported: Java, C, Python, C++, Javascript)
        + *name* (optional) : name of the file to be generated

## Output Format of Scenario Translation
The Scenario Translation Feature creates completions via the Codex model. It was used to natural language descriptions from code snippets.
The output json files contains the following information:
        + *text* : the generated natural language description
        + *language* : the programming language of the source file translated (if possible)
        + *name* : file name incl. the directory
        + *vulnerable* : flag set based on existing CodeQL Result files in the directory of the code snippet, undefined if no results file found
        + a score field for each of the four scores *naturalness*, *expressiveness*, *contentadequacy*, *conciseness*, all set to empty value
