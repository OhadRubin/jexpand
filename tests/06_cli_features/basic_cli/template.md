# Basic CLI Test

## Simple Content
This is a basic template for testing CLI functionality.

## Current File Information
Template file: {{ basename('tests/06_cli_features/basic_cli/template.md') }}

## Include Simple Content
{{ include_file('jexpand/__init__.py') | code_block('python') }}

## File System Info
{% if file_exists('jexpand/main.py') %}
✅ Main module exists
{% else %}
❌ Main module missing
{% endif %}

## Current Date/Time
Template processed successfully!