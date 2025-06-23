# Include File Function Test

## Basic File Inclusion
This demonstrates basic file inclusion:

{{ include_file('tests/01_core_functions/include_file/sample_file.txt') }}

## File Inclusion with Default Value
This tests including a non-existent file with a default value:

{{ include_file('tests/01_core_functions/include_file/nonexistent.txt', default='Default content when file is missing') }}

## File Inclusion with Custom Encoding
This tests the same file with UTF-8 encoding explicitly specified:

{{ include_file('tests/01_core_functions/include_file/sample_file.txt', encoding='utf-8') }}

## Relative Path Test
Including the jexpand module's __init__.py file:

{{ include_file('jexpand/__init__.py') }}

## File Size Check Before Including
{% if file_exists('tests/01_core_functions/include_file/sample_file.txt') %}
File exists! Size: {{ file_size('tests/01_core_functions/include_file/sample_file.txt') }} bytes
{% endif %}