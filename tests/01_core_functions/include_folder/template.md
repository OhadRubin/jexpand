# Include Folder Function Test

## Basic Folder Inclusion (XML format)
This demonstrates basic folder inclusion with XML format:

{{ include_folder('tests/01_core_functions/include_folder/sample_folder') }}

## Folder Inclusion with Pattern Matching (Python files only)
This includes only Python files from the folder:

{{ include_folder('tests/01_core_functions/include_folder/sample_folder', '*.py', false, 'blocks') }}

## Recursive Folder Inclusion
This includes all files recursively with blocks format:

{{ include_folder('tests/01_core_functions/include_folder/sample_folder', '*', true, 'blocks') }}

## Content Format (Raw concatenation)
This shows files concatenated with custom separator:

{{ include_folder('tests/01_core_functions/include_folder/sample_folder', '*.txt', false, 'content', '\n--- FILE SEPARATOR ---\n') }}

## Pattern Matching for JavaScript Files
This includes only JavaScript files:

{{ include_folder('tests/01_core_functions/include_folder/sample_folder', '*.js', true, 'xml') }}

## Folder Information
{% if file_exists('tests/01_core_functions/include_folder/sample_folder') %}
The sample folder exists and contains files.
{% else %}
The sample folder does not exist.
{% endif %}