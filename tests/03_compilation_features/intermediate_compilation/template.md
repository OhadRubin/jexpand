# Intermediate Compilation Test

## Basic File Inclusion
This will be converted to Jinja2 syntax but not expanded in intermediate form:

{{ include_file('jexpand/__init__.py') }}

## Conditional Logic
{% if file_exists('jexpand/main.py') %}
The main module exists!
File size: {{ file_size('jexpand/main.py') }} bytes
{% else %}
The main module does not exist.
{% endif %}

## Simple Syntax Conversion Test
This should be converted from simple syntax to Jinja2:

{jexpand/feature_todo.md}

## Loop Example
{% for item in ['file1', 'file2', 'file3'] %}
Item {{ loop.index }}: {{ item }}
{% endfor %}

## Filter Examples
{{ "Sample text for filtering" | code_block('text') }}

{{ "Line 1\nLine 2\nLine 3" | line_numbers }}

## Path Functions
File: {{ basename('path/to/example.py') }}
Directory: {{ dirname('path/to/example.py') }}
Extension: {{ file_extension('example.py') }}