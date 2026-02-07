#!/usr/bin/env python3
"""
Fetch paper abstracts and metadata from arXiv API
"""

import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


def fetch_arxiv_metadata(paper_id):
    """Fetch metadata from arXiv API"""
    url = f"http://export.arxiv.org/api/query?id_list={paper_id}"

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read().decode("utf-8")
            return parse_arxiv_xml(data)
    except Exception as e:
        print(f"  Error fetching {paper_id}: {e}")
        return None


def parse_arxiv_xml(xml_data):
    """Parse arXiv API XML response"""
    try:
        root = ET.fromstring(xml_data)

        # Define namespace
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        entry = root.find(".//atom:entry", ns)
        if entry is None:
            return None

        # Extract fields
        title = entry.find("atom:title", ns)
        abstract = entry.find("atom:summary", ns)
        authors = entry.findall("atom:author/atom:name", ns)
        published = entry.find("atom:published", ns)
        updated = entry.find("atom:updated", ns)
        categories = entry.findall("atom:category", ns)

        # Get PDF link
        pdf_link = None
        for link in entry.findall("atom:link", ns):
            if link.get("title") == "pdf":
                pdf_link = link.get("href")
                break

        return {
            "title": title.text.strip() if title is not None and title.text else "",
            "abstract": abstract.text.strip()
            if abstract is not None and abstract.text
            else "",
            "authors": [a.text for a in authors if a.text],
            "published": published.text if published is not None else "",
            "updated": updated.text if updated is not None else "",
            "categories": [c.get("term") for c in categories if c.get("term")],
            "pdf_url": pdf_link,
        }
    except Exception as e:
        print(f"  Error parsing XML: {e}")
        return None


def enrich_database():
    """Add abstracts and metadata to papers_database.json"""
    # Load database
    with open("papers_database.json", "r", encoding="utf-8") as f:
        database = json.load(f)

    papers = database["papers"]
    total = len(papers)

    print(f"Enriching {total} papers with arXiv metadata...")
    print("This will take about {total * 3} seconds (3 second delay between requests)")
    print()

    enriched_count = 0
    error_count = 0

    for i, (paper_id, paper) in enumerate(papers.items(), 1):
        # Skip if already has abstract
        if "abstract" in paper and paper["abstract"]:
            print(f"[{i}/{total}] {paper_id} - already enriched ✓")
            continue

        print(f"[{i}/{total}] {paper_id} - fetching...", end=" ")

        metadata = fetch_arxiv_metadata(paper_id)

        if metadata:
            paper["abstract"] = metadata["abstract"]
            paper["authors"] = metadata["authors"]
            paper["published"] = metadata["published"]
            paper["categories"] = metadata["categories"]
            paper["arxiv_title"] = metadata["title"]
            enriched_count += 1
            print("✓")
        else:
            error_count += 1
            print("✗")

        # Be nice to arXiv API
        time.sleep(3)

        # Save progress every 10 papers
        if i % 10 == 0:
            with open("papers_database.json", "w", encoding="utf-8") as f:
                json.dump(database, f, indent=2, ensure_ascii=False)
            print(f"  Saved progress ({i}/{total})")

    # Final save
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print()
    print(f"Enrichment complete!")
    print(f"  Enriched: {enriched_count}")
    print(f"  Errors: {error_count}")
    print(f"  Total: {total}")


if __name__ == "__main__":
    enrich_database()
