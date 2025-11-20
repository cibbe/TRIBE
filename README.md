# TRIBE
Two-Mode Rotationally Symmetric Bosonic Code Error Bias

## Installation

### Prerequisites
- Python 3.8 or higher
- uv package manager (install from https://github.com/astral-sh/uv)

#### Installing uv
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip (alternative)
pip install uv
```

### Setup
```bash
# Clone the repository
git clone https://github.com/cibbe/TRIBE.git
cd TRIBE

# Install dependencies and create virtual environment
uv sync

# Or install in development mode
uv pip install -e .
```

**Note**: This project uses `uv.lock` for reproducible dependency management. The lock file is committed to version control to ensure consistent environments across different machines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this code in your research, please cite:

```
@software{tribe2025,
  title = {{TRIBE}: Two-Mode Rotation-Symmetric Bosonic Code Error Bias},
  author = {Andersson, Julius and Hiscoke, Griffin and Svensson, Carl and Zou, Hang},
  year = {2025},
  url = {https://github.com/cibbe/TRIBE}
}
```

## Acknowledgments

- Supervisors: Prof. Giulia Ferrini, Assoc. Prof. Mats Granath
- Co-supervisors: Rui Wang, Alex Maltesson, Adithi Udupa
- Examiner: Assoc. Prof. Simone Gasparinetti
