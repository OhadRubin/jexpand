# JEXPAND.md - Comprehensive Guide to File Assembly and Template Expansion

## Table of Contents
1. [What is JEXPAND.md?](#what-is-jexpandmd)
2. [Core Concepts](#core-concepts)
3. [Basic Template Functions](#basic-template-functions)
4. [Python Code Execution Blocks](#python-code-execution-blocks)
5. [Advanced File Assembly Patterns](#advanced-file-assembly-patterns)
6. [Multi-File Project Assembly](#multi-file-project-assembly)
7. [Dependency Resolution Strategies](#dependency-resolution-strategies)
8. [Best Practices](#best-practices)
9. [Real-World Examples](#real-world-examples)
10. [Integration Workflows](#integration-workflows)

## What is JEXPAND.md?

JEXPAND.md is a powerful template-based file assembly system that allows you to:

- **Combine multiple source files** into a single consolidated file
- **Extract specific sections** from files using line ranges
- **Resolve dependencies** by controlling file inclusion order
- **Generate documentation** that includes live code examples
- **Create build artifacts** from distributed source code
- **Maintain single-source-of-truth** while generating multiple outputs

The system uses Jinja2 templating with custom functions specifically designed for file manipulation and code assembly.

## Core Concepts

### Template Processing Pipeline

```
Source Files → JEXPAND Template → jexpand CLI → Final Output
     ↓              ↓                ↓           ↓
 Multiple .js    template.md    Processing    combined.js
 Multiple .py    assembly.md    Engine        bundle.py
 Config files    docs.md        Jinja2        README.md
```

### Key Principles

1. **Declarative Assembly**: Describe what you want, not how to get it
2. **Line-Level Precision**: Include exact line ranges from source files
3. **Dependency Awareness**: Control inclusion order to resolve dependencies
4. **Content Preservation**: Maintain original formatting and structure
5. **Template Reusability**: Create reusable assembly patterns

## Basic Template Functions

### File Inclusion Functions

```jinja2
# Include entire file
{{ include_file('src/utils.js') }}

# Include specific line range
{{ include_file('src/core.js', start_line=10, end_line=50) }}

# Include from start to specific line
{{ include_file('src/config.js', end_line=25) }}

# Include from specific line to end
{{ include_file('src/main.js', start_line=100) }}

# Include with line numbers for debugging
{{ include_file('src/debug.js', start_line=1, end_line=20, line_numbers='short') }}
```

### File System Functions

```jinja2
# Check if file exists before including
{% if file_exists('optional-config.js') %}
{{ include_file('optional-config.js') }}
{% endif %}

# Get file metadata
File size: {{ file_size('data.json') }} bytes
Extension: {{ file_extension('script.py') }}
Directory: {{ dirname('/path/to/file.js') }}
Filename: {{ basename('/path/to/file.js') }}
```

### Content Formatting Filters

```jinja2
# Wrap in code blocks with syntax highlighting
{{ include_file('example.py') | code_block('python') }}

# Add indentation
{{ include_file('snippet.js') | indent(4) }}

# Comment out code
{{ include_file('template.sql') | comment_out('--') }}

# Add line numbers
{{ include_file('source.c') | line_numbers('full') }}

# Chain multiple filters
{{ include_file('code.js') | line_numbers | indent(2) | code_block('javascript') }}
```

## Python Code Execution Blocks

JExpand supports embedded Python code execution using `<jexpand>` blocks. This powerful feature allows you to dynamically generate template content using Python's full programming capabilities.

### Basic Python Execution

```markdown
<jexpand>
files = ["src/main.py", "src/utils.py", "src/config.py"]
for filename in files:
    print(f'file_xml("{filename}")')
</jexpand>
```

The Python code executes and its output becomes part of the template:

```markdown
file_xml("src/main.py")
file_xml("src/utils.py")
file_xml("src/config.py")
```

This output is then processed by the shorthand parser and becomes:

```jinja2
{{ include_file("src/main.py", format_as='xml') }}
{{ include_file("src/utils.py", format_as='xml') }}
{{ include_file("src/config.py", format_as='xml') }}
```

### Dynamic File Discovery

Use Python to dynamically discover and include files:

```markdown
<jexpand>
import os
import glob

# Find all JavaScript files in components directory
for js_file in glob.glob("src/components/**/*.js", recursive=True):
    print(f'f("{js_file}")')
    
# Add separators between files
print('\n// ============================================================================\n')

# Find all TypeScript definition files
for ts_file in glob.glob("src/**/*.d.ts", recursive=True):
    print(f'file_xml("{ts_file}")')
</jexpand>
```

### Conditional Assembly Logic

Implement complex conditional logic for file assembly:

```markdown
<jexpand>
# Configuration-based assembly
config = {
    "include_tests": True,
    "environment": "production",
    "features": ["auth", "database", "caching"]
}

# Core files (always included)
core_files = ["src/core.js", "src/utils.js", "src/constants.js"]
for file in core_files:
    print(f'f("{file}")')

# Feature-based inclusion
feature_map = {
    "auth": ["src/auth.js", "src/session.js"],
    "database": ["src/db/connection.js", "src/db/models.js"],
    "caching": ["src/cache/redis.js", "src/cache/memory.js"]
}

for feature in config["features"]:
    if feature in feature_map:
        print(f'\n// Feature: {feature}')
        for file in feature_map[feature]:
            print(f'f("{file}")')

# Environment-specific files
if config["environment"] == "production":
    print('f("src/production-config.js")')
elif config["environment"] == "development":
    print('f("src/dev-config.js")')
    if config["include_tests"]:
        print('f("src/test-helpers.js")')
</jexpand>
```

### Data-Driven Template Generation

Generate templates from external data sources:

```markdown
<jexpand>
import json

# Load configuration from external file
with open('build-config.json', 'r') as f:
    build_config = json.load(f)

# Generate includes based on build configuration
for module in build_config['modules']:
    module_name = module['name']
    files = module['files']
    
    print(f'// Module: {module_name}')
    print(f'// Files: {", ".join(files)}')
    
    for file_path in files:
        if module.get('format') == 'xml':
            print(f'file_xml("{file_path}")')
        else:
            print(f'f("{file_path}")')
    
    print()  # Add spacing between modules
</jexpand>
```

### Advanced Pattern Generation

Create complex assembly patterns with Python logic:

```markdown
<jexpand>
# Generate dependency-ordered assembly
dependency_graph = {
    'constants': [],
    'utils': ['constants'],  
    'core': ['constants', 'utils'],
    'api': ['core'],
    'main': ['api']
}

# Topological sort for dependency resolution
def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = [node for node in in_degree if in_degree[node] == 0]
    result = []
    
    while queue:
        node = queue.pop(0)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

# Generate files in dependency order
sorted_modules = topological_sort(dependency_graph)

for module in sorted_modules:
    deps = dependency_graph[module]
    deps_str = ', '.join(deps) if deps else 'none'
    
    print(f'// Module: {module} (depends on: {deps_str})')
    print(f'f("src/{module}.js")')
    print()
</jexpand>
```

### Integration with Build Systems

Use Python to integrate with build tools and version control:

```markdown
<jexpand>
import subprocess
import datetime

# Get git information
try:
    git_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
    git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
    git_dirty = subprocess.call(['git', 'diff-index', '--quiet', 'HEAD']) != 0
except:
    git_hash = 'unknown'
    git_branch = 'unknown'
    git_dirty = False

# Generate build header
print(f'// Build Information')
print(f'// Generated: {datetime.datetime.now().isoformat()}')
print(f'// Git Hash: {git_hash}')
print(f'// Git Branch: {git_branch}')
print(f'// Working Directory: {"dirty" if git_dirty else "clean"}')
print(f'//')

# Get file modification times for cache busting
import os
import time

files_to_process = ['src/core.js', 'src/api.js', 'src/utils.js']
print(f'// File Modification Times:')
for file_path in files_to_process:
    if os.path.exists(file_path):
        mtime = os.path.getmtime(file_path)
        readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
        print(f'// {file_path}: {readable_time}')
        print(f'f("{file_path}")')

print(f'//')
print(f'// End Build Information')
</jexpand>
```

### Error Handling and Debugging

Handle errors gracefully in Python blocks:

```markdown
<jexpand>
import os
import sys

required_files = [
    'src/core.js',
    'src/api.js', 
    'src/config.js'
]

optional_files = [
    'src/debug.js',
    'src/analytics.js'
]

# Check required files
missing_files = []
for file in required_files:
    if not os.path.exists(file):
        missing_files.append(file)
        
if missing_files:
    print(f'// ERROR: Missing required files: {", ".join(missing_files)}')
    print(f'// Build cannot continue')
    # Note: In strict mode, jexpand will fail on missing files anyway
else:
    print(f'// All required files present')
    
    # Include required files
    for file in required_files:
        print(f'f("{file}")')
    
    # Include optional files if they exist
    for file in optional_files:
        if os.path.exists(file):
            print(f'// Optional: {file}')
            print(f'f("{file}")')
        else:
            print(f'// Skipping optional file (not found): {file}')
</jexpand>
```

### Best Practices for Python Blocks

1. **Keep Python blocks focused**: Each block should have a single, clear purpose
2. **Use descriptive comments**: Explain complex logic within Python blocks
3. **Handle errors gracefully**: Check file existence and handle exceptions
4. **Generate readable output**: Add comments and spacing to generated template code
5. **Leverage Python's ecosystem**: Use libraries like `os`, `glob`, `json`, etc.

The `<jexpand>` feature transforms jexpand from a static template processor into a dynamic, programmable file assembly system that can adapt to complex project structures and requirements.

## Advanced File Assembly Patterns

### Pattern 1: Modular JavaScript Bundle

```jinja2
// Bundle created: {{ "now" | strftime('%Y-%m-%d %H:%M:%S') }}
// Combining modules in dependency order

// Step 1: Utility functions (no dependencies)
{{ include_file('src/utils.js') }}

// Step 2: Core classes (depends on utils)
{{ include_file('src/core.js', start_line=1, end_line=200) }}

// Step 3: Feature modules (depends on core)
{{ include_file('src/features/auth.js', start_line=10) }}
{{ include_file('src/features/api.js', start_line=15) }}

// Step 4: Main application (depends on everything)
{{ include_file('src/main.js', start_line=20) }}
```

### Pattern 2: Python Package Assembly

```jinja2
#!/usr/bin/env python3
"""
Single-file distribution of {{ project_name }}
Generated from multiple source files
"""

# Imports section
{{ include_file('src/__init__.py', start_line=1, end_line=10) }}
{{ include_file('src/utils.py', start_line=1, end_line=5) }}

# Utility functions
{{ include_file('src/utils.py', start_line=6) }}

# Core classes
{% for module in ['base', 'processor', 'validator'] %}
# Module: {{ module }}.py
{{ include_file('src/' + module + '.py', start_line=10) }}

{% endfor %}

# Main interface
{{ include_file('src/api.py', start_line=15) }}
```

### Pattern 3: Configuration Assembly

```jinja2
# Combined configuration file
# Sources: {{ config_sources | join(', ') }}

{% set config_files = [
    {'file': 'config/base.yaml', 'section': 'Base configuration'},
    {'file': 'config/database.yaml', 'section': 'Database settings'},
    {'file': 'config/api.yaml', 'section': 'API configuration'},
    {'file': 'config/env/production.yaml', 'section': 'Production overrides'}
] %}

{% for config in config_files %}
# {{ config.section }}
{% if file_exists(config.file) %}
{{ include_file(config.file) }}
{% else %}
# WARNING: {{ config.file }} not found - using defaults
{% endif %}

{% endfor %}
```

## Multi-File Project Assembly

### Complex Dependency Resolution

When assembling projects with complex dependencies, use this systematic approach:

```jinja2
{#
  Step 1: Define file dependency graph
  Each entry: [file_path, dependencies, line_ranges]
#}

{% set dependency_graph = [
    {
        'file': 'lib/constants.js',
        'deps': [],
        'imports': {'start': 1, 'end': 5},
        'content': {'start': 6, 'end': -1},
        'description': 'Constants and enums'
    },
    {
        'file': 'lib/utils.js', 
        'deps': ['constants'],
        'imports': {'start': 1, 'end': 8},
        'content': {'start': 9, 'end': -1},
        'description': 'Utility functions'
    },
    {
        'file': 'lib/core.js',
        'deps': ['constants', 'utils'],
        'imports': {'start': 1, 'end': 12},
        'content': {'start': 13, 'end': -1},
        'description': 'Core functionality'
    },
    {
        'file': 'lib/api.js',
        'deps': ['core'],
        'imports': {'start': 1, 'end': 6},
        'content': {'start': 7, 'end': -1},
        'description': 'Public API'
    }
] %}

{# Step 2: Assembly in dependency order #}
// Generated bundle - dependency resolved
// Build timestamp: {{ "now" | strftime('%Y-%m-%d %H:%M:%S') }}

{% for module in dependency_graph %}
// ============================================================================
// {{ module.description }}
// Source: {{ module.file }}
// Dependencies: {{ module.deps | join(', ') if module.deps else 'none' }}
// ============================================================================

{% if module.content.end == -1 %}
{{ include_file(module.file, start_line=module.content.start) }}
{% else %}
{{ include_file(module.file, start_line=module.content.start, end_line=module.content.end) }}
{% endif %}

{% endfor %}
```

### Selective Assembly Based on Features

```jinja2
{# Feature flags - modify as needed #}
{% set features = {
    'authentication': true,
    'database': true,
    'caching': false,
    'analytics': true,
    'debug_mode': false
} %}

// Feature-based assembly
// Active features: {{ features.keys() | select | list | join(', ') }}

// Core (always included)
{{ include_file('src/core.js') }}

// Conditional features
{% if features.authentication %}
// Authentication module
{{ include_file('src/auth.js', start_line=10) }}
{% endif %}

{% if features.database %}
// Database integration
{{ include_file('src/database.js', start_line=15) }}
{% endif %}

{% if features.caching %}
// Caching layer
{{ include_file('src/cache.js', start_line=8) }}
{% endif %}

{% if features.analytics %}
// Analytics tracking
{{ include_file('src/analytics.js', start_line=12) }}
{% endif %}

{% if features.debug_mode %}
// Debug utilities (development only)
{{ include_file('src/debug.js') | comment_out('//') }}
{% endif %}
```

## Dependency Resolution Strategies

### Strategy 1: Topological Sort Assembly

```jinja2
{#
  Use this when you have a clear dependency graph
  Define dependencies explicitly and let the template resolve order
#}

{% set modules = {
    'logger': {
        'file': 'src/logger.js',
        'deps': [],
        'priority': 1
    },
    'config': {
        'file': 'src/config.js', 
        'deps': ['logger'],
        'priority': 2
    },
    'database': {
        'file': 'src/database.js',
        'deps': ['config', 'logger'],
        'priority': 3
    },
    'api': {
        'file': 'src/api.js',
        'deps': ['database', 'config'],
        'priority': 4
    }
} %}

{% for module_name in modules.keys() | sort(attribute='priority') %}
{% set module = modules[module_name] %}
// Module: {{ module_name }} (depends on: {{ module.deps | join(', ') }})
{{ include_file(module.file) }}

{% endfor %}
```

### Strategy 2: Layered Architecture Assembly

```jinja2
{# Assemble by architectural layers #}

// ============================================================================
//                              LAYER 1: FOUNDATION
// ============================================================================

// Constants and type definitions
{{ include_file('src/types.js') }}
{{ include_file('src/constants.js') }}

// ============================================================================
//                              LAYER 2: UTILITIES  
// ============================================================================

// Pure utility functions (no external dependencies)
{{ include_file('src/utils/string.js') }}
{{ include_file('src/utils/array.js') }}
{{ include_file('src/utils/object.js') }}

// ============================================================================
//                              LAYER 3: CORE SERVICES
// ============================================================================

// Infrastructure services
{{ include_file('src/services/logger.js') }}
{{ include_file('src/services/config.js') }}
{{ include_file('src/services/events.js') }}

// ============================================================================
//                              LAYER 4: BUSINESS LOGIC
// ============================================================================

// Domain models and business rules
{{ include_file('src/models/user.js') }}
{{ include_file('src/models/session.js') }}
{{ include_file('src/business/auth.js') }}
{{ include_file('src/business/validation.js') }}

// ============================================================================
//                              LAYER 5: API INTERFACE
// ============================================================================

// Public API and exports
{{ include_file('src/api/public.js') }}
{{ include_file('src/api/exports.js') }}
```

### Strategy 3: Import Analysis Assembly

```jinja2
{#
  Analyze import statements to determine assembly order
  This approach separates imports from implementation
#}

// PHASE 1: All import statements (creates namespace)
{% set js_files = [
    'src/core.js',
    'src/utils.js', 
    'src/api.js',
    'src/main.js'
] %}

{% for file in js_files %}
// Imports from {{ file }}
{{ include_file(file, start_line=1, end_line=20) | regex_replace('^(?!import|const.*require)', '// \\g<0>') }}

{% endfor %}

// PHASE 2: All implementations (provides functionality)
{% for file in js_files %}
// Implementation from {{ file }}
{{ include_file(file, start_line=21) }}

{% endfor %}
```

## Best Practices

### 1. Template Organization

```jinja2
{# Always start with metadata and configuration #}
{#
  Template: JavaScript Bundle Assembly
  Purpose: Combine modular JS files into single bundle
  Author: Development Team
  Last Updated: {{ "now" | strftime('%Y-%m-%d') }}
  
  Usage: jexpand bundle-template.md -o dist/bundle.js
#}

{# Define reusable variables #}
{% set source_dir = 'src' %}
{% set build_info = {
    'version': '1.2.3',
    'timestamp': "now" | strftime('%Y-%m-%d %H:%M:%S'),
    'environment': 'production'
} %}
```

### 2. Error Handling

```jinja2
{# Always check file existence for critical files #}
{% set required_files = ['src/core.js', 'src/api.js'] %}
{% for file in required_files %}
{% if not file_exists(file) %}
#error "Required file missing: {{ file }}"
{% endif %}
{% endfor %}

{# Graceful handling of optional files #}
{% if file_exists('src/optional-feature.js') %}
// Optional feature available
{{ include_file('src/optional-feature.js') }}
{% else %}
// Optional feature not available - using fallback
{{ include_file('src/fallback-feature.js') }}
{% endif %}
```

### 3. Documentation Integration

```jinja2
/**
 * Bundle Information
 * =================
 * Generated: {{ "now" | strftime('%Y-%m-%d %H:%M:%S') }}
 * Source Files: {{ source_files | length }} files
 * Total Lines: {{ total_lines }}
 * 
 * File Manifest:
{% for file in source_files %}
 * - {{ file.name }} (lines {{ file.start }}-{{ file.end }})
{% endfor %}
 */
```

### 4. Conditional Assembly

```jinja2
{# Environment-specific assembly #}
{% set env = environment | default('development') %}

// Environment: {{ env }}
{% if env == 'development' %}
// Development mode - include debug utilities
{{ include_file('src/debug.js') }}
{{ include_file('src/test-helpers.js') }}
{% elif env == 'production' %}
// Production mode - optimized bundle
{{ include_file('src/optimized.js') }}
{% endif %}
```

## Real-World Examples

### Example 1: React Component Library Bundle

```jinja2
{# React component library assembly #}
// React Component Library Bundle
// Generated: {{ "now" | strftime('%Y-%m-%d %H:%M:%S') }}

// React imports (only once at the top)
import React from 'react';
import PropTypes from 'prop-types';

{% set components = [
    {'name': 'Button', 'file': 'src/Button/Button.jsx'},
    {'name': 'Modal', 'file': 'src/Modal/Modal.jsx'}, 
    {'name': 'Form', 'file': 'src/Form/Form.jsx'},
    {'name': 'Table', 'file': 'src/Table/Table.jsx'}
] %}

{% for component in components %}
// ============================================================================
// {{ component.name }} Component
// ============================================================================
{{ include_file(component.file, start_line=5) }}

{% endfor %}

// Export all components
export {
{% for component in components %}
  {{ component.name }},
{% endfor %}
};
```

### Example 2: Microservice API Assembly

```jinja2
{# Microservice API assembly from multiple route files #}
const express = require('express');
const app = express();

// Middleware setup
{{ include_file('src/middleware/cors.js') }}
{{ include_file('src/middleware/auth.js') }}
{{ include_file('src/middleware/logging.js') }}

// Route handlers
{% set api_routes = [
    {'path': '/auth', 'file': 'src/routes/auth.js'},
    {'path': '/users', 'file': 'src/routes/users.js'},
    {'path': '/orders', 'file': 'src/routes/orders.js'},
    {'path': '/products', 'file': 'src/routes/products.js'}
] %}

{% for route in api_routes %}
// {{ route.path }} routes
{{ include_file(route.file, start_line=10) }}

{% endfor %}

// Server startup
{{ include_file('src/server.js', start_line=50) }}
```

### Example 3: Configuration File Assembly

```jinja2
{# Multi-environment configuration assembly #}
{% set env = environment | default('development') %}
{% set config_base = 'config/' + env %}

# {{ env.upper() }} CONFIGURATION
# Generated: {{ "now" | strftime('%Y-%m-%d %H:%M:%S') }}

# Base configuration
{{ include_file('config/base.yaml') }}

# Environment-specific overrides
{% if file_exists(config_base + '/database.yaml') %}
# Database configuration
{{ include_file(config_base + '/database.yaml') }}
{% endif %}

{% if file_exists(config_base + '/redis.yaml') %}
# Redis configuration  
{{ include_file(config_base + '/redis.yaml') }}
{% endif %}

{% if file_exists(config_base + '/security.yaml') %}
# Security settings
{{ include_file(config_base + '/security.yaml') }}
{% endif %}

# Feature flags
{% if file_exists('config/features/' + env + '.yaml') %}
{{ include_file('config/features/' + env + '.yaml') }}
{% endif %}
```

## Integration Workflows

### Development Workflow

```bash
# 1. Develop modular source files
src/
├── core.js
├── utils.js  
├── api.js
└── main.js

# 2. Create assembly template
templates/bundle.md

# 3. Generate bundle during build
jexpand templates/bundle.md -o dist/bundle.js

# 4. Test generated bundle
npm test dist/bundle.js
```

### Continuous Integration

```yaml
# .github/workflows/build.yml
- name: Generate Bundle
  run: |
    jexpand templates/production-bundle.md -o dist/app.js
    jexpand templates/development-bundle.md -o dist/app-dev.js
    
- name: Validate Bundles
  run: |
    node --check dist/app.js
    node --check dist/app-dev.js
```

### Documentation Generation

```jinja2
# API Documentation Assembly
# Combines code examples with documentation

{% for endpoint in api_endpoints %}
## {{ endpoint.name }}

{{ include_file('docs/' + endpoint.name + '.md') }}

### Code Example

```javascript
{{ include_file('examples/' + endpoint.name + '.js') }}
```

### Implementation

```javascript
{{ include_file('src/api/' + endpoint.name + '.js', start_line=20, end_line=100) }}
```

{% endfor %}
```

### Multi-Target Generation

```jinja2
{# Generate different bundles for different environments #}
{% if target == 'browser' %}
// Browser bundle - ES6 modules
{{ include_file('src/browser-entry.js') }}
{% elif target == 'node' %}  
// Node.js bundle - CommonJS
{{ include_file('src/node-entry.js') }}
{% elif target == 'worker' %}
// Web Worker bundle - minimal dependencies
{{ include_file('src/worker-entry.js') }}
{% endif %}

{# Common code for all targets #}
{{ include_file('src/shared.js') }}
```

This comprehensive guide shows how JEXPAND.md can be used to solve complex file assembly challenges while maintaining code organization and dependency management. The key is to think declaratively about what you want to achieve and use the template system to express that intent clearly.