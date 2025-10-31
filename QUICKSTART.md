# Quick Start Guide

Get up and running with the CS50P repository in 5 minutes! ⚡

## 🚀 Super Quick Start

```bash
# Clone and enter the repository
git clone https://github.com/N1KH1LT0X1N/CS50P.git
cd CS50P

# Install dependencies
pip install -r requirements.txt

# Run a solution
cd week0/ps0/einstein
python einstein.py

# Run tests
cd ../../..
pytest
```

## 📦 What You'll Need

- **Python 3.11+** → [Download](https://www.python.org/downloads/)
- **Git** → [Download](https://git-scm.com/downloads)
- **pip** (comes with Python)

## 🎯 Common Tasks

### Run a Specific Problem

```bash
# Week 0 - Einstein
cd week0/ps0/einstein && python einstein.py

# Week 1 - Bank
cd week1/ps1/bank && python bank.py

# Week 2 - Vanity Plates
cd week2/ps2/plates && python plates.py
```

### Run Tests

```bash
# All tests
pytest

# Specific week
pytest week2/

# Specific problem with verbose output
pytest week2/ps2/plates/test_plates.py -v

# With coverage
pytest --cov=. --cov-report=html
```

### Use Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 📁 Repository Structure at a Glance

```
CS50P/
├── week0/ps0/         # 5 problems (Indoor, Playback, Faces, Einstein, Tip)
├── week1/ps1/         # 5 problems (Deep, Bank, Extensions, Interpreter, Meal)
├── week2/ps2/         # 5 problems (camelCase, Coke, Nutrition, Plates, twttr)
├── week3-9/           # More weeks to explore!
└── requirements.txt   # All dependencies
```

## 🎓 Learning Path

1. **Start with Week 0** - Learn basics of functions and variables
2. **Progress sequentially** - Each week builds on previous concepts
3. **Read the README** - Each week has detailed explanations
4. **Try before looking** - Attempt problems yourself first
5. **Run the tests** - Verify your understanding

## 🐛 Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Python not found"
Make sure Python is in your PATH, or use:
```bash
python3 einstein.py  # On macOS/Linux
py einstein.py       # Alternative on Windows
```

### Tests not running
```bash
pip install pytest
pytest --version
```

## 📚 Next Steps

- [ ] Read the full [README.md](README.md)
- [ ] Check out [DOCUMENTATION.md](DOCUMENTATION.md) for detailed guides
- [ ] Review [CONTRIBUTING.md](CONTRIBUTING.md) if you want to contribute
- [ ] Join the [CS50 Discord](https://discord.gg/cs50)

## 💡 Pro Tips

1. **Use VS Code** - Great Python support with extensions
2. **Enable virtual environment** - Keeps dependencies isolated
3. **Run tests often** - Catch issues early
4. **Read error messages** - They're helpful!
5. **Check CS50 docs** - When stuck, official resources help

## 🎉 You're Ready!

Happy coding! If you get stuck, check the documentation or open an issue.

---

[← Back to Main README](README.md) | [View Documentation](DOCUMENTATION.md)
