# Non-Strict Mode Test

## Existing File (Should Work)
{{ include_file('jexpand/__init__.py') }}

## Non-existent File (Should Show Placeholder)
{{ include_file('tests/04_operating_modes/non_strict_mode/missing_file.txt') }}

## Non-existent File with Default Value
{{ include_file('tests/04_operating_modes/non_strict_mode/missing_file.txt', default='This is the default content when file is missing') }}

## Non-existent Folder (Should Show Placeholder)
{{ include_folder('tests/04_operating_modes/non_strict_mode/missing_folder') }}

## Pattern with No Matches (Should Show Placeholder)
{{ include_folder('jexpand', '*.nonexistent') }}

## Mixed Existing and Non-existing Files
{% for file_path in ['jexpand/__init__.py', 'missing1.txt', 'jexpand/main.py', 'missing2.txt'] %}
### File: {{ file_path }}
{% if file_exists(file_path) %}
✅ File exists ({{ file_size(file_path) }} bytes)
{{ include_file(file_path) | code_block }}
{% else %}
❌ File does not exist
{{ include_file(file_path, default='<FILE NOT FOUND>') }}
{% endif %}

---
{% endfor %}

## Repository Test (Commented out - requires network)
<!-- {{ include_repo_folder('https://github.com/nonexistent/repo', ['missing']) }} -->