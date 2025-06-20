# jexpand Feature Tests

This directory contains comprehensive tests for all jexpand features. Each feature is tested in its own folder with dedicated templates and supporting files.

## Test Structure

### 01_core_functions/
Tests for core template functions:
- **include_file/**: Tests file inclusion with various options
- **include_folder/**: Tests folder inclusion with different formats and patterns
- **include_repo_folder/**: Tests repository inclusion (requires network)
- **file_exists/**: Tests file existence checks
- **file_size/**: Tests file size retrieval
- **file_extension/**: Tests file extension extraction
- **basename/**: Tests basename extraction
- **dirname/**: Tests dirname extraction

### 02_template_filters/
Tests for template filters:
- **code_block/**: Tests markdown code block wrapping
- **indent/**: Tests content indentation
- **comment_out/**: Tests line commenting
- **line_numbers/**: Tests line number addition

### 03_compilation_features/
Tests for compilation modes:
- **standard_expansion/**: Tests normal template expansion
- **intermediate_compilation/**: Tests intermediate form compilation
- **two_stage_compilation/**: Tests two-stage compilation workflow
- **simple_syntax_conversion/**: Tests {file} to {{ include_file('file') }} conversion

### 04_operating_modes/
Tests for different operating modes:
- **strict_mode/**: Tests strict mode (fails on missing files)
- **non_strict_mode/**: Tests non-strict mode (placeholders for missing files)

### 05_output_formats/
Tests for different output formats:
- **xml_format/**: Tests XML output format
- **blocks_format/**: Tests blocks output format
- **content_format/**: Tests content output format
- **dict_format/**: Tests dictionary output format

### 06_cli_features/
Tests for command-line interface:
- **basic_cli/**: Tests basic CLI functionality
- **output_to_file/**: Tests file output
- **template_directory/**: Tests template directory specification
- **version_help/**: Tests version and help commands

### 07_advanced_features/
Tests for advanced functionality:
- **path_handling/**: Tests various path types (absolute, relative, ~)
- **error_handling/**: Tests error conditions and recovery
- **context_passing/**: Tests variable context passing

## Running Tests

### Run All Tests
Execute the comprehensive test runner:
```bash
cd /workspace
python3 tests/run_all_tests.py
```

### Run Individual Tests
Test specific features:
```bash
# Test include_file function
python3 -m jexpand tests/01_core_functions/include_file/template.md

# Test code_block filter
python3 -m jexpand tests/02_template_filters/code_block/template.md

# Test intermediate compilation
python3 -m jexpand tests/03_compilation_features/intermediate_compilation/template.md --intermediate intermediate.md
```

### Run Individual Test Runners
Some tests have their own runners:
```bash
python3 tests/01_core_functions/include_file/test_runner.py
```

## Test Categories

### ✅ Core Functions (8 tests)
- File inclusion with encoding, defaults, error handling
- Folder inclusion with patterns, recursion, formats
- Repository inclusion from Git repos
- File system information functions

### ✅ Template Filters (4 tests)
- Code block formatting with language support
- Content indentation with custom spacing
- Line commenting with various comment characters
- Line numbering in short and full formats

### ✅ Compilation Features (4 tests)
- Standard Jinja2 template expansion
- Intermediate form compilation (syntax conversion only)
- Two-stage compilation workflow
- Simple {file} syntax conversion

### ✅ Operating Modes (2 tests)
- Strict mode validation (fails on missing resources)
- Non-strict mode graceful handling (shows placeholders)

### ✅ Output Formats (4 tests)
- XML format with file path attributes
- Blocks format with comment headers
- Content format with custom separators
- Dictionary format for programmatic use

### ✅ CLI Features (4 tests)
- Basic command-line expansion
- Output redirection to files
- Template directory specification
- Version and help command functionality

### ✅ Advanced Features (3 tests)
- Path handling (absolute, relative, home directory)
- Error handling and recovery mechanisms
- Context variable passing to templates

## Expected Outcomes

### Successful Tests
- ✅ All core functions work with valid inputs
- ✅ All filters produce expected output formats
- ✅ Compilation features handle syntax conversion correctly
- ✅ Non-strict mode shows placeholders for missing files
- ✅ Output formats produce correct structures
- ✅ CLI commands execute without errors

### Expected Failures
- ❌ Strict mode fails appropriately with missing files
- ❌ Invalid repository URLs fail gracefully
- ❌ Malformed templates show clear error messages

## Test File Patterns

Each test folder typically contains:
- **template.md**: Main test template
- **sample_files/**: Supporting files for inclusion
- **test_runner.py**: Individual test script (optional)
- **expected_output.md**: Expected results (optional)

## Dependencies

Tests require:
- Python 3.7+
- jinja2
- GitPython (for repository tests)
- pypandoc (for format conversion)

## Coverage

These tests cover:
- 🔧 **8 core template functions**
- 🎨 **4 template filters**
- ⚙️ **4 compilation modes**
- 🔒 **2 operating modes**
- 📋 **4 output formats**
- 💻 **4 CLI features**
- 🚀 **3 advanced features**

**Total: 29+ individual feature tests**

## Troubleshooting

### Common Issues
1. **Missing dependencies**: Install with `pip install jinja2 GitPython pypandoc`
2. **Network tests**: Repository tests require internet connection
3. **Path issues**: Ensure tests are run from workspace root
4. **Permission errors**: Some tests create temporary files

### Test Debugging
Use `--no-strict` mode for tests with missing files:
```bash
python3 -m jexpand tests/path/to/template.md --no-strict
```

Add `-o output.md` to save results for inspection:
```bash
python3 -m jexpand tests/path/to/template.md -o debug_output.md
```