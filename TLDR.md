# JExpand TLDR - Quick Reference

## Installation
```bash
pip install jexpand
```

## Basic CLI Usage
```bash
# Print to stdout
jexpand template.md

# Save to file
jexpand template.md -o output.md

# Non-strict mode (don't fail on missing files)
jexpand template.md --no-strict
```

## Core Template Functions
```jinja2
{{ include_file('path/to/file.py') }}           # Include file contents
{{ include_file('file.py', start_line=10, end_line=20) }}  # Include lines 10-20
{{ include_file('file.py', start_line=5) }}     # Include from line 5 to end
{{ include_file('file.py', end_line=10) }}      # Include from start to line 10
{{ include_file('file.py', line_numbers='short') }}  # Include with line numbers (1 |)
{{ include_file('file.py', start_line=5, end_line=10, line_numbers='full') }}  # Range with line numbers (line 1 |)
{{ file_exists('path/to/file') }}               # Check if file exists (true/false)
{{ file_size('path/to/file') }}                 # Get file size in bytes
{{ basename('path/to/file.py') }}               # Get filename: file.py
{{ dirname('path/to/file.py') }}                # Get directory: path/to
{{ file_extension('path/to/file.py') }}         # Get extension: .py
```

## Useful Filters
```jinja2
{{ content | code_block('python') }}            # Wrap in ```python code block
{{ content | indent(4) }}                       # Indent each line by 4 spaces
{{ content | comment_out('#') }}                # Comment out each line with #
{{ content | line_numbers }}                    # Add line numbers: "1 | content"
{{ content | line_numbers('full') }}            # Add line numbers: "line 1 | content"
```

## Python Code Execution

Execute Python code directly in templates to generate dynamic content:

```markdown
<jexpand>
files = ["src/main.py", "src/utils.py", "src/config.py"]
for filename in files:
    print(f'file_xml("{filename}")')
</jexpand>
```

Output becomes shorthand that gets processed:
```markdown
file_xml("src/main.py")
file_xml("src/utils.py") 
file_xml("src/config.py")
```

### Dynamic File Lists
```markdown
<jexpand>
import os
for file in os.listdir("src"):
    if file.endswith(".js"):
        print(f'{{ include_file("src/{file}") | code_block("javascript") }}')
</jexpand>
```

### Conditional Processing
```markdown
<jexpand>
project_type = "react"  # Could come from environment
if project_type == "react":
    components = ["Button.jsx", "Modal.jsx", "Form.jsx"]
    for comp in components:
        print(f'f("src/components/{comp}")')
</jexpand>
```

## Common Patterns

### Include Source with Syntax Highlighting
```jinja2
{{ include_file('src/main.py') | code_block('python') }}
```

### Conditional File Inclusion
```jinja2
{% if file_exists('config.yaml') %}
{{ include_file('config.yaml') | code_block('yaml') }}
{% else %}
No configuration found.
{% endif %}
```

### Multiple Files with Loop
```jinja2
{% for file in ['app.py', 'utils.py', 'models.py'] %}
## {{ basename(file) }}
{{ include_file(file) | code_block('python') }}
{% endfor %}
```

### Source with Line Numbers
```jinja2
{{ include_file('script.py') | line_numbers | code_block('python') }}
```

### Include Specific Line Ranges
```jinja2
<!-- Include a specific function (lines 15-30) -->
{{ include_file('utils.py', start_line=15, end_line=30) | code_block('python') }}

<!-- Include configuration section from start to line 20 -->
{{ include_file('config.yaml', end_line=20) | code_block('yaml') }}

<!-- Include error handling part from line 50 onwards -->
{{ include_file('main.py', start_line=50) | code_block('python') }}

<!-- Include just the imports section -->
{{ include_file('app.py', start_line=1, end_line=10) | code_block('python') }}

<!-- Include function with line numbers for debugging -->
{{ include_file('utils.py', start_line=25, end_line=40, line_numbers='short') | code_block('python') }}

<!-- Include configuration with full line number format -->
{{ include_file('config.py', end_line=15, line_numbers='full') | code_block('python') }}
```

### File Information Table
```jinja2
| File | Size | Extension |
|------|------|-----------|
{% for file in ['app.py', 'README.md', 'config.json'] %}
{% if file_exists(file) %}
| {{ basename(file) }} | {{ file_size(file) }} bytes | {{ file_extension(file) }} |
{% endif %}
{% endfor %}
```

## Simple Syntax (Legacy)
```markdown
{src/main.py}           # Gets converted to {{ include_file('src/main.py') }}
```

## Python API
```python
from jexpand import JinjaFileExpander

expander = JinjaFileExpander(strict_mode=True)

# Expand to file
expander.expand_file("template.md", "output.md")

# Expand to string
result = expander.expand_file("template.md")

# Simple expansion
result = expander.simple_expand("template.md")
```

## Pro Tips
- Use `--no-strict` when some included files might not exist
- Chain filters: `{{ content | line_numbers | indent(2) | code_block('python') }}`
- Use `file_exists()` for conditional inclusion
- Combine with loops for batch file processing
- Use `<jexpand>` blocks for dynamic template generation with Python
- Python output becomes shorthand syntax that gets processed by jexpand