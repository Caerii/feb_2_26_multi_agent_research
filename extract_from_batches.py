#!/usr/bin/env python3
"""
Extract more papers from batch files and add to database
"""

import json
import re
from pathlib import Path
from datetime import datetime


def extract_arxiv_id(text):
    """Extract arXiv ID from text"""
    # Pattern: YYMM.NNNNN or YYYY.NNNNN
    patterns = [
        r"arXiv:(\d{4}\.\d{5})",
        r"arXiv:(\d{4}\.\d{4})",
        r"(\d{4}\.\d{5})",
        r"(\d{4}\.\d{4})",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def parse_batch_file(batch_file):
    """Parse a batch JSON file and extract papers"""
    with open(batch_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    papers = []

    # Handle different structures
    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict):
        if "data" in data:
            entries = data["data"]
        elif "papers" in data:
            entries = data["papers"]
        elif "results" in data:
            entries = data["results"]
        else:
            entries = [data]
    else:
        entries = []

    for entry in entries:
        if not isinstance(entry, dict):
            continue

        # Try to extract paper info
        paper = {}

        # Get ID
        if "id" in entry:
            paper["id"] = entry["id"]
        elif "arxiv_id" in entry:
            paper["id"] = entry["arxiv_id"]
        elif "title" in entry:
            paper["id"] = extract_arxiv_id(entry["title"])

        if not paper.get("id"):
            continue

        # Get title
        if "title" in entry:
            paper["name"] = entry["title"].replace("arXiv:", "").strip()
        elif "name" in entry:
            paper["name"] = entry["name"]
        else:
            paper["name"] = f"Paper {paper['id']}"

        # Get abstract/focus
        if "abstract" in entry:
            paper["focus"] = (
                entry["abstract"][:200] + "..."
                if len(entry["abstract"]) > 200
                else entry["abstract"]
            )
        elif "summary" in entry:
            paper["focus"] = entry["summary"][:200]
        elif "focus" in entry:
            paper["focus"] = entry["focus"]
        else:
            paper["focus"] = "No description available"

        # Initialize tags
        paper["tags"] = {
            "use_case": [],
            "technical": [],
            "application": [],
            "scalability": [],
            "maturity": [],
        }

        papers.append(paper)

    return papers


def load_existing_database():
    """Load existing papers database"""
    try:
        with open("papers_database.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"metadata": {}, "papers": {}}


def save_database(database):
    """Save papers database"""
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)


def extract_from_batches():
    """Main function to extract papers from batch files"""
    # Find batch files in papers/ directory
    batch_files = list(Path("papers").glob("batch_*.json"))

    print(f"Found {len(batch_files)} batch files")
    print()

    # Load existing database
    database = load_existing_database()
    existing_ids = set(database["papers"].keys())

    print(f"Existing papers: {len(existing_ids)}")
    print()

    # Load existing database
    database = load_existing_database()
    existing_ids = set(database["papers"].keys())

    print(f"Existing papers: {len(existing_ids)}")
    print()

    new_papers_count = 0
    skipped_count = 0

    # Process each batch file
    for batch_file in sorted(batch_files):
        print(f"Processing {batch_file}...")

        try:
            papers = parse_batch_file(batch_file)
            print(f"  Found {len(papers)} entries")

            for paper in papers:
                paper_id = paper.get("id")
                if not paper_id:
                    continue

                # Skip if already exists
                if paper_id in existing_ids:
                    skipped_count += 1
                    continue

                # Add to database
                database["papers"][paper_id] = paper
                existing_ids.add(paper_id)
                new_papers_count += 1

            print(f"  Added {len(papers)} papers")

        except Exception as e:
            print(f"  Error processing {batch_file}: {e}")

        print()

    # Update metadata
    database["metadata"] = {
        "total_papers": len(database["papers"]),
        "last_updated": datetime.now().isoformat(),
        "source": "arXiv cs.AI + batch files",
    }

    # Save database
    save_database(database)

    print("=" * 50)
    print(f"Extraction complete!")
    print(f"  New papers: {new_papers_count}")
    print(f"  Skipped (duplicates): {skipped_count}")
    print(f"  Total in database: {len(database['papers'])}")


if __name__ == "__main__":
    extract_from_batches()
