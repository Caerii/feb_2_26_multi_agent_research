#!/usr/bin/env python3
"""
Download papers from arXiv based on papers_database.json
"""

import json
import os
import requests
import time
from pathlib import Path


def download_paper(paper_id, base_dir="papers"):
    """Download paper PDF from arXiv into year subfolder"""
    # arXiv ID format: YYMM.NNNNN
    url = f"https://arxiv.org/pdf/{paper_id}.pdf"

    # Extract year and create subfolder
    year = "20" + paper_id[:2]  # e.g., "2602.06039" -> "2026"
    output_dir = os.path.join(base_dir, year)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    output_path = os.path.join(output_dir, f"{paper_id}.pdf")

    # Skip if already exists
    if os.path.exists(output_path):
        print(f"  [SKIP] {paper_id} - already exists")
        return True

    try:
        print(f"  [DOWNLOAD] {paper_id}...", end=" ")
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            print("OK")
            return True
        else:
            print(f"FAIL (HTTP {response.status_code})")
            return False
    except Exception as e:
        print(f"FAIL ({str(e)})")
        return False


def main():
    # Load database
    with open("papers_database.json", "r", encoding="utf-8") as f:
        database = json.load(f)

    papers = database["papers"]
    total = len(papers)

    print(f"Downloading {total} papers from arXiv...")
    print(f"Output directory: papers/YYYY/")
    print()

    success_count = 0
    fail_count = 0

    for i, (paper_id, paper) in enumerate(papers.items(), 1):
        print(f"[{i}/{total}] {paper['name']}")

        if download_paper(paper_id):
            success_count += 1
        else:
            fail_count += 1

        # Be nice to arXiv servers
        time.sleep(1)

    print()
    print(f"Download complete!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Total: {total}")


if __name__ == "__main__":
    main()
