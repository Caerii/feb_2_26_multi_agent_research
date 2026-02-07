#!/usr/bin/env python3
"""
Reorganize papers into subfolders by year
"""

import os
import shutil
from pathlib import Path


def reorganize_papers():
    papers_dir = Path("papers")

    if not papers_dir.exists():
        print("No papers directory found")
        return

    # Get all PDF files
    pdf_files = list(papers_dir.glob("*.pdf"))

    print(f"Reorganizing {len(pdf_files)} papers into year subfolders...")

    for pdf_file in pdf_files:
        # Extract year from arXiv ID (format: YYMM.NNNNN)
        paper_id = pdf_file.stem  # e.g., "2602.06039"
        year = "20" + paper_id[:2]  # e.g., "2026"

        # Create year subfolder
        year_dir = papers_dir / year
        year_dir.mkdir(exist_ok=True)

        # Move file
        dest = year_dir / pdf_file.name
        shutil.move(str(pdf_file), str(dest))

    # Show structure
    print("\nNew structure:")
    for year_dir in sorted(papers_dir.iterdir()):
        if year_dir.is_dir():
            count = len(list(year_dir.glob("*.pdf")))
            print(f"  papers/{year_dir.name}/ - {count} papers")

    print("\nDone!")


if __name__ == "__main__":
    reorganize_papers()
