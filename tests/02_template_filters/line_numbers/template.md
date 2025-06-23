# Line Numbers Filter Test

## Basic Line Numbers (Short format)
{{ "First line\nSecond line\nThird line\nFourth line" | line_numbers }}

## Full Format Line Numbers
{{ "First line\nSecond line\nThird line\nFourth line" | line_numbers('full') }}

## Line Numbers with File Content (Short)
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | line_numbers }}

## Line Numbers with File Content (Full)
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | line_numbers('full') }}

## Combined with Code Block
{{ include_file('tests/02_template_filters/code_block/sample_code.py') | line_numbers | code_block('python') }}

## Line Numbers with Indentation
{{ "def function():\n    pass\n\nclass MyClass:\n    def method(self):\n        return True" | line_numbers | indent(4) }}

## Long Content Example
{{ "Line 1: This is the first line\nLine 2: This is the second line\nLine 3: This is the third line\nLine 4: This is the fourth line\nLine 5: This is the fifth line\nLine 6: This is the sixth line\nLine 7: This is the seventh line\nLine 8: This is the eighth line\nLine 9: This is the ninth line\nLine 10: This is the tenth line" | line_numbers('full') }}

## Empty Lines Handling
{{ "Line 1\n\nLine 3\n\nLine 5" | line_numbers }}