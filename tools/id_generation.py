"""
NEI Identifier Generation
=========================

Generates deterministic NDI (indicator concept) identifiers from normalized
indicator names using SHA-256 and base32 encoding.

Usage
-----
Generate an ID from the command line:

    python tools/id_generation.py "administrative processes simplified expense reporting"

Or import and use programmatically:

    from tools.id_generation import generate_ndi_id, normalize_name

ID Generation Algorithm
-----------------------
1. Normalize the name:
   - Convert to lowercase
   - Remove all characters that are not letters, digits, or spaces
   - Collapse multiple spaces to a single space
   - Strip leading and trailing whitespace

2. Hash the normalized name:
   - Encode as UTF-8
   - Compute SHA-256 digest

3. Encode:
   - Base32 encode the digest
   - Convert to lowercase
   - Strip padding characters (=)

4. Truncate and prefix:
   - Take the first 6 characters
   - Prepend "NDI-"

The result is a stable, deterministic 10-character identifier.
"""

import hashlib
import base64
import re
import sys


def normalize_name(name: str) -> str:
    """
    Normalize an indicator name for ID generation.

    Rules:
    - Lowercase
    - Remove characters that are not letters, digits, or spaces
    - Collapse multiple spaces to a single space
    - Strip leading/trailing whitespace
    """
    name = name.lower()
    name = re.sub(r"[^a-z0-9 ]", "", name)
    name = re.sub(r"\s+", " ", name)
    return name.strip()


def generate_ndi_id(normalized_name: str) -> str:
    """
    Generate a deterministic NDI identifier from a normalized indicator name.

    Args:
        normalized_name: The already-normalized indicator name.

    Returns:
        An NDI identifier of the form "NDI-xxxxxx".
    """
    digest = hashlib.sha256(normalized_name.encode("utf-8")).digest()
    b32 = base64.b32encode(digest).decode("ascii").lower().replace("=", "")
    return f"NDI-{b32[:6]}"


def generate_ndt_id(normalized_name: str) -> str:
    """
    Generate a deterministic NDT domain identifier from a normalized domain name.

    Args:
        normalized_name: The already-normalized domain name.

    Returns:
        An NDT identifier of the form "NDT-xxxxxx".
    """
    digest = hashlib.sha256(normalized_name.encode("utf-8")).digest()
    b32 = base64.b32encode(digest).decode("ascii").lower().replace("=", "")
    return f"NDT-{b32[:6]}"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("Usage: python tools/id_generation.py <indicator name>")
        print("       python tools/id_generation.py --domain <domain name>")
        sys.exit(1)

    if sys.argv[1] == "--domain":
        if len(sys.argv) < 3:
            print("Error: --domain requires a domain name argument.")
            sys.exit(1)
        raw_name = " ".join(sys.argv[2:])
        normalized = normalize_name(raw_name)
        identifier = generate_ndt_id(normalized)
        prefix = "Domain"
    else:
        raw_name = " ".join(sys.argv[1:])
        normalized = normalize_name(raw_name)
        identifier = generate_ndi_id(normalized)
        prefix = "Indicator"

    print(f"{prefix} ID:       {identifier}")
    print(f"Normalized name: {normalized}")
    print(f"Raw input:       {raw_name}")


if __name__ == "__main__":
    main()
