# Contributing to KH-Eghtesadino

Thank you for your interest in contributing to KH-Eghtesadino! This document provides guidelines and information about contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment (see below)
4. Create a new branch for your changes
5. Make your changes
6. Test your changes
7. Commit and push your changes
8. Create a Pull Request

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

When creating a bug report, include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please provide:
- A clear description of the feature
- The motivation/use case
- Any implementation ideas

### Contributing Code

1. **Find or create an issue** — Check existing issues or create a new one
2. **Fork and clone** — Fork the repo and clone your fork
3. **Create a branch** — Use a descriptive branch name (e.g., `feature/add-export`, `fix/login-error`)
4. **Make changes** — Follow coding standards below
5. **Test** — Ensure all tests pass
6. **Commit** — Write clear commit messages
7. **Push** — Push to your fork
8. **Create PR** — Submit a pull request

## Development Setup

### Prerequisites

- Python 3.10 or later
- `pip` package manager
- Git

### Setup Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/Eghtesadino-Finance-App-.git
cd Eghtesadino-Finance-App-

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python main.py
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Keep functions focused and concise

### Code Organization

- **Models** (`models/`): Business logic and database operations
- **Screens** (`screens/`): UI components and screen logic
- **Utils** (`utils/`): Shared utilities, constants, and helper functions

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private methods**: `_leading_underscore`

### Comments

- Use comments to explain *why*, not *what*
- Keep comments up-to-date
- Use docstrings for public APIs

## Testing

### Running Tests

```bash
# Run all tests
python tests/test_financial_features.py
python tests/run_theme_tests.py

# Run with verbose output
python -m pytest tests/ -v
```

### Writing Tests

- Add tests for new features
- Ensure tests are isolated and don't depend on external state
- Use descriptive test names
- Test both success and error cases

## Pull Request Process

### Before Submitting

1. **Update documentation** if your changes affect user-facing features
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** with a brief description of your changes

### PR Requirements

- **Clear title** — Descriptive and concise
- **Description** — Explain what the PR does and why
- **Related issues** — Link to related issues (e.g., "Fixes #123")
- **Screenshots** — For UI changes, include before/after screenshots
- **Tests** — Include test results if applicable

### Review Process

1. Maintainers will review your PR
2. You may be asked to make changes
3. Once approved, a maintainer will merge your PR

## Project Structure

```
Eghtesadino-Finance-App-/
├── main.py                 # Application entry point
├── models/                 # Business logic
├── screens/                # UI components
├── utils/                  # Shared utilities
├── tests/                  # Test files
├── assets/                 # Static assets (screenshots, etc.)
└── docs/                   # Documentation
```

## Questions?

If you have questions about contributing, feel free to:
- Open an issue with the "question" label
- Reach out to the maintainers

Thank you for contributing to KH-Eghtesadino! 🎉
