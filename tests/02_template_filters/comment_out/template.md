# Comment Out Filter Test

## Basic Comment Out (Default # character)
{{ "This is line 1\nThis is line 2\nThis is line 3" | comment_out }}

## Python-style Comments
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | comment_out('#') }}

## JavaScript-style Comments
{{ "function hello() {\n    console.log('Hello!');\n}" | comment_out('//') }}

## HTML Comments
{{ "<html>\n<head><title>Test</title></head>\n<body>Content</body>\n</html>" | comment_out('<!--') }}

## SQL Comments
{{ "SELECT * FROM users;\nUPDATE users SET active = 1;\nDELETE FROM logs;" | comment_out('--') }}

## C-style Comments
{{ "#include <stdio.h>\nint main() {\n    printf(\"Hello\");\n    return 0;\n}" | comment_out('//') }}

## Custom Comment Character
{{ "Configuration line 1\nConfiguration line 2\nConfiguration line 3" | comment_out(';') }}

## Combined with Other Filters
{{ include_file('jexpand/__init__.py') | comment_out('#') | indent(2) }}