# Strict Mode Test

## Existing File (Should Work)
{{ include_file('jexpand/__init__.py') }}

## Non-existent File (Should Fail in Strict Mode)
{{ include_file('tests/04_operating_modes/strict_mode/missing_file.txt') }}

## Non-existent Folder (Should Fail in Strict Mode)
{{ include_folder('tests/04_operating_modes/strict_mode/missing_folder') }}

## Pattern with No Matches (Should Fail in Strict Mode)
{{ include_folder('jexpand', '*.nonexistent') }}

## File Information Functions (Should Handle Missing Files)
File exists check: {{ file_exists('tests/04_operating_modes/strict_mode/missing_file.txt') }}
File size: {{ file_size('tests/04_operating_modes/strict_mode/missing_file.txt') }} bytes