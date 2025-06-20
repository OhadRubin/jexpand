# jexpand - Complete Feature List

This document provides a comprehensive list of all features available in the jexpand template expansion tool.

## Core Template Functions

### 1. File Inclusion Functions
- **`include_file(path, encoding='utf-8', default='')`**
  - Include the complete contents of a file
  - Supports custom encoding and default values
  - Handles missing files based on strict mode

- **`include_folder(folder_path, pattern='*', recursive=False, format_as='xml', separator='\n\n', encoding='utf-8', include_folder_name=True)`**
  - Include contents of all files in a folder
  - Support for file pattern matching (*.py, *.txt, etc.)
  - Recursive directory traversal option
  - Multiple output formats: xml, blocks, content, dict
  - Customizable file separators and encoding

- **`include_repo_folder(url, dirs_to_checkout, branch='main', format_as='xml')`**
  - Include files directly from remote Git repositories
  - Sparse checkout for efficient downloads
  - Support for specific branches
  - Multiple output formats

### 2. File System Information Functions
- **`file_exists(path)`**
  - Check if a file exists
  - Returns boolean true/false

- **`file_size(path)`**
  - Get file size in bytes
  - Returns 0 if file doesn't exist or error occurs

- **`file_extension(path)`**
  - Get file extension including the dot (e.g., '.py')
  - Uses pathlib for reliable extraction

- **`basename(path)`**
  - Get the filename part of a path
  - Example: '/path/to/file.txt' → 'file.txt'

- **`dirname(path)`**
  - Get the directory part of a path
  - Example: '/path/to/file.txt' → '/path/to'

## Template Filters

### 1. Code Formatting Filters
- **`code_block(language='')`**
  - Wrap content in markdown code blocks
  - Optional language specification for syntax highlighting
  - Usage: `{{ content | code_block('python') }}`

- **`indent(spaces=4)`**
  - Indent each line with specified number of spaces
  - Default: 4 spaces
  - Usage: `{{ content | indent(8) }}`

- **`comment_out(comment_char='#')`**
  - Comment out each line with specified character
  - Default: '#' character
  - Usage: `{{ content | comment_out('//') }}`

- **`line_numbers(format='short')`**
  - Add line numbers to content
  - Formats: 'short' (1 | content) or 'full' (line 1 | content)
  - Usage: `{{ content | line_numbers('full') }}`

## Compilation Features

### 1. Standard Template Expansion
- **Basic expansion**: Process Jinja2 templates with custom functions
- **Simple syntax conversion**: Convert `{file_path}` to `{{ include_file('file_path') }}`
- **Context support**: Pass variables to templates during expansion

### 2. Intermediate Compilation (Feature 1.5)
- **`compile_to_intermediate()`**: Convert template syntax without expanding includes
- **`expand_intermediate()`**: Expand intermediate form to final output
- **Two-stage compilation**: Template → Intermediate → Final
- **Syntax preservation**: Maintains existing Jinja2 syntax during conversion

### 3. Simple Expansion Mode
- **Backward compatibility**: Support for simple `{file_path}` syntax
- **Automatic conversion**: Converts simple syntax to full Jinja2
- **Legacy support**: Maintains compatibility with older templates

## Operating Modes

### 1. Strict Mode (Default)
- **File validation**: Fails if any referenced file/folder doesn't exist
- **Error handling**: Raises clear exceptions for missing resources
- **Pattern validation**: Fails if no files match folder patterns

### 2. Non-Strict Mode
- **Graceful fallback**: Shows placeholder comments for missing files
- **Error tolerance**: Continues processing despite missing resources
- **Debugging friendly**: Clearly indicates what's missing

## Output Formats

### 1. Include Folder Formats
- **`xml`**: Wraps each file in `<file path='...'>content</file>` tags
- **`blocks`**: Each file wrapped with `<!-- File: path -->` comments
- **`content`**: Just concatenated file contents with separators
- **`dict`**: Returns Python dictionary {filename: content}

### 2. Repository Formats
- **`xml`**: XML-wrapped file contents with paths
- **`blocks`**: Comment-wrapped file blocks
- **`content`**: Raw concatenated content
- **`dict`**: Dictionary format for programmatic use

## Command Line Interface

### 1. Basic Operations
- **Standard expansion**: `jexpand template.md`
- **Output to file**: `jexpand template.md -o output.md`
- **Help and version**: `jexpand --help`, `jexpand --version`

### 2. Mode Controls
- **Strict mode**: `jexpand template.md --strict` (default)
- **Non-strict mode**: `jexpand template.md --no-strict`
- **Template directory**: `jexpand template.md --template-dir /path/to/templates`

### 3. Compilation Features
- **Intermediate compilation**: `jexpand template.md --intermediate intermediate.md`
- **Two-stage compilation**: `jexpand template.md --intermediate inter.md --final final.md`

## Repository Integration

### 1. Git Repository Support
- **Sparse checkout**: Download only specified directories
- **Branch selection**: Choose specific Git branches
- **Temporary handling**: Automatic cleanup of downloaded content
- **Error handling**: Graceful handling of network/repository errors

### 2. Content Processing
- **Format conversion**: Automatic RST to Markdown conversion
- **File filtering**: Skip common non-content files (__init__.py, .ipynb)
- **Path normalization**: Clean and standardize file paths

## Advanced Features

### 1. Template Environment
- **Jinja2 integration**: Full Jinja2 template engine support
- **Custom loader**: String-based template loading
- **Environment configuration**: Trim blocks, strip blocks, preserve newlines

### 2. Error Handling
- **Comprehensive error messages**: Clear descriptions of problems
- **Graceful degradation**: Fallback behavior in non-strict mode
- **Exception propagation**: Proper error handling in strict mode

### 3. Path Handling
- **Absolute paths**: Full path support
- **Relative paths**: Relative to working directory or template directory
- **Home directory**: Tilde (~) expansion support
- **Cross-platform**: Works on Windows, macOS, Linux

## Python API Features

### 1. Programmatic Access
- **JinjaFileExpander class**: Main expansion engine
- **expand_file() function**: Simple file expansion
- **expand_string() method**: Template string expansion
- **Context passing**: Variable injection into templates

### 2. Integration Capabilities
- **Module import**: Direct Python import without subprocess
- **Custom functions**: Extensible template function system
- **Custom filters**: Extensible filter system
- **Configuration**: Flexible initialization options

## Version Information
- **Current version**: 1.0.4
- **Python compatibility**: 3.7+
- **Dependencies**: jinja2, GitPython (for repo features), pypandoc (for format conversion)

## Backward Compatibility
- **Legacy syntax**: Support for old `{file_path}` syntax
- **API compatibility**: Maintains existing function signatures
- **Template compatibility**: Existing templates continue to work
- **CLI compatibility**: Previous command-line options preserved