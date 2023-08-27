
# String Manipulation Algorithm
This project involves a string manipulation algorithm designed to transform input strings into combinations of specific terms. The algorithm is focused on identifying and creating unique combinations based on provided criteria within the input string. The primary goal is to generate well-structured combinations for further analysis or usage.

## Algorithm Overview
The algorithm takes an input string and follows these key steps:

## Separation of Choice Lists: 
The input string is split into individual words, and these words are grouped into choice lists based on certain criteria. The algorithm identifies words that are not "OR" and groups them until an "OR" or the end of the string is encountered. This forms the basis for generating different combinations.

## Building Combinations: 
The algorithm then constructs combinations by combining elements from the choice lists. It begins by initializing a result list and iterates through each choice list. For each choice in a choice list, the algorithm combines it with each element in the result list to create new combinations. This process generates a set of unique combinations.

## Final Output: 
The final output of the algorithm is a list of strings representing the various combinations derived from the input string. These combinations can be used for further analysis or processing as required.

## Test Cases
The project includes a set of test cases to validate the correctness of the algorithm. These test cases cover a range of scenarios to ensure the algorithm performs as expected. Here are some of the notable test cases:

Single Element Input: Validates that a single element input string is correctly transformed into a single-element output list.

Multiple Elements with Single OR: Checks if an input string with multiple elements and a single "OR" creates unique combinations.

Multiple Elements with Multiple ORs: Tests the algorithm's ability to handle multiple "OR" conditions in the input string and generate distinct combinations.

Input with Double Quote and OR: Validates the algorithm's behavior when encountering a double quote character and "OR" in the input string.

Multiple OR Conditions: Tests the algorithm's performance with multiple "OR" conditions and multiple elements, ensuring accurate combinations are produced.

Ten OR Conditions: Evaluates the algorithm's efficiency and accuracy when dealing with a larger number of "OR" conditions.

## Usage
To use the algorithm, follow these steps:

Set up a virtual environment with python3 -m virtualenv venv.
Activate the virtual environment using source venv/Scripts/activate.
Run tests using pytest.
Execute the algorithm by running python3 main.py.

The algorithm, once executed, will transform input strings into combinations and provide the resulting list of combinations for further analysis or utilization.
