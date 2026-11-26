"""Resolve project-owned manuscript files without importing Template infrastructure."""

from pathlib import Path

__all__ = ["manuscript_source_dir"]


def manuscript_source_dir(project_root: Path) -> Path:
    """Use the maintained layout and support existing callers with legacy trees."""
    canonical = project_root / "docs" / "manuscript"
    legacy = project_root / "manuscript"
    if canonical.is_dir() or not legacy.is_dir():
        return canonical
    return legacy
