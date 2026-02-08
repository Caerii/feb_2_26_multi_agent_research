#!/usr/bin/env python3
"""
Enrich all papers with abstracts, authors, and metadata from arXiv API
"""

import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime


def fetch_arxiv_metadata(paper_id):
    """Fetch metadata from arXiv API"""
    url = f"http://export.arxiv.org/api/query?id_list={paper_id}"

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode("utf-8")
            return parse_arxiv_xml(data)
    except Exception as e:
        print(f"    Error: {e}")
        return None


def parse_arxiv_xml(xml_data):
    """Parse arXiv API XML response"""
    try:
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        entry = root.find(".//atom:entry", ns)
        if entry is None:
            return None

        # Extract fields
        title = entry.find("atom:title", ns)
        abstract = entry.find("atom:summary", ns)
        authors = entry.findall("atom:author/atom:name", ns)
        published = entry.find("atom:published", ns)
        categories = entry.findall("atom:category", ns)

        return {
            "title": title.text.strip() if title is not None and title.text else "",
            "abstract": abstract.text.strip()
            if abstract is not None and abstract.text
            else "",
            "authors": [a.text for a in authors if a.text],
            "published": published.text if published is not None else "",
            "categories": [c.get("term") for c in categories if c.get("term")],
        }
    except Exception as e:
        print(f"    Parse error: {e}")
        return None


def main():
    # Load database
    print("Loading database...")
    with open("papers_database.json", "r", encoding="utf-8") as f:
        database = json.load(f)

    papers = database["papers"]

    # Find papers needing enrichment
    to_enrich = [
        (pid, paper)
        for pid, paper in papers.items()
        if not paper.get("abstract") or not paper.get("authors")
    ]

    total = len(to_enrich)
    print(f"Found {total} papers needing enrichment")
    print(f"Estimated time: {total * 3} seconds ({total * 3 / 60:.1f} minutes)")
    print()

    enriched = 0
    failed = 0

    for i, (paper_id, paper) in enumerate(to_enrich, 1):
        print(f"[{i}/{total}] {paper_id} - {paper['name'][:50]}...")

        metadata = fetch_arxiv_metadata(paper_id)

        if metadata:
            paper["abstract"] = metadata["abstract"]
            paper["authors"] = metadata["authors"]
            paper["published"] = metadata["published"]
            paper["categories"] = metadata["categories"]
            paper["arxiv_title"] = metadata["title"]
            enriched += 1
            print(
                f"    ✓ Enriched ({len(metadata['authors'])} authors, {len(metadata['abstract'])} chars)"
            )
        else:
            failed += 1
            print(f"    [FAIL] Failed")

        # Save every 10 papers
        if i % 10 == 0:
            with open("papers_database.json", "w", encoding="utf-8") as f:
                json.dump(database, f, indent=2, ensure_ascii=False)
            print(f"    Saved progress")

        # Respect arXiv rate limits
        time.sleep(3)

    # Final save
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("ENRICHMENT COMPLETE")
    print("=" * 70)
    print(f"  Enriched: {enriched}")
    print(f"  Failed: {failed}")
    print(f"  Total: {total}")


if __name__ == "__main__":
    main()
