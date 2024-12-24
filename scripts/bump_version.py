import re
from pathlib import Path


def bump_version(version_file: str, bump_type: str = "patch") -> str:
    """
    Bump the version number in the specified file.

    Args:
        version_file: Path to the version file
        bump_type: One of 'major', 'minor', or 'patch'

    Returns:
        The new version string
    """
    version_path = Path(version_file)
    content = version_path.read_text()

    # Extract current version
    version_match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if not version_match:
        raise ValueError("Could not find version string")

    current_version = version_match.group(1)
    major, minor, patch = map(int, current_version.split("."))

    # Bump version according to type
    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")

    new_version = f"{major}.{minor}.{patch}"

    # Update the file
    new_content = content.replace(
        f'__version__ = "{current_version}"', f'__version__ = "{new_version}"'
    )
    version_path.write_text(new_content)

    return new_version


if __name__ == "__main__":
    import sys

    version_file = sys.argv[1]
    bump_type = sys.argv[2] if len(sys.argv) > 2 else "patch"
    new_version = bump_version(version_file, bump_type)
    print(new_version)
