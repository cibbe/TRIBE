# TRIBE
Two-Mode Rotationally Symmetric Bosonic Code Error Bias

## Project Overview

TRIBE (TRA200) investigates two-mode rotation-symmetric bosonic (RSB) codes by deriving their logical channels for photon loss and dephasing errors. This research project analyzes error bias in continuous-variable quantum error correction, focusing on binomial RSB codes and their performance under different noise models.

The project aims to:
- Derive logical channels $\mathcal{N}_{log}$ analytically and numerically
- Analyze error bias through Pauli error probabilities ($p_x, p_y, p_z$)
- Investigate binomial RSB codes with varying parameters ($\theta, \phi, N$)
- Study cat codes and code concatenation with repetition codes
- Perform QuTiP-based simulations of quantum error correction

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

### Development Setup
```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest

# Format code
uv run black src/
uv run isort src/
```

**Note**: This project uses `uv.lock` for reproducible dependency management. The lock file is committed to version control to ensure consistent environments across different machines.

## Project Structure

```
TRIBE/
├── src/                   # Core source code
├── notebooks/             # Jupyter notebooks
├── scripts/               # Utility scripts
├── data/                  # Data storage
├── .github/               # GitHub configuration
│   └── copilot-instructions.md  # AI coding guidelines
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock                # Locked dependency versions
└── README.md             # This file
```

## Usage

<!-- ### Running Simulations
```python
from src.codes.binomial_rsb import BinomialRSBCode
from src.channels.photon_loss import PhotonLossChannel

# Create a binomial RSB code
code = BinomialRSBCode(N=2, theta=np.pi/4, phi=np.pi/2)

# Apply photon loss channel
channel = PhotonLossChannel(loss_rate=0.1)
logical_channel = code.apply_channel(channel)

# Analyze error bias
bias_analysis = logical_channel.analyze_bias()
``` -->

<!-- ### Running Notebooks
```bash
# Start Jupyter notebook server
jupyter notebook

# Navigate to notebooks/ directory
``` -->

<!-- ## Key Components

### Bosonic Codes (`src/codes/`)
- `BinomialRSBCode`: Implementation of binomial rotation-symmetric bosonic codes
- `CatCode`: Cat code implementations
- Base classes for extensible code families

### Quantum Channels (`src/channels/`)
- `PhotonLossChannel`: Photon loss error model
- `DephasingChannel`: Dephasing error model
- Kraus operator representations

### Analysis Tools (`src/analysis/`)
- Error bias calculation
- Pauli transfer matrix analysis
- Logical fidelity metrics

## Research Methodology

1. **Literature Review**: Understanding RSB codes and error correction methods
2. **Single-mode Analysis**: Gain understanding with simpler single-mode cases
3. **Two-mode Implementation**: Apply methods to binomial two-mode RSB codes
4. **Parameter Investigation**: Study effects of $\theta, \phi, N$ parameters
5. **Alternative Codes**: Analyze cat codes and code concatenation
6. **Numerical Validation**: QuTiP-based simulations with physical truncations

## Testing

Run the test suite:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=src --cov-report=html
```

## Documentation

- **Technical Reports**: LaTeX documents in `reports/latex/`
- **API Documentation**: Generated from docstrings
- **Research Notes**: Jupyter notebooks with analysis

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this code in your research, please cite:

```
@software{tribe2024,
  title = {{TRIBE}: Two-Mode Rotation-Symmetric Bosonic Code Error Bias},
  author = {Andersson, Julius and Hiscoke, Griffin and Svensson, Carl and Zou, Hang},
  year = {2024},
  url = {https://github.com/cibbe/TRIBE}
}
``` -->

## Acknowledgments

- Supervisors: Prof. Giulia Ferrini, Assoc. Prof. Mats Granath
- Co-supervisors: Rui Wang, Alex Maltesson, Adithi Udupa
- Examiner: Assoc. Prof. Simone Gasparinetti
