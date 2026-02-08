#!/usr/bin/env python3
"""
Extract ALL papers from arXiv XML batch files
Parses the Atom XML feeds and adds papers to database
"""

import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import re


def extract_arxiv_id_from_url(url):
    """Extract arXiv ID from URL like http://arxiv.org/abs/2412.05449v1"""
    if not url:
        return None
    match = re.search(r"/abs/(\d{4}\.\d{4,5})", url)
    if match:
        return match.group(1)
    return None


def parse_arxiv_xml_batch(xml_file):
    """Parse arXiv Atom XML feed and extract ALL papers"""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Define namespace
        ns = {
            "atom": "http://www.w3.org/2005/Atom",
            "arxiv": "http://arxiv.org/schemas/atom",
        }

        papers = []

        # Get total results info
        total_elem = root.find(
            ".//opensearch:totalResults",
            {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"},
        )
        if total_elem is not None:
            print(f"  Total results available: {total_elem.text}")

        # Find all entries (papers)
        entries = root.findall("atom:entry", ns)
        print(f"  Found {len(entries)} entries in this file")

        for entry in entries:
            paper = {}

            # Get ID from entry ID
            id_elem = entry.find("atom:id", ns)
            if id_elem is not None and id_elem.text:
                arxiv_id = extract_arxiv_id_from_url(id_elem.text)
                if arxiv_id:
                    paper["id"] = arxiv_id
                else:
                    continue
            else:
                continue

            # Get title
            title_elem = entry.find("atom:title", ns)
            if title_elem is not None and title_elem.text:
                paper["name"] = title_elem.text.strip()
            else:
                paper["name"] = f"Paper {paper['id']}"

            # Get summary/abstract
            summary_elem = entry.find("atom:summary", ns)
            if summary_elem is not None and summary_elem.text:
                abstract = summary_elem.text.strip()
                paper["abstract"] = abstract
                paper["focus"] = (
                    abstract[:200] + "..." if len(abstract) > 200 else abstract
                )
            else:
                paper["focus"] = "No description available"
                paper["abstract"] = ""

            # Get authors
            authors = []
            for author in entry.findall("atom:author", ns):
                name_elem = author.find("atom:name", ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text)
            paper["authors"] = authors

            # Get published date
            published_elem = entry.find("atom:published", ns)
            if published_elem is not None:
                paper["published"] = published_elem.text

            # Get updated date
            updated_elem = entry.find("atom:updated", ns)
            if updated_elem is not None:
                paper["updated"] = updated_elem.text

            # Get categories
            categories = []
            for cat in entry.findall("atom:category", ns):
                term = cat.get("term")
                if term:
                    categories.append(term)
            paper["categories"] = categories

            # Get primary category
            primary_cat = entry.find("arxiv:primary_category", ns)
            if primary_cat is not None:
                paper["primary_category"] = primary_cat.get("term")

            # Get comment
            comment_elem = entry.find("arxiv:comment", ns)
            if comment_elem is not None and comment_elem.text:
                paper["comment"] = comment_elem.text

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
        print(f"  ERROR parsing {xml_file}: {e}")
        import traceback

        traceback.print_exc()
        return []


def load_existing_database():
    """Load existing papers database"""
    try:
        with open("papers_database.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "metadata": {
                "total_papers": 0,
                "last_updated": datetime.now().isoformat(),
                "source": "arXiv cs.AI",
            },
            "papers": {},
        }


def save_database(database):
    """Save papers database"""
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)


def main():
    """Main function to extract all papers from batch XML files"""
    # Find batch files in papers/ directory
    batch_dir = Path("papers")
    batch_files = list(batch_dir.glob("batch_*.json"))

    print("=" * 70)
    print("EXTRACTING ALL PAPERS FROM BATCH FILES")
    print("=" * 70)
    print(f"\nFound {len(batch_files)} batch files")
    print()

    # Load existing database
    database = load_existing_database()
    existing_ids = set(database["papers"].keys())

    print(f"Currently in database: {len(existing_ids)} papers")
    print()

    total_new = 0
    total_skipped = 0
    total_errors = 0

    # Process each batch file
    for i, batch_file in enumerate(sorted(batch_files), 1):
        print(f"[{i}/{len(batch_files)}] Processing {batch_file.name}...")

        try:
            papers = parse_arxiv_xml_batch(batch_file)

            file_new = 0
            file_skipped = 0

            for paper in papers:
                paper_id = paper.get("id")
                if not paper_id:
                    continue

                # Skip if already exists
                if paper_id in existing_ids:
                    total_skipped += 1
                    file_skipped += 1
                    continue

                # Add to database
                database["papers"][paper_id] = paper
                existing_ids.add(paper_id)
                total_new += 1
                file_new += 1

            print(f"  -> Added {file_new} new, skipped {file_skipped} duplicates")

        except Exception as e:
            print(f"  ERROR: {e}")
            total_errors += 1

        print()

    # Update metadata
    database["metadata"] = {
        "total_papers": len(database["papers"]),
        "last_updated": datetime.now().isoformat(),
        "source": "arXiv cs.AI + batch files",
    }

    # Save database
    save_database(database)

    print("=" * 70)
    print("EXTRACTION COMPLETE")
    print("=" * 70)
    print(f"  New papers added: {total_new}")
    print(f"  Skipped (duplicates): {total_skipped}")
    print(f"  Errors: {total_errors}")
    print(f"  TOTAL IN DATABASE: {len(database['papers'])}")
    print()
    print(f"Database saved to: papers_database.json")


if __name__ == "__main__":
    main()
