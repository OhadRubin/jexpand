# Testing Line Numbers with Range Functionality

## Test 1: Range with short line numbers
{{ include_file('test_file.txt', start_line=3, end_line=5, line_numbers='short') }}

## Test 2: Range with full line numbers
{{ include_file('test_file.txt', start_line=7, end_line=9, line_numbers='full') }}

## Test 3: Entire file with short line numbers
{{ include_file('test_file.txt', line_numbers='short') }}

## Test 4: From start to line 3 with line numbers
{{ include_file('test_file.txt', end_line=3, line_numbers='short') }}

## Test 5: Single line with line numbers
{{ include_file('test_file.txt', start_line=2, end_line=2, line_numbers='full') }}