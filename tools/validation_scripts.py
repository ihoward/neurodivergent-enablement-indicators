"""
NEI Repository Validation
==========================

Validates the integrity of the NEI repository by checking:

1. No duplicate indicator IDs across concept files
2. No duplicate version IDs across version files
3. All version files reference a valid concept ID
4. Taxonomy node and edge files reference valid IDs
5. Release manifests reference only Standard indicator IDs (NDI-xxxxxx-vN format)
6. Release manifests reference a valid taxonomy version
7. ID format conformance for all files

Usage
-----
Run from the repository root:

    python tools/validation_scripts.py

Or check only a specific release:

    python tools/validation_scripts.py --release NDR-1.0.0

Exit codes:
    0 — all checks passed
    1 — one or more validation errors found
"""

import os
import re
import sys
import csv
import yaml
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).parent.parent
CONCEPTS_DIR = REPO_ROOT / "indicators" / "concepts"
VERSIONS_DIR = REPO_ROOT / "indicators" / "versions"
TAXONOMY_NODES_DIR = REPO_ROOT / "taxonomy" / "nodes"
TAXONOMY_EDGES_DIR = REPO_ROOT / "taxonomy" / "edges"
RELEASES_DIR = REPO_ROOT / "releases"

CONCEPT_ID_PATTERN = re.compile(r"^NDI-[a-z0-9]{6}$")
VERSION_ID_PATTERN = re.compile(r"^NDI-[a-z0-9]{6}-v\d+$")
# Standard: NDT-1.0.0  |  Candidate: NDT-0.1.0C-NDP-seed
TAXONOMY_VERSION_PATTERN = re.compile(r"^NDT-\d+\.\d+\.\d+([CP]-\S+)?$")
# Standard: NDR-1.0.0  |  Candidate: NDR-0.1.0C-NDP-seed
RELEASE_ID_PATTERN = re.compile(r"^NDR-\d+\.\d+\.\d+([CP]-\S+)?$")


class ValidationError:
    def __init__(self, file: str, message: str):
        self.file = file
        self.message = message

    def __str__(self):
        return f"  [{self.file}] {self.message}"


def load_yaml(path: Path) -> Optional[dict]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        return None


def load_csv(path: Path) -> Optional[list[dict]]:
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except Exception as e:
        return None


def check_concept_files(errors: list[ValidationError]) -> set[str]:
    """Check indicator concept files and return set of valid concept IDs."""
    concept_ids = set()

    for path in sorted(CONCEPTS_DIR.glob("*.yaml")):
        data = load_yaml(path)
        if data is None:
            errors.append(ValidationError(path.name, "Could not parse YAML."))
            continue

        # Check required fields
        for field in ("id", "normalized_name", "title", "description", "evidence_categories"):
            if field not in data:
                errors.append(ValidationError(path.name, f"Missing required field: {field}"))

        concept_id = data.get("id", "")

        # Check ID format
        if not CONCEPT_ID_PATTERN.match(concept_id):
            errors.append(ValidationError(path.name, f"Invalid concept ID format: {concept_id}"))

        # Check for duplicates
        if concept_id in concept_ids:
            errors.append(ValidationError(path.name, f"Duplicate concept ID: {concept_id}"))
        else:
            concept_ids.add(concept_id)

        # Check filename matches ID
        expected_filename = f"{concept_id}.yaml"
        if path.name != expected_filename:
            errors.append(ValidationError(path.name, f"Filename should be {expected_filename}"))

    return concept_ids


def check_version_files(concept_ids: set[str], errors: list[ValidationError]) -> set[str]:
    """Check indicator version files and return set of valid version IDs."""
    version_ids = set()

    for path in sorted(VERSIONS_DIR.glob("*.yaml")):
        data = load_yaml(path)
        if data is None:
            errors.append(ValidationError(path.name, "Could not parse YAML."))
            continue

        # Check required fields
        for field in ("id", "concept_id", "criteria"):
            if field not in data:
                errors.append(ValidationError(path.name, f"Missing required field: {field}"))

        version_id = data.get("id", "")
        concept_id = data.get("concept_id", "")

        # Check ID format
        if not VERSION_ID_PATTERN.match(version_id):
            errors.append(ValidationError(path.name, f"Invalid version ID format: {version_id}"))

        # Check for duplicates
        if version_id in version_ids:
            errors.append(ValidationError(path.name, f"Duplicate version ID: {version_id}"))
        else:
            version_ids.add(version_id)

        # Check concept_id references a valid concept
        if concept_id and concept_id not in concept_ids:
            errors.append(ValidationError(path.name, f"concept_id {concept_id} does not match any concept file."))

        # Check version references the right concept
        if version_id and concept_id:
            if not version_id.startswith(concept_id):
                errors.append(ValidationError(path.name, f"Version ID {version_id} does not match concept_id {concept_id}"))

        # Check filename matches ID
        expected_filename = f"{version_id}.yaml"
        if path.name != expected_filename:
            errors.append(ValidationError(path.name, f"Filename should be {expected_filename}"))

    return version_ids


def check_taxonomy_files(concept_ids: set[str], errors: list[ValidationError]) -> set[str]:
    """Check taxonomy node and edge files and return valid taxonomy version IDs."""
    taxonomy_versions = set()
    all_node_ids = set()

    # Check node files
    for path in sorted(TAXONOMY_NODES_DIR.glob("*-nodes.csv")):
        # Extract version from filename: NDT-x.x.x-nodes.csv
        stem = path.stem.replace("-nodes", "")
        if not TAXONOMY_VERSION_PATTERN.match(stem):
            errors.append(ValidationError(path.name, f"Cannot determine taxonomy version from filename."))
            continue

        taxonomy_versions.add(stem)
        rows = load_csv(path)
        if rows is None:
            errors.append(ValidationError(path.name, "Could not parse CSV."))
            continue

        node_ids = set()
        for row in rows:
            node_id = row.get("node_id", "").strip()
            if node_id in node_ids:
                errors.append(ValidationError(path.name, f"Duplicate node_id: {node_id}"))
            node_ids.add(node_id)
            all_node_ids.add(node_id)

            # Indicator nodes must match concept IDs; root and domain nodes are exempt
            node_type = row.get("node_type", "").strip()
            if node_type == "indicator" and node_id not in concept_ids:
                errors.append(ValidationError(path.name, f"Indicator node {node_id} has no corresponding concept file."))

    # Check edge files
    for path in sorted(TAXONOMY_EDGES_DIR.glob("*-edges.csv")):
        rows = load_csv(path)
        if rows is None:
            errors.append(ValidationError(path.name, "Could not parse CSV."))
            continue

        for row in rows:
            source_id = row.get("source_id", "").strip()
            target_id = row.get("target_id", "").strip()

            if source_id not in all_node_ids:
                errors.append(ValidationError(path.name, f"Edge references unknown source_id: {source_id}"))
            if target_id not in all_node_ids:
                errors.append(ValidationError(path.name, f"Edge references unknown target_id: {target_id}"))

    return taxonomy_versions


def check_release_files(version_ids: set[str], taxonomy_versions: set[str],
                        errors: list[ValidationError], target_release: Optional[str] = None):
    """Check release manifest files."""
    pattern = f"{target_release}.yaml" if target_release else "NDR-*.yaml"

    for path in sorted(RELEASES_DIR.glob(pattern if target_release else "NDR-*.yaml")):
        if path.name in ("NDR-template.yaml",):
            continue

        data = load_yaml(path)
        if data is None:
            errors.append(ValidationError(path.name, "Could not parse YAML."))
            continue

        # Check required fields — accept either "indicators" or "indicator_versions"
        indicators_field = "indicators" if "indicators" in data else "indicator_versions"
        for field in ("release_id", "taxonomy_id"):
            if field not in data:
                errors.append(ValidationError(path.name, f"Missing required field: {field}"))
        if "indicators" not in data and "indicator_versions" not in data:
            errors.append(ValidationError(path.name, "Missing required field: indicators (or indicator_versions)"))

        release_id = data.get("release_id", "")
        taxonomy_id = data.get("taxonomy_id", "")
        indicators = data.get(indicators_field, [])
        is_candidate = bool(re.search(r"[CP]-", release_id))

        # Check release ID format
        if not RELEASE_ID_PATTERN.match(release_id):
            errors.append(ValidationError(path.name, f"Invalid release ID format: {release_id}"))

        # Check taxonomy version exists
        if taxonomy_id and taxonomy_id not in taxonomy_versions:
            errors.append(ValidationError(path.name, f"taxonomy_id {taxonomy_id} has no corresponding taxonomy files."))

        # Standard releases: indicators must be Standard format and exist
        # Candidate releases: indicators must exist in version files (candidate status allowed)
        for ind_id in indicators:
            if not VERSION_ID_PATTERN.match(ind_id):
                errors.append(ValidationError(path.name, f"Indicator {ind_id} is not in Standard version format (NDI-xxxxxx-vN)."))
            elif ind_id not in version_ids:
                errors.append(ValidationError(path.name, f"Indicator {ind_id} has no corresponding version file."))

        # Check for duplicates within release
        seen = set()
        for ind_id in indicators:
            if ind_id in seen:
                errors.append(ValidationError(path.name, f"Duplicate indicator in release: {ind_id}"))
            seen.add(ind_id)


def run_validation(target_release: Optional[str] = None) -> int:
    errors: list[ValidationError] = []

    print("NEI Repository Validation")
    print("=" * 40)
    print(f"Repository root: {REPO_ROOT}")
    print()

    print("Checking indicator concept files...")
    concept_ids = check_concept_files(errors)
    print(f"  Found {len(concept_ids)} concept(s).")

    print("Checking indicator version files...")
    version_ids = check_version_files(concept_ids, errors)
    print(f"  Found {len(version_ids)} version(s).")

    print("Checking taxonomy files...")
    taxonomy_versions = check_taxonomy_files(concept_ids, errors)
    print(f"  Found {len(taxonomy_versions)} taxonomy version(s).")

    print("Checking release manifests...")
    check_release_files(version_ids, taxonomy_versions, errors, target_release)

    print()
    if errors:
        print(f"FAILED — {len(errors)} error(s) found:")
        for error in errors:
            print(str(error))
        return 1
    else:
        print("PASSED — all checks passed.")
        return 0


def main():
    target_release = None
    if len(sys.argv) >= 3 and sys.argv[1] == "--release":
        target_release = sys.argv[2]

    exit_code = run_validation(target_release)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
