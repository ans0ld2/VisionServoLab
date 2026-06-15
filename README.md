# VisionServoLab

Experimental visual-feedback layer for robotic servo dynamics research.

This repository is intended to sit above simulator/control backends such as
`SO101_CoppeliaSim`. The simulator backend should be added as a git submodule
under `thirdparty/SO101_CoppeliaSim`, while this repository owns visual
observation capture, synchronized metadata, and feedback-loop experiments.

## Planned Scope

- Connect to simulator/control backends through their public APIs.
- Capture visual observations synchronized with simulation time and servo telemetry.
- Store experiment artifacts in reproducible CSV/JSON/JSONL layouts.
- Evaluate how visual feedback delay, noise, and estimation errors affect servo motion quality.

## Repository Layout

```text
VisionServoLab/
├── configs/                  # Experiment configuration files
├── results/                  # Local experiment outputs, ignored by git
├── scripts/                  # Thin user-facing commands
├── src/vision_servo_lab/     # Python package
├── tests/                    # Unit tests
└── thirdparty/               # External repositories, including simulator submodules
```

## Add The Simulator Backend

After creating the GitHub repository for the simulator backend, add it as a
submodule:

```bash
git submodule add <SO101_CoppeliaSim_GIT_URL> thirdparty/SO101_CoppeliaSim
git submodule update --init --recursive
```

Keep submodule changes explicit: this repository should normally track a known
commit of the backend rather than relying on uncommitted backend edits.

## Development

```bash
uv sync
uv run python -m unittest discover -s tests -v
```

## CI

GitHub Actions runs:

```bash
uv lock --check
uv run python -m unittest discover -s tests -v
git diff --check
```

