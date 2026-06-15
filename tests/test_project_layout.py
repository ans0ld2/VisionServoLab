from __future__ import annotations

import importlib.metadata
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


class ProjectLayoutTests(unittest.TestCase):
    def test_expected_project_directories_exist(self) -> None:
        expected_directories = (
            ".github/workflows",
            "configs",
            "results",
            "scripts",
            "src/vision_servo_lab",
            "tests",
            "thirdparty",
        )

        for relative_path in expected_directories:
            with self.subTest(path=relative_path):
                self.assertTrue((PROJECT_ROOT / relative_path).is_dir())

    def test_package_exposes_version(self) -> None:
        import vision_servo_lab

        self.assertEqual(vision_servo_lab.__version__, "0.1.0")

    def test_paths_point_to_thirdparty_backend_location(self) -> None:
        from vision_servo_lab.paths import PROJECT_ROOT as PACKAGE_PROJECT_ROOT
        from vision_servo_lab.paths import SO101_COPPELIA_SUBMODULE_DIR, THIRDPARTY_DIR

        self.assertEqual(PACKAGE_PROJECT_ROOT, PROJECT_ROOT)
        self.assertEqual(THIRDPARTY_DIR, PROJECT_ROOT / "thirdparty")
        self.assertEqual(SO101_COPPELIA_SUBMODULE_DIR, THIRDPARTY_DIR / "SO101_CoppeliaSim")

    def test_distribution_metadata_is_declared(self) -> None:
        pyproject_text = (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")

        self.assertIn('name = "vision-servo-lab"', pyproject_text)
        self.assertIn('requires-python = ">=3.10"', pyproject_text)
        self.assertIn('license = "MIT"', pyproject_text)

    def test_license_file_matches_project_metadata(self) -> None:
        license_text = (PROJECT_ROOT / "LICENSE").read_text(encoding="utf-8")

        self.assertIn("MIT License", license_text)


if __name__ == "__main__":
    unittest.main()
