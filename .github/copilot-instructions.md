# TRIBE - AI Coding Guidelines

## Project Overview
TRIBE (TRA200) investigates two-mode rotation-symmetric bosonic (RSB) codes by deriving their logical channels for photon loss and dephasing errors. This research project analyzes error bias in continuous-variable quantum error correction, focusing on binomial RSB codes and their performance under different noise models.

## Technology Stack
- **Language**: Python 3.x
- **Domain**: Continuous-variable quantum computing, quantum error correction
- **Libraries**: QuTiP for quantum mechanics simulations, numpy/scipy for numerical computing
- **Documentation**: LaTeX for technical reports and mathematical derivations

## Code Patterns
- Implement logical channels $\mathcal{N}_{log}$ and Pauli error probabilities ($p_x, p_y, p_z$)
- Use descriptive variable names for quantum states, operators, and code parameters ($\theta, \phi, N$)
- Structure code with classes for different RSB code families (e.g., `BinomialRSBCode`, `CatCode`)
- Implement beam splitter operations and Fock state encodings
- Include unit tests for mathematical correctness of quantum operations
- Document analytical derivations with LaTeX-style mathematical comments

## Development Workflow
- Run simulations with `python main.py` (when implemented)
- Use Jupyter notebooks in `notebooks/` for exploratory analysis
- Validate results against known quantum code benchmarks
- Document theoretical background in docstrings

## File Organization
- `src/`: Core implementation of bosonic codes and error correction
- `tests/`: Unit tests for quantum operations and code properties
- `notebooks/`: Research notebooks for analysis and visualization
- `docs/`: Theoretical documentation and research notes

## Key Conventions
- Use QuTiP for bosonic mode representations (`qutip.tensor`, `qutip.destroy`, `qutip.create`)
- Implement bosonic operators using QuTiP's harmonic oscillator functions
- Define logical states using Fock state superpositions and beam splitter operations
- Calculate error bias through Pauli transfer matrices and Kraus operators
- Use parameters: symmetry order $N$, beam splitter angles $\theta, \phi$
- Comment complex quantum algorithms with references to papers (cite TwoModeRSB, Grimsmo2019)
- Prefer functional programming for pure quantum operations
- Use type hints for clarity in scientific computing

## Research Focus
- Two-mode bosonic codes with rotational symmetry
- Error bias analysis in quantum channels (photon loss and dephasing)
- Derivation of logical channels $\mathcal{N}_{log}$ analytically and numerically
- Investigation of binomial RSB codes with varying parameters ($\theta, \phi, N$)
- Analysis of cat codes and code concatenation with repetition codes
- Optimization of error correction thresholds
- Optional: QAOA simulations with investigated codes