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

## Shorthand Syntax

JExpand provides powerful shorthand syntax for quick file inclusion without writing full Jinja2 templates.

### CLI-Style Shorthand (`>>>>|`)

The `>>>>|` prefix enables command-line style syntax for file operations:

```markdown
# Basic file inclusion
>>>>| src/main.py
# Becomes: {{ include_file('src/main.py') }}

# Include file with XML formatting
>>>>| -f -x config.yaml
# Becomes: {{ include_file('config.yaml', format_as='xml') }}

# Include directory with XML formatting
>>>>| -d -x src/components
# Becomes: {{ include_folder('src/components', format_as='xml') }}

# Include specific line range
>>>>| -f -s 10 -e 50 utils.js
# Becomes: {{ include_file('utils.js', start_line=10, end_line=50) }}

# Include with line numbers
>>>>| -l -x database.py
# Becomes: {{ include_file('database.py', format_as='xml', line_numbers='short') }}

# Include with full line numbers
>>>>| --full src/api.js
# Becomes: {{ include_file('src/api.js', line_numbers='full') }}

# Line range using path syntax
>>>>| src/module.py:L5-L15
# Becomes: {{ include_file('src/module.py', start_line=5, end_line=15) }}
```

#### CLI Shorthand Flags

- `-f` or `--file` - Include file (default)
- `-d` or `--directory` - Include directory
- `-x` - Format as XML
- `-l` - Add short line numbers (1 |)
- `--full` - Add full line numbers (line 1 |)
- `-s N` - Start from line N
- `-e N` - End at line N
- `:LN-LM` - Line range suffix (L5-L15)

### Function-Style Shorthand

Quick function-like syntax for common operations:

```markdown
# Basic inclusion
f("src/app.py")                    # {{ include_file('src/app.py') }}
d("src/utils")                     # {{ include_folder('src/utils') }}

# XML formatting
file_xml("config.json")            # {{ include_file('config.json', format_as='xml') }}
dir_xml("templates")               # {{ include_folder('templates', format_as='xml') }}
f_xml_lines("main.py")             # {{ include_file('main.py', format_as='xml', line_numbers='short') }}
dir_xml_lines("src")               # {{ include_folder('src', format_as='xml', line_numbers='short') }}
d_xml_fulllines("docs")            # {{ include_folder('docs', format_as='xml', line_numbers='full') }}

# Line numbers
f_lines("code.js")                 # {{ include_file('code.js', line_numbers='short') }}
f_fulllines("main.c")              # {{ include_file('main.c', line_numbers='full') }}
d_lines("scripts")                 # {{ include_folder('scripts', line_numbers='short') }}
d_fulllines("examples")            # {{ include_folder('examples', line_numbers='full') }}

# Line ranges
f_s10("partial.py")                # {{ include_file('partial.py', start_line=10) }}
f_e30("beginning.py")              # {{ include_file('beginning.py', end_line=30) }}
f_s10_e30("middle.py")             # {{ include_file('middle.py', start_line=10, end_line=30) }}
```

### Real-World Usage Example

Here's how shorthand syntax is used in practice (from pivotbench):

```markdown
<set_rem>
We are implementing a benchmark. The latest vision is in `proposal_high_level.md`.
I want to include all relevant files for context.
</set_rem>

>>>>| -f -x proposal.md
>>>>| -f -x proposal_high_level.md
>>>>| -f -x schedule.md
>>>>| -f -x system_prompts/benchmark_prompt.md
>>>>| -f -x flow_questions.xml
>>>>| -f -x src/core/icl_schema.py
>>>>| -f -x src/level4/predictor.py
>>>>| -f -x src/level3/builder_loader.py
>>>>| -f -x src/level3/pipeline.py
>>>>| -d -x flow_files
```

This expands to include all these files in XML format, creating a comprehensive context document.

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

## Special Features

### `<set_rem>` Blocks

Wrap instructions or context that should be preserved but not processed:

```markdown
<set_rem>
This is a reminder or instruction block.
It can contain context, notes, or instructions for LLMs.
The content inside is preserved as-is.
</set_rem>

>>>>| -f -x src/main.py
>>>>| -f -x src/utils.py
```

This is particularly useful when building prompt templates for LLMs, where you want to include instructions followed by file contents.

## Pro Tips
- Use `--no-strict` when some included files might not exist
- Chain filters: `{{ content | line_numbers | indent(2) | code_block('python') }}`
- Use `file_exists()` for conditional inclusion
- Combine with loops for batch file processing
- Use `<jexpand>` blocks for dynamic template generation with Python
- Python output becomes shorthand syntax that gets processed by jexpand
- Use `>>>>|` shorthand for quick file inclusion without Jinja2 syntax
- Combine `>>>>|` with `-x` flag for XML-formatted output (great for LLM prompts)
- Use `<set_rem>` blocks to wrap instructions that should remain in the output