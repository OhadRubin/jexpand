# Output Formats Test

## XML Format (Default)
{{ include_folder('tests/05_output_formats/xml_format/sample_files') }}

## Blocks Format
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*', false, 'blocks') }}

## Content Format with Default Separator
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*', false, 'content') }}

## Content Format with Custom Separator
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*', false, 'content', '\n\n=== FILE SEPARATOR ===\n\n') }}

## XML Format with Pattern Matching
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*.yml', false, 'xml') }}

## Blocks Format with Pattern Matching
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*.txt', false, 'blocks') }}

## XML Format without Folder Name in Path
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*', false, 'xml', '\n\n', 'utf-8', false) }}

## Comparison of All Formats
All formats shown side by side:

### XML:
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*.yml', false, 'xml') }}

### Blocks:
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*.yml', false, 'blocks') }}

### Content:
{{ include_folder('tests/05_output_formats/xml_format/sample_files', '*.yml', false, 'content') }}