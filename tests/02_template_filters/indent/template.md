# Indent Filter Test

## Basic Indentation (4 spaces default)
```
{{ "Line 1\nLine 2\nLine 3" | indent }}
```

## Custom Indentation (8 spaces)
```
{{ "Function definition:\ndef hello():\n    print('Hello!')" | indent(8) }}
```

## Indenting File Content
```
{{ include_file('jexpand/__init__.py') | indent(2) }}
```

## Complex Indentation Example
Here's some nested content:

Level 1 content:
{{ "This is level 1\nMultiple lines at level 1" | indent(2) }}

Level 2 content:
{{ "This is level 2\nNested deeper\nWith more content" | indent(4) }}

Level 3 content:
{{ "This is level 3\nDeeply nested\nVery indented content" | indent(6) }}

## Indenting Code Blocks
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | indent(4) | code_block('python') }}

## Tab-like Indentation
{{ "Item 1\nItem 2\nItem 3" | indent(8) }}