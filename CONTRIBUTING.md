# Contributing to CS50P

First off, thank you for considering contributing to this CS50P repository! 🎉

## 🤔 How Can I Contribute?

### Reporting Bugs

If you find a bug in any of the solutions or notice an issue:

1. **Check existing issues** to see if it's already reported
2. **Create a new issue** with a clear title and description
3. Include:
   - Steps to reproduce the issue
   - Expected behavior
   - Actual behavior
   - Python version and OS

### Suggesting Enhancements

Have ideas for improvements? Great!

1. **Open an issue** describing your enhancement
2. Explain why this enhancement would be useful
3. Provide examples if possible

### Pull Requests

#### Process

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/your-feature-name`)
3. **Make your changes** with clear, descriptive commits
4. **Test your changes** thoroughly
5. **Push to your fork** (`git push origin feature/your-feature-name`)
6. **Submit a pull request**

#### Guidelines

- Follow the existing code style
- Add comments where necessary
- Update documentation if needed
- Ensure all tests pass
- Keep commits atomic and well-described

### Code Style

This project follows the [CS50 Style Guide for Python](https://cs50.readthedocs.io/style/python/):

- Use 4 spaces for indentation (no tabs)
- Follow PEP 8 conventions
- Write descriptive variable names
- Add docstrings for functions
- Keep lines under 80 characters when reasonable

Example:
```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width
```

## 📝 Commit Message Guidelines

Write clear and meaningful commit messages:

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Start with a capital letter
- Keep the first line under 50 characters
- Add detailed description if needed

Examples:
- ✅ `Add solution for Week 3 Fuel Gauge problem`
- ✅ `Fix edge case in Vanity Plates validator`
- ✅ `Update README with testing instructions`
- ❌ `fixed stuff`
- ❌ `Update`

## ⚠️ Academic Honesty

**Important:** This repository is meant for reference and learning purposes.

- Do not submit these solutions as your own for CS50P
- Use them for guidance only after attempting problems yourself
- Follow [CS50's Academic Honesty Policy](https://cs50.harvard.edu/python/2022/honesty/)

## 🧪 Testing

Before submitting a pull request:

1. Test your code thoroughly
2. If applicable, run existing unit tests: `pytest`
3. Add new tests for new features
4. Ensure all tests pass

## 📞 Questions?

Feel free to:
- Open an issue for discussion
- Reach out via GitHub

## 🙏 Thank You!

Your contributions make this project better for everyone learning Python and CS50P!

Happy coding! 🚀
