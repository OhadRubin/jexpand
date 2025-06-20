# Code Block Filter Test

## Basic Code Block (No Language)
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | code_block }}

## Python Code Block
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | code_block('python') }}

## JavaScript Code Block with Inline Content
{{ "function hello() {\n    console.log('Hello, World!');\n}" | code_block('javascript') }}

## JSON Code Block
{{ '{\n  "name": "jexpand",\n  "version": "1.0.4",\n  "features": ["templates", "expansion"]\n}' | code_block('json') }}

## SQL Code Block
{{ "SELECT * FROM users WHERE active = 1 ORDER BY created_date DESC;" | code_block('sql') }}

## Combined with Other Filters
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | line_numbers | code_block('python') }}

## Bash Code Block
{{ "#!/bin/bash\necho 'Running tests...'\npython3 -m pytest tests/" | code_block('bash') }}