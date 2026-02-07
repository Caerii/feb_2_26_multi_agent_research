#!/usr/bin/env python3
"""
Search papers by keywords in title, abstract, and focus
"""

import json
import re
import sys
from pathlib import Path


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def search_papers(query, database=None, search_fields=None):
    """Search papers by keywords"""
    if database is None:
        database = load_database()

    if search_fields is None:
        search_fields = ["name", "focus", "abstract", "tags"]

    papers = database["papers"]
    query_lower = query.lower()
    results = []

    for paper_id, paper in papers.items():
        score = 0
        matches = []

        # Search in name
        if "name" in search_fields and query_lower in paper["name"].lower():
            score += 10
            matches.append("name")

        # Search in focus
        if "focus" in search_fields and query_lower in paper["focus"].lower():
            score += 5
            matches.append("focus")

        # Search in abstract
        if "abstract" in search_fields and "abstract" in paper:
            if query_lower in paper["abstract"].lower():
                score += 3
                matches.append("abstract")

        # Search in tags
        if "tags" in search_fields:
            for category, tags in paper["tags"].items():
                for tag in tags:
                    if query_lower in tag.lower():
                        score += 2
                        matches.append(f"tag:{tag}")

        if score > 0:
            results.append({"paper": paper, "score": score, "matches": matches})

    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)

    return results


def print_results(results, limit=20):
    """Print search results"""
    if not results:
        print("No results found.")
        return

    print(f"\nFound {len(results)} results:\n")

    for i, result in enumerate(results[:limit], 1):
        paper = result["paper"]
        print(f"{i}. {paper['name']}")
        print(f"   ID: {paper['id']}")
        print(f"   Focus: {paper['focus'][:100]}...")
        if "abstract" in paper and paper["abstract"]:
            abstract = paper["abstract"][:150].replace("\n", " ")
            print(f"   Abstract: {abstract}...")
        print(f"   Tags: {', '.join(paper['tags']['use_case'][:3])}")
        print(
            f"   Score: {result['score']} (matched in: {', '.join(result['matches'])})"
        )
        print(f"   PDF: papers/20{paper['id'][:2]}/{paper['id']}.pdf")
        print()


def interactive_search():
    """Interactive search mode"""
    print("Multi-Agent Paper Search")
    print("=" * 50)
    print("Type 'quit' to exit, 'help' for commands")
    print()

    database = load_database()

    while True:
        query = input("\nSearch query: ").strip()

        if query.lower() == "quit":
            break

        if query.lower() == "help":
            print("\nCommands:")
            print("  quit - Exit search")
            print("  help - Show this help")
            print("  tags - Show available tags")
            print("  <keyword> - Search for papers")
            print()
            continue

        if query.lower() == "tags":
            print("\nAvailable tags:")
            print(
                "  Use-Case: #team-formation, #governance, #communication, #negotiation, #memory, #federated, #supply-chain, #task-allocation, #large-scale, #safety, #verification, #human-in-loop"
            )
            print(
                "  Technical: #marl, #deep-learning, #llm, #planning, #pddl, #formal-methods, #game-theory, #simulation, #benchmark"
            )
            print(
                "  Application: #supply-chain-logistics, #finance-trading, #healthcare, #manufacturing-ops, #scientific-discovery, #telecom, #robotics"
            )
            print()
            continue

        if not query:
            continue

        results = search_papers(query, database)
        print_results(results)


def main():
    if len(sys.argv) > 1:
        # Command line search
        query = " ".join(sys.argv[1:])
        results = search_papers(query)
        print_results(results)
    else:
        # Interactive mode
        interactive_search()


if __name__ == "__main__":
    main()
