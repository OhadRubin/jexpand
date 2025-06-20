# Intermediate Compilation Test

## Basic File Inclusion
This will be converted to Jinja2 syntax but not expanded in intermediate form:

"""
jexpand - Enhanced file expansion using Jinja2 templates
"""

from .main import expand_file, JinjaFileExpander, main

__version__ = "1.0.4"
__all__ = ["expand_file", "JinjaFileExpander", "main"]


if __name__ == "__main__":
    main() 


## Conditional Logic
The main module exists!
File size: 25262 bytes

## Simple Syntax Conversion Test
This should be converted from simple syntax to Jinja2:

Feature 1:
using jexpand should fail if any file/folder doesn't exists.

Feature 1.5:
I should be able to compile it to an intermidiate form and then compile it to a final form.

Feature 2:

Looking at the `download_repo_folder` function, it's a clever utility that downloads specific directories from a Git repository without having to clone the entire repo. Here's what it does:

## What `download_repo_folder` does:

1. **Sparse Checkout**: Uses Git's sparse-checkout feature to download only specific directories from a repository
2. **Temporary Download**: Creates a temporary directory, downloads the specified folders, reads all files, and cleans up
3. **Content Extraction**: Returns a dictionary mapping file paths to their contents
4. **Efficiency**: Avoids downloading the entire repository when you only need specific folders

The function takes:
- `url`: Git repository URL 
- `dirs_to_checkout`: List of directory paths to download
- `branch`: Git branch to pull from (defaults to "main")

## How it could be useful for jexpand:

This would be a **powerful addition** to jexpand's template capabilities! Here are some use cases:

### 1. **Include Remote Documentation/Examples**
```jinja2
<!-- Include examples directly from GitHub -->
{{ include_repo_folder('https://github.com/google/jax', ['jax/experimental/pallas/ops/tpu']) }}

<!-- Reference documentation from any public repo -->
{{ include_repo_folder('https://github.com/tensorflow/tensorflow', ['tensorflow/docs/guide']) }}
```

### 2. **Template Libraries & Snippets**
```jinja2
<!-- Pull reusable code templates -->
{{ include_repo_folder('https://github.com/myorg/code-templates', ['python/fastapi', 'python/utils']) }}
```

### 3. **Live Documentation Generation**
```jinja2
<!-- Always get the latest examples from upstream -->
<latest_examples>
{{ include_repo_folder('https://github.com/project/repo', ['examples'], branch='main') }}
</latest_examples>
```

### 4. **Cross-Repository References**
```jinja2
<!-- Compare implementations across different repos -->
<implementation_a>
{{ include_repo_folder('https://github.com/org1/project', ['src/core']) }}
</implementation_a>

<implementation_b>
{{ include_repo_folder('https://github.com/org2/project', ['lib/core']) }}
</implementation_b>
```

## Integration with jexpand:

You could add this as a new template function:

```python
def _include_repo_folder(self, url, dirs_to_checkout, branch="main", format_as="xml"):
    """Include files from a remote Git repository"""
    from .load_from_repo import download_repo_folder, filter_files
    
    try:
        content_dict = download_repo_folder(url, dirs_to_checkout, branch)
        # Apply similar formatting options as include_folder
        # Return formatted content
    except Exception as e:
        if self.strict_mode:
            raise
        return f"<!-- Error downloading from {url}: {str(e)} -->"
```

This would make jexpand incredibly powerful for documentation generation, code analysis, and creating templates that pull live content from multiple repositories!

## Loop Example
Item 1: file1
Item 2: file2
Item 3: file3

## Filter Examples
```text
Sample text for filtering
```

1 | Line 1
2 | Line 2
3 | Line 3

## Path Functions
File: example.py
Directory: path/to
Extension: .py