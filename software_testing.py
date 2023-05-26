Executable file testing

import subprocess

def test_executable(executable_path, test_cases):
    for test_case in test_cases:
        # Extract test case data
        name = test_case['name']
        input_data = test_case['input']
        expected_output = test_case['expected_output']

        # Execute the software executable
        process = subprocess.Popen([executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Pass input data to the executable
        stdout, stderr = process.communicate(input=input_data)

        # Check the output against the expected value
        assert stdout.strip() == expected_output.strip(), f"{name}: Expected output {expected_output}, but got {stdout.strip()}"

        # Test case passed
        print(f"{name}: PASSED")

# Example usage
executable_path = 'path/to/executable.exe'
test_cases = [
    {
        "name": "Test case 1",
        "input": "input data",
        "expected_output": "expected output"
    },
    {
        "name": "Test case 2",
        "input": "input data",
        "expected_output": "expected output"
    }
]

test_executable(executable_path, test_cases)
