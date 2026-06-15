from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIGS_DIR = PROJECT_ROOT / "configs"
RESULTS_DIR = PROJECT_ROOT / "results"
THIRDPARTY_DIR = PROJECT_ROOT / "thirdparty"
SO101_COPPELIA_SUBMODULE_DIR = THIRDPARTY_DIR / "SO101_CoppeliaSim"

