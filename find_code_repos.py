#!/usr/bin/env python3
"""
Scrape GitHub and code repository links from papers
"""

import json
import re
from pathlib import Path


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def extract_code_links(text):
    """Extract GitHub and code repository links from text"""
    if not text:
        return []

    links = []

    # GitHub patterns
    github_patterns = [
        r"github\.com/[\w-]+/[\w-]+",
        r"github\.com/[\w-]+/[\w-]+/[\w-]+",
    ]

    for pattern in github_patterns:
        matches = re.findall(pattern, text)
        links.extend(["https://" + m for m in matches])

    # General code repo patterns
    code_patterns = [
        r"(gitlab\.com/[\w-]+/[\w-]+)",
        r"(bitbucket\.org/[\w-]+/[\w-]+)",
        r"(sourceforge\.net/projects/[\w-]+)",
    ]

    for pattern in code_patterns:
        matches = re.findall(pattern, text)
        links.extend(["https://" + m for m in matches])

    # Remove duplicates
    return list(set(links))


def find_code_repositories():
    """Find code repositories for all papers"""
    database = load_database()
    papers = database["papers"]

    print(f"Scanning {len(papers)} papers for code repositories...")
    print()

    papers_with_code = 0
    total_links = 0

    for pid, paper in papers.items():
        # Combine all text fields
        text = " ".join(
            [
                paper.get("abstract", ""),
                paper.get("focus", ""),
                paper.get("comment", ""),
                paper.get("name", ""),
            ]
        )

        links = extract_code_links(text)

        if links:
            paper["code_links"] = links
            papers_with_code += 1
            total_links += len(links)
            print(f"[{pid}] {paper['name'][:50]}...")
            for link in links:
                print(f"    -> {link}")

    # Save updated database
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("CODE REPOSITORY SCAN COMPLETE")
    print("=" * 70)
    print(f"  Papers with code: {papers_with_code}/{len(papers)}")
    print(f"  Total links found: {total_links}")
    print(f"  Percentage: {papers_with_code / len(papers) * 100:.1f}%")


def main():
    find_code_repositories()


if __name__ == "__main__":
    main()
