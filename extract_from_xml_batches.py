#!/usr/bin/env python3
"""
Extract papers from arXiv XML batch files and add to database
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime


def parse_arxiv_xml_batch(xml_file):
    """Parse arXiv Atom XML feed and extract papers"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Define namespace
        ns = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }

        papers = []

        # Find all entries
        for entry in root.findall("atom:entry", ns):
            paper = {}

            # Get ID from entry ID
            id_elem = entry.find("atom:id", ns)
            if id_elem is not None:
                # Extract arXiv ID from URL like http://arxiv.org/abs/2412.05449v1
                id_url = id_elem.text
                if "/abs/" in id_url:
                    arxiv_id = id_url.split("/abs/")[1].split("v")[0]  # Remove version
                    paper["id"] = arxiv_id
                else:
                    continue
            else:
                continue

            # Get title
            title_elem = entry.find("atom:title", ns)
            paper["name"] = (
                title_elem.text.strip()
                if title_elem is not None
                else f"Paper {paper['id']}"
            )

            # Get summary/abstract
            summary_elem = entry.find("atom:summary", ns)
            if summary_elem is not None and summary_elem.text:
                abstract = summary_elem.text.strip()
                paper["focus"] = (
                    abstract[:200] + "..." if len(abstract) > 200 else abstract
                )
                paper["abstract"] = abstract
            else:
                paper["focus"] = "No description available"

            # Get authors
            authors = []
            for author in entry.findall("atom:author", ns):
                name_elem = author.find("atom:name", ns)
                if name_elem is not None:
                    authors.append(name_elem.text)
            paper["authors"] = authors

            # Get published date
            published_elem = entry.find("atom:published", ns)
            if published_elem is not None:
                paper["published"] = published_elem.text

            # Get categories
            categories = []
            for cat in entry.findall("atom:category", ns):
                term = cat.get("term")
                if term:
                    categories.append(term)
            paper["categories"] = categories

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
    except Exception as e:
        print(f"  Error parsing {xml_file}: {e}")
        return []


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
    """Main function to extract papers from batch XML files"""
    # Find batch files in papers/ directory (they're XML with .json extension)
    batch_dir = Path("papers")
    batch_files = list(batch_dir.glob("batch_*.json"))

    print(f"Found {len(batch_files)} batch files")
    print()

    # Load existing database
    database = load_existing_database()
    existing_ids = set(database["papers"].keys())

    print(f"Existing papers: {len(existing_ids)}")
    print()

    new_papers_count = 0
    skipped_count = 0
    error_count = 0

    # Process XML files
    for xml_file in sorted(xml_files):
        print(f"Processing {xml_file.name}...")

        papers = parse_arxiv_xml_batch(xml_file)
        print(f"  Found {len(papers)} papers")

        file_new = 0
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
            file_new += 1

        print(f"  Added {file_new} new papers")
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
    print(f"  Errors: {error_count}")
    print(f"  Total in database: {len(database['papers'])}")


if __name__ == "__main__":
    extract_from_batches()
