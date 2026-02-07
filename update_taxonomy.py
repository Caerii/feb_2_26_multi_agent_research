#!/usr/bin/env python3
"""
Update TAXONOMY.md with actual data from papers_database.json
"""

import json
from collections import defaultdict


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_taxonomy():
    database = load_database()
    papers = database["papers"]

    # Build tag index
    tag_index = defaultdict(lambda: defaultdict(list))
    for paper_id, paper in papers.items():
        for category, tags in paper["tags"].items():
            for tag in tags:
                tag_index[category][tag].append(paper)

    taxonomy = f"""# Multi-Agent Paper Taxonomy for Virtual Organizations

**Total Papers:** {len(papers)}  
**Source:** arXiv cs.AI  
**Focus:** Virtual AI companies and autonomous organizations  
**Last Updated:** 2026-02-07

This document provides multiple organization views for the multi-agent papers compiled in this repository, enabling different audiences to find papers relevant to their needs.

---

## View 1: By Use-Case

### 1.1 Team Formation & Organization
*Forming and structuring multi-agent teams*

"""

    # Use-Case sections
    use_case_sections = [
        (
            "#team-formation",
            "1.1 Team Formation & Organization",
            "Forming and structuring multi-agent teams",
        ),
        (
            "#governance",
            "1.2 Governance & Norms",
            "Rules, norms, and formal frameworks",
        ),
        (
            "#communication",
            "1.3 Communication & Coordination",
            "Protocols for agent interaction",
        ),
        (
            "#negotiation",
            "1.4 Negotiation & Economics",
            "Bargaining and market mechanisms",
        ),
        ("#memory", "1.5 Memory & Knowledge", "Agent memory and knowledge sharing"),
        (
            "#federated",
            "1.6 Federated Learning",
            "Privacy-preserving distributed learning",
        ),
        (
            "#supply-chain",
            "1.7 Supply Chain & Operations",
            "Inventory, logistics, operations",
        ),
        ("#task-allocation", "1.8 Task Allocation", "Work distribution and scheduling"),
        ("#large-scale", "1.9 Large-Scale Systems", "100+ agent coordination"),
        ("#safety", "1.10 Safety & Security", "Robustness and rogue agent prevention"),
        (
            "#verification",
            "1.11 Verification & Formal Methods",
            "Logic, proofs, guarantees",
        ),
        ("#human-in-loop", "1.12 Human-AI Collaboration", "Human-agent interaction"),
    ]

    for tag, section_id, description in use_case_sections:
        if tag in tag_index["use_case"]:
            papers_in_tag = tag_index["use_case"][tag]
            taxonomy += f"""### {section_id}
*{description}*

| Paper | ID | Key Relevance |
|-------|-----|---------------|
"""
            for paper in sorted(papers_in_tag, key=lambda x: x["name"]):
                taxonomy += (
                    f"| {paper['name']} | {paper['id']} | {paper['focus'][:60]}... |\n"
                )
            taxonomy += "\n"

    # Technical Approach
    taxonomy += """---

## View 2: By Technical Approach

"""

    technical_sections = [
        ("#marl", "2.1 Multi-Agent RL", "MARL and deep RL"),
        ("#deep-learning", "2.2 Deep Learning", "Neural architectures"),
        ("#llm", "2.3 LLM-Based Systems", "Large language model agents"),
        ("#planning", "2.4 Planning & PDDL", "Task planning"),
        ("#formal-methods", "2.5 Formal Methods", "Logic and verification"),
        ("#game-theory", "2.6 Game Theory", "Economic approaches"),
        ("#simulation", "2.7 Simulation", "Frameworks and benchmarks"),
    ]

    for tag, section_id, description in technical_sections:
        if tag in tag_index["technical"]:
            papers_in_tag = tag_index["technical"][tag]
            taxonomy += f"""### {section_id}
*{description}*

| Paper | ID | Type |
|-------|-----|------|
"""
            for paper in sorted(papers_in_tag, key=lambda x: x["name"])[:15]:
                maturity = (
                    paper["tags"]["maturity"][0]
                    if paper["tags"]["maturity"]
                    else "Research"
                )
                taxonomy += f"| {paper['name']} | {paper['id']} | {maturity} |\n"
            if len(papers_in_tag) > 15:
                taxonomy += f"| *...and {len(papers_in_tag) - 15} more* | | |\n"
            taxonomy += "\n"

    # Application Domain
    taxonomy += """---

## View 3: By Application Domain

"""

    app_sections = [
        ("#supply-chain-logistics", "3.1 Supply Chain & Logistics"),
        ("#finance-trading", "3.2 Finance & Trading"),
        ("#healthcare", "3.3 Healthcare"),
        ("#manufacturing-ops", "3.4 Manufacturing & Operations"),
        ("#scientific-discovery", "3.5 Scientific Discovery"),
        ("#telecom", "3.6 Telecommunications"),
        ("#robotics", "3.7 Robotics & Physical Systems"),
    ]

    for tag, section_id in app_sections:
        if tag in tag_index["application"]:
            papers_in_tag = tag_index["application"][tag]
            taxonomy += f"""### {section_id}

| Paper | ID | Use |
|-------|-----|-----|
"""
            for paper in sorted(papers_in_tag, key=lambda x: x["name"]):
                taxonomy += (
                    f"| {paper['name']} | {paper['id']} | {paper['focus'][:50]} |\n"
                )
            taxonomy += "\n"

    # Scalability
    taxonomy += """---

## View 4: By Scalability

"""

    scale_sections = [
        ("#scale-small", "4.1 Small Scale (2-10 agents)"),
        ("#scale-medium", "4.2 Medium Scale (10-100 agents)"),
        ("#scale-large", "4.3 Large Scale (100-1000 agents)"),
        ("#scale-massive", "4.4 Massive Scale (1000+ agents)"),
    ]

    for tag, section_id in scale_sections:
        if tag in tag_index["scalability"]:
            papers_in_tag = tag_index["scalability"][tag]
            taxonomy += f"""### {section_id}

| Paper | ID | Context |
|-------|-----|---------|
"""
            for paper in sorted(papers_in_tag, key=lambda x: x["name"])[:10]:
                taxonomy += (
                    f"| {paper['name']} | {paper['id']} | {paper['focus'][:50]} |\n"
                )
            if len(papers_in_tag) > 10:
                taxonomy += f"| *...and {len(papers_in_tag) - 10} more* | | |\n"
            taxonomy += "\n"

    # Cross-reference
    taxonomy += """---

## Cross-Reference: Papers by Multiple Dimensions

Sample of papers showing how they span multiple categories:

| ID | Paper | Use-Case | Technical | AppDomain | Scale | Maturity |
|----|-------|----------|-----------|-----------|-------|----------|
"""

    # Sample cross-reference
    sample_papers = list(papers.values())[:15]
    for paper in sample_papers:
        uc = paper["tags"]["use_case"][0] if paper["tags"]["use_case"] else "-"
        tech = paper["tags"]["technical"][0] if paper["tags"]["technical"] else "-"
        app = paper["tags"]["application"][0] if paper["tags"]["application"] else "-"
        scale = paper["tags"]["scalability"][0] if paper["tags"]["scalability"] else "-"
        mat = paper["tags"]["maturity"][0] if paper["tags"]["maturity"] else "-"

        name_short = (
            paper["name"][:25] + "..." if len(paper["name"]) > 25 else paper["name"]
        )
        taxonomy += f"| {paper['id']} | {name_short} | {uc} | {tech} | {app} | {scale} | {mat} |\n"

    taxonomy += """
---

## Tagging System

For future papers, use this tagging system:

### Use-Case Tags
"""

    # Add tag counts
    for tag, count in sorted(tag_index["use_case"].items(), key=lambda x: -len(x[1])):
        if tag != "#general":
            taxonomy += f"- `{tag}` ({len(tag_index['use_case'][tag])} papers)\n"

    taxonomy += "\n### Technical Tags\n"
    for tag, count in sorted(tag_index["technical"].items(), key=lambda x: -len(x[1])):
        if tag != "#general":
            taxonomy += f"- `{tag}` ({len(tag_index['technical'][tag])} papers)\n"

    taxonomy += "\n### Application Tags\n"
    for tag, count in sorted(
        tag_index["application"].items(), key=lambda x: -len(x[1])
    ):
        if tag != "#general":
            taxonomy += f"- `{tag}` ({len(tag_index['application'][tag])} papers)\n"

    taxonomy += "\n### Scalability Tags\n"
    for tag, count in sorted(
        tag_index["scalability"].items(), key=lambda x: -len(x[1])
    ):
        taxonomy += f"- `{tag}` ({len(tag_index['scalability'][tag])} papers)\n"

    taxonomy += "\n### Maturity Tags\n"
    for tag, count in sorted(tag_index["maturity"].items(), key=lambda x: -len(x[1])):
        taxonomy += f"- `{tag}` ({len(tag_index['maturity'][tag])} papers)\n"

    taxonomy += """
---

## Files Generated

- `papers_database.json` - Complete structured data with tags
- `README.md` - Multi-view navigation with all papers
- `TAXONOMY.md` - This file with detailed categorization
- `download_papers.py` - Script to download PDFs locally
- `extract_papers.py` - Script to extract and tag papers
- `generate_readme.py` - Script to generate multi-view README

---

*Generated automatically from papers_database.json*
"""

    return taxonomy


def main():
    taxonomy = generate_taxonomy()

    with open("TAXONOMY_NEW.md", "w", encoding="utf-8") as f:
        f.write(taxonomy)

    print("Generated TAXONOMY_NEW.md with actual data")


if __name__ == "__main__":
    main()
