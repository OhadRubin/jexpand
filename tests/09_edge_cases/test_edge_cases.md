# Testing Edge Cases

## Test 1: Out of bounds line number (should handle gracefully in non-strict mode)
{{ include_file('test_file.txt', start_line=15, end_line=20) }}

## Test 2: Invalid range (start > end)
{{ include_file('test_file.txt', start_line=8, end_line=5) }}

## Test 3: Negative line numbers
{{ include_file('test_file.txt', start_line=-1, end_line=3) }}