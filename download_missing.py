#!/usr/bin/env python3
"""
Download only missing papers
"""

import json
import os
import requests
import time
from pathlib import Path


def get_downloaded_papers():
    """Get set of already downloaded paper IDs"""
    downloaded = set()
    papers_dir = Path("papers")

    if not papers_dir.exists():
        return downloaded

    for year_dir in papers_dir.iterdir():
        if year_dir.is_dir():
            for pdf_file in year_dir.glob("*.pdf"):
                downloaded.add(pdf_file.stem)

    return downloaded


def download_paper(paper_id, base_dir="papers"):
    """Download paper PDF from arXiv"""
    url = f"https://arxiv.org/pdf/{paper_id}.pdf"

    # Extract year and create subfolder
    year = "20" + paper_id[:2]
    output_dir = os.path.join(base_dir, year)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{paper_id}.pdf")

    # Skip if already exists
    if os.path.exists(output_path):
        return True, "exists"

    try:
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(response.content)
            return True, "downloaded"
        else:
            return False, f"HTTP {response.status_code}"
    except Exception as e:
        return False, str(e)


def main():
    # Load database
    with open("papers_database.json", "r", encoding="utf-8") as f:
        database = json.load(f)

    papers = database["papers"]

    # Get already downloaded papers
    downloaded = get_downloaded_papers()
    print(f"Already downloaded: {len(downloaded)} papers")

    # Find missing papers
    missing = [(pid, paper) for pid, paper in papers.items() if pid not in downloaded]
    print(f"Missing: {len(missing)} papers")
    print()

    if not missing:
        print("All papers already downloaded!")
        return

    print(f"Downloading {len(missing)} missing papers...")
    print()

    success = 0
    failed = 0

    for i, (paper_id, paper) in enumerate(missing, 1):
        # Safe print for Unicode
        paper_name = paper.get("name", paper_id)
        try:
            print(f"[{i}/{len(missing)}] {paper_id}", end=" ")
        except:
            print(f"[{i}/{len(missing)}] {paper_id}", end=" ")

        result, status = download_paper(paper_id)

        if result:
            success += 1
            print(f"- OK")
        else:
            failed += 1
            print(f"- FAIL ({status})")

        time.sleep(1)

    print()
    print(f"Download complete!")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")
    print(f"  Total missing: {len(missing)}")


if __name__ == "__main__":
    main()
