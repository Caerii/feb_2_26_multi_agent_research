#!/usr/bin/env python3
"""
Split README into organized subfiles by category
"""

import json
from pathlib import Path
from collections import defaultdict


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_category_files(database, output_dir="docs"):
    """Generate separate markdown files for each category"""
    papers = database["papers"]
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Build tag index
    tag_index = defaultdict(lambda: defaultdict(list))
    for paper_id, paper in papers.items():
        for category, tags in paper["tags"].items():
            for tag in tags:
                tag_index[category][tag].append(paper)

    # Generate files for each category type
    categories = {
        "use-case": {
            "title": "By Use-Case",
            "description": "Papers organized by organizational function",
            "tags": [
                "#team-formation",
                "#governance",
                "#communication",
                "#negotiation",
                "#memory",
                "#federated",
                "#supply-chain",
                "#task-allocation",
                "#large-scale",
                "#safety",
                "#verification",
                "#human-in-loop",
            ],
        },
        "technical": {
            "title": "By Technical Approach",
            "description": "Papers organized by methodology",
            "tags": [
                "#marl",
                "#deep-learning",
                "#llm",
                "#planning",
                "#pddl",
                "#formal-methods",
                "#game-theory",
                "#simulation",
                "#benchmark",
            ],
        },
        "application": {
            "title": "By Application Domain",
            "description": "Papers organized by industry",
            "tags": [
                "#supply-chain-logistics",
                "#finance-trading",
                "#healthcare",
                "#manufacturing-ops",
                "#scientific-discovery",
                "#telecom",
                "#robotics",
            ],
        },
        "scalability": {
            "title": "By Scalability",
            "description": "Papers organized by agent count",
            "tags": ["#scale-small", "#scale-medium", "#scale-large", "#scale-massive"],
        },
        "maturity": {
            "title": "By Maturity",
            "description": "Papers organized by development stage",
            "tags": ["#survey", "#theoretical", "#applied", "#experimental"],
        },
    }

    index_links = []

    for cat_type, cat_info in categories.items():
        cat_dir = output_path / cat_type
        cat_dir.mkdir(exist_ok=True)

        # Create index file for this category
        index_content = f"""# {cat_info["title"]}

{cat_info["description"]}

**Total Papers:** {len(papers)}

## Categories

"""

        for tag in cat_info["tags"]:
            if tag in tag_index.get(cat_type, {}):
                papers_in_tag = tag_index[cat_type][tag]
                tag_name = tag.replace("#", "").replace("-", " ").title()

                # Create separate file for this tag
                tag_filename = f"{tag.replace('#', '').replace('-', '_')}.md"

                tag_content = f"""# {tag_name}

**Tag:** `{tag}`  
**Papers:** {len(papers_in_tag)}

| Paper | ID | Focus |
|-------|-----|-------|
"""

                for paper in sorted(papers_in_tag, key=lambda x: x["name"]):
                    tag_content += f"| {paper['name'][:60]} | {paper['id']} | {paper['focus'][:70]}... |\n"

                # Save tag file
                tag_file_path = cat_dir / tag_filename
                with open(tag_file_path, "w", encoding="utf-8") as f:
                    f.write(tag_content)

                # Add to index
                index_content += (
                    f"- [{tag_name}]({tag_filename}) - {len(papers_in_tag)} papers\n"
                )

        # Save category index
        index_file_path = cat_dir / "README.md"
        with open(index_file_path, "w", encoding="utf-8") as f:
            f.write(index_content)

        index_links.append(f"- [{cat_info['title']}]({cat_type}/README.md)")

    # Generate year-based organization
    year_dir = output_path / "by-year"
    year_dir.mkdir(exist_ok=True)

    # Group papers by year
    papers_by_year = defaultdict(list)
    for paper_id, paper in papers.items():
        year = "20" + paper_id[:2]
        papers_by_year[year].append(paper)

    year_index = "# Papers by Year\n\n"

    for year in sorted(papers_by_year.keys()):
        year_papers = papers_by_year[year]
        year_filename = f"{year}.md"

        year_content = f"""# Papers from {year}

**Count:** {len(year_papers)} papers

| Paper | ID | Focus |
|-------|-----|-------|
"""

        for paper in sorted(year_papers, key=lambda x: x["name"]):
            year_content += (
                f"| {paper['name'][:60]} | {paper['id']} | {paper['focus'][:70]}... |\n"
            )

        # Save year file
        year_file_path = year_dir / year_filename
        with open(year_file_path, "w", encoding="utf-8") as f:
            f.write(year_content)

        year_index += f"- [{year}]({year_filename}) - {len(year_papers)} papers\n"

    # Save year index
    with open(year_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(year_index)

    index_links.append("- [By Year](by-year/README.md)")

    # Generate main docs index
    docs_index = f"""# Multi-Agent Research Documentation

**Total Papers:** {len(papers)}  
**Last Updated:** 2026-02-07  
**Focus:** Virtual AI companies and autonomous organizations

## Browse Papers

{chr(10).join(index_links)}

## Quick Stats

- **By Use-Case:** {len(tag_index.get("use_case", {}))} categories
- **By Technical:** {len(tag_index.get("technical", {}))} approaches  
- **By Application:** {len(tag_index.get("application", {}))} domains
- **By Scalability:** {len(tag_index.get("scalability", {}))} levels
- **By Year:** {len(papers_by_year)} years

## Files

- [papers_database.json](../papers_database.json) - Complete structured database
- [download_papers.py](../download_papers.py) - Download all PDFs
- [search_papers.py](../search_papers.py) - Search by keywords

## Paper Downloads

All papers are organized in `papers/YYYY/` directories:
```
papers/
├── 2017/
├── 2019/
├── 2020/
├── ...
└── 2026/
```

Run `python download_papers.py` to download all PDFs.
"""

    with open(output_path / "README.md", "w", encoding="utf-8") as f:
        f.write(docs_index)

    print(f"Generated documentation structure in {output_dir}/")
    print(f"  - {len(categories)} category directories")
    print(f"  - {len(papers_by_year)} year files")
    print(f"  - Total: {len(papers)} papers organized")


def generate_main_readme(database):
    """Generate a concise main README"""
    papers = database["papers"]
    total = len(papers)

    readme = f"""# Multi-Agent AI Research

**Total Papers:** {total} multi-agent systems from arXiv cs.AI  
**Last Updated:** 2026-02-07  
**Focus:** Virtual AI companies and autonomous organizations

## Quick Navigation

📚 **[Browse by Category](docs/README.md)** - Organized views of all papers
🔍 **[Search Papers](search_papers.py)** - Find papers by keywords  
📥 **[Download Papers](download_papers.py)** - Get all PDFs locally
📊 **[View Database](papers_database.json)** - Structured data with tags

## Repository Structure

```
.
├── README.md                    # This file
├── docs/                        # Organized documentation
│   ├── README.md               # Documentation index
│   ├── use-case/               # By organizational function
│   ├── technical/              # By methodology
│   ├── application/            # By industry
│   ├── scalability/            # By agent count
│   ├── maturity/               # By development stage
│   └── by-year/                # By publication year
├── papers/                      # Downloaded PDFs
│   ├── 2017/                   # Papers from 2017
│   ├── 2024/                   # Papers from 2024
│   ├── 2025/                   # Papers from 2025
│   └── 2026/                   # Papers from 2026
├── papers_database.json         # Structured database (98KB)
├── search_papers.py            # Search tool
├── download_papers.py          # Download tool
└── extract_all_batches.py      # Batch extraction tool
```

## Key Statistics

- **{total} papers** with complete metadata
- **5 navigation views** (use-case, technical, application, scalability, maturity)
- **30+ unique tags** for filtering
- **796MB** of PDFs downloaded
- **9 years** of research (2017-2026)

## Top Tags

### Use-Cases
- Team Formation & Organization (19 papers)
- Memory & Knowledge (23 papers)  
- Human-AI Collaboration (20 papers)
- Large-Scale Systems (14 papers)

### Technical Approaches
- Simulation & Benchmarks (29 papers)
- LLM-Based Systems (28 papers)
- Multi-Agent RL (18 papers)
- Planning & PDDL (15 papers)

### Applications
- Robotics & Physical Systems (59 papers)
- Telecommunications (28 papers)
- Scientific Discovery (26 papers)
- Manufacturing & Operations (19 papers)

## Quick Start

**Browse papers by category:**
```bash
# View organized documentation
open docs/README.md

# Or browse specific categories:
open docs/use-case/README.md      # Team formation, governance, etc.
open docs/technical/README.md     # MARL, LLM, planning, etc.
open docs/application/README.md   # Supply chain, healthcare, etc.
```

**Search for specific papers:**
```bash
# Search by keyword
python search_papers.py "negotiation"

# Interactive search mode
python search_papers.py
```

**Download papers:**
```bash
# Download all PDFs (organized by year)
python download_papers.py

# Papers will be saved to papers/YYYY/
```

## Contributing

To add more papers from arXiv batch files:
```bash
python extract_all_batches.py
python refine_tags.py
python generate_split_docs.py  # Regenerate docs
```

## License

Research compilation for academic and commercial use.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("Generated concise main README.md")


def main():
    database = load_database()

    print("=" * 70)
    print("SPLITTING DOCUMENTATION INTO ORGANIZED SUBFILES")
    print("=" * 70)
    print()

    # Generate docs structure
    generate_category_files(database)
    print()

    # Generate concise main README
    generate_main_readme(database)
    print()

    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print()
    print("New structure:")
    print("  README.md - Concise main file")
    print("  docs/ - Organized subfiles")
    print("    ├── README.md - Index")
    print("    ├── use-case/ - Team formation, governance, etc.")
    print("    ├── technical/ - MARL, LLM, planning, etc.")
    print("    ├── application/ - Supply chain, healthcare, etc.")
    print("    ├── scalability/ - Small to massive scale")
    print("    ├── maturity/ - Survey, theoretical, applied")
    print("    └── by-year/ - 2017, 2019-2026")


if __name__ == "__main__":
    main()
