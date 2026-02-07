#!/usr/bin/env python3
"""
Generate multi-view README with tag-based organization
"""

import json
from collections import defaultdict


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def generate_tag_index(papers):
    """Generate index of papers by tag"""
    tag_index = defaultdict(lambda: defaultdict(list))

    for paper_id, paper in papers.items():
        for category, tags in paper["tags"].items():
            for tag in tags:
                tag_index[category][tag].append(paper)

    return tag_index


def generate_readme():
    database = load_database()
    papers = database["papers"]
    tag_index = generate_tag_index(papers)

    readme = f"""# Multi-Agent AI Research - February 2-6, 2026

## Quick Navigation

**Total Papers:** {len(papers)} multi-agent systems from arXiv cs.AI  
**Last Updated:** 2026-02-07  
**Focus:** Virtual AI companies and autonomous organizations

### Multi-View Access

- **[By Use-Case](#view-1-by-use-case)** - Find papers by organizational function
- **[By Technical Approach](#view-2-by-technical-approach)** - Find papers by methodology
- **[By Application Domain](#view-3-by-application-domain)** - Find papers by industry
- **[By Scalability](#view-4-by-scalability)** - Find papers by agent count
- **[By Maturity](#view-5-by-maturity)** - Find papers by development stage
- **[Complete Paper List](#complete-paper-index)** - All papers with tags
- **[Download Papers](#downloading-papers)** - Get PDFs locally

### Supporting Files

- **[papers_database.json](papers_database.json)** - Structured data with tags for all papers
- **[TAXONOMY.md](TAXONOMY.md)** - Detailed taxonomy and cross-references
- **[Agent.md](Agent.md)** - Research progress and handoff notes

---

## View 1: By Use-Case

Organized by organizational function for virtual AI companies.

"""

    # Use-Case sections
    use_case_order = [
        (
            "#team-formation",
            "Team Formation & Organization",
            "Forming and structuring multi-agent teams",
        ),
        ("#governance", "Governance & Norms", "Rules, norms, and formal frameworks"),
        (
            "#communication",
            "Communication & Coordination",
            "Protocols and mechanisms for agent interaction",
        ),
        (
            "#negotiation",
            "Negotiation & Economics",
            "Bargaining, auctions, and market mechanisms",
        ),
        (
            "#memory",
            "Memory & Knowledge",
            "Systems for agent memory and knowledge sharing",
        ),
        ("#federated", "Federated Learning", "Privacy-preserving distributed learning"),
        (
            "#supply-chain",
            "Supply Chain & Operations",
            "Inventory, logistics, and operational systems",
        ),
        ("#task-allocation", "Task Allocation", "Work distribution and scheduling"),
        ("#large-scale", "Large-Scale Systems", "Scaling to 100+ agents"),
        (
            "#safety",
            "Safety & Security",
            "Robustness, verification, and rogue agent prevention",
        ),
        (
            "#verification",
            "Verification & Formal Methods",
            "Logic, proofs, and formal guarantees",
        ),
        (
            "#human-in-loop",
            "Human-AI Collaboration",
            "Human-agent interaction and collaboration",
        ),
    ]

    for tag, title, description in use_case_order:
        if tag in tag_index["use_case"]:
            papers_in_tag = tag_index["use_case"][tag]
            readme += f"### {title}\n*{description}*\n\n"
            readme += "| Paper | ID | Focus | Tags |\n"
            readme += "|-------|-----|-------|------|\n"

            for paper in sorted(papers_in_tag, key=lambda x: x["name"]):
                other_tags = [t for t in paper["tags"]["use_case"] if t != tag]
                tag_str = ", ".join(other_tags[:2]) if other_tags else "-"
                readme += f"| {paper['name']} | {paper['id']} | {paper['focus']} | {tag_str} |\n"

            readme += "\n"

    # Technical Approach
    readme += """---

## View 2: By Technical Approach

Organized by methodology and technical foundation.

"""

    technical_order = [
        ("#marl", "Multi-Agent Reinforcement Learning", "MARL and deep RL approaches"),
        (
            "#deep-learning",
            "Deep Learning & Neural Networks",
            "Neural architectures and learning",
        ),
        ("#llm", "LLM-Based Systems", "Large language model agents"),
        ("#planning", "Planning & PDDL", "Task planning and automated planning"),
        (
            "#formal-methods",
            "Formal Methods",
            "Logic, verification, and formal guarantees",
        ),
        ("#game-theory", "Game Theory", "Economic and game-theoretic approaches"),
        (
            "#simulation",
            "Simulation & Benchmarks",
            "Frameworks and evaluation environments",
        ),
    ]

    for tag, title, description in technical_order:
        if tag in tag_index["technical"]:
            papers_in_tag = tag_index["technical"][tag]
            readme += f"### {title}\n*{description}*\n\n"
            readme += "| Paper | ID | Focus |\n"
            readme += "|-------|-----|-------|\n"

            for paper in sorted(papers_in_tag, key=lambda x: x["name"])[
                :20
            ]:  # Limit to 20
                readme += f"| {paper['name']} | {paper['id']} | {paper['focus']} |\n"

            if len(papers_in_tag) > 20:
                readme += f"| *...and {len(papers_in_tag) - 20} more* | | |\n"

            readme += "\n"

    # Application Domain
    readme += """---

## View 3: By Application Domain

Organized by industry and application area.

"""

    app_order = [
        (
            "#supply-chain-logistics",
            "Supply Chain & Logistics",
            "Inventory, delivery, and SCM",
        ),
        ("#finance-trading", "Finance & Trading", "Financial markets and trading"),
        (
            "#healthcare",
            "Healthcare & Medicine",
            "Medical applications and clinical systems",
        ),
        (
            "#manufacturing-ops",
            "Manufacturing & Operations",
            "Production and factory systems",
        ),
        (
            "#scientific-discovery",
            "Scientific Discovery",
            "Research and scientific applications",
        ),
        ("#telecom", "Telecommunications", "Networks, 5G/6G, and wireless"),
        (
            "#robotics",
            "Robotics & Physical Systems",
            "Robots, vehicles, and embodied agents",
        ),
    ]

    for tag, title, description in app_order:
        if tag in tag_index["application"]:
            papers_in_tag = tag_index["application"][tag]
            readme += f"### {title}\n*{description}*\n\n"
            readme += "| Paper | ID | Focus |\n"
            readme += "|-------|-----|-------|\n"

            for paper in sorted(papers_in_tag, key=lambda x: x["name"]):
                readme += f"| {paper['name']} | {paper['id']} | {paper['focus']} |\n"

            readme += "\n"

    # Scalability
    readme += """---

## View 4: By Scalability

Organized by number of agents.

"""

    scale_order = [
        ("#scale-small", "Small Scale (2-10 agents)", "Pairs and small teams"),
        (
            "#scale-medium",
            "Medium Scale (10-100 agents)",
            "Standard multi-agent systems",
        ),
        ("#scale-large", "Large Scale (100-1000 agents)", "Hundreds of agents"),
        (
            "#scale-massive",
            "Massive Scale (1000+ agents)",
            "Swarms and emergent systems",
        ),
    ]

    for tag, title, description in scale_order:
        if tag in tag_index["scalability"]:
            papers_in_tag = tag_index["scalability"][tag]
            readme += f"### {title}\n*{description}*\n\n"
            readme += "| Paper | ID | Focus |\n"
            readme += "|-------|-----|-------|\n"

            for paper in sorted(papers_in_tag, key=lambda x: x["name"])[:15]:
                readme += f"| {paper['name']} | {paper['id']} | {paper['focus']} |\n"

            if len(papers_in_tag) > 15:
                readme += f"| *...and {len(papers_in_tag) - 15} more* | | |\n"

            readme += "\n"

    # Maturity
    readme += """---

## View 5: By Maturity

Organized by development stage.

"""

    maturity_order = [
        ("#survey", "Surveys & Reviews", "Comprehensive overviews and surveys"),
        ("#theoretical", "Theoretical", "Foundational theory and frameworks"),
        ("#applied", "Applied & Production", "Deployed and real-world systems"),
        ("#experimental", "Experimental", "Research prototypes and experiments"),
    ]

    for tag, title, description in maturity_order:
        if tag in tag_index["maturity"]:
            papers_in_tag = tag_index["maturity"][tag]
            readme += f"### {title}\n*{description}*\n\n"
            readme += "| Paper | ID | Focus |\n"
            readme += "|-------|-----|-------|\n"

            for paper in sorted(papers_in_tag, key=lambda x: x["name"])[:20]:
                readme += f"| {paper['name']} | {paper['id']} | {paper['focus']} |\n"

            if len(papers_in_tag) > 20:
                readme += f"| *...and {len(papers_in_tag) - 20} more* | | |\n"

            readme += "\n"

    # Complete index
    readme += """---

## Complete Paper Index

All papers with their complete tag sets.

"""

    readme += "| Paper | ID | Use-Case | Technical | Application | Scale | Maturity |\n"
    readme += (
        "|-------|-----|----------|-----------|-------------|-------|----------|\n"
    )

    for paper_id in sorted(papers.keys()):
        paper = papers[paper_id]
        uc = ", ".join(paper["tags"]["use_case"][:2])
        tech = ", ".join(paper["tags"]["technical"][:2])
        app = ", ".join(paper["tags"]["application"][:1])
        scale = ", ".join(paper["tags"]["scalability"])
        mat = ", ".join(paper["tags"]["maturity"][:1])

        readme += f"| {paper['name'][:40]} | {paper['id']} | {uc} | {tech} | {app} | {scale} | {mat} |\n"

    # Downloading papers section
    readme += """
---

## Downloading Papers

To download all papers locally:

```bash
python download_papers.py
```

This will create a `papers/` directory with PDFs for all {len(papers)} papers.

**Note:** Please be respectful of arXiv's servers. The script includes a 1-second delay between downloads.

---

## Tag Legend

### Use-Case Tags
- `#team-formation` - Team formation and organization
- `#governance` - Rules, norms, and governance
- `#communication` - Communication protocols
- `#negotiation` - Bargaining and auctions
- `#memory` - Memory and knowledge systems
- `#federated` - Federated learning
- `#supply-chain` - Supply chain and logistics
- `#task-allocation` - Task scheduling
- `#large-scale` - 100+ agent systems
- `#safety` - Security and safety
- `#verification` - Formal verification
- `#human-in-loop` - Human-AI collaboration

### Technical Tags
- `#marl` - Multi-agent RL
- `#deep-learning` - Neural networks
- `#llm` - Large language models
- `#planning` - Task planning
- `#pddl` - Planning domain language
- `#formal-methods` - Logic and verification
- `#game-theory` - Economic approaches
- `#simulation` - Simulators and frameworks
- `#benchmark` - Evaluation benchmarks

### Application Tags
- `#supply-chain-logistics` - SCM and logistics
- `#finance-trading` - Financial markets
- `#healthcare` - Medical applications
- `#manufacturing-ops` - Manufacturing
- `#scientific-discovery` - Research
- `#telecom` - Telecommunications
- `#robotics` - Physical robots

### Scalability Tags
- `#scale-small` - 2-10 agents
- `#scale-medium` - 10-100 agents
- `#scale-large` - 100-1000 agents
- `#scale-massive` - 1000+ agents

### Maturity Tags
- `#survey` - Comprehensive reviews
- `#theoretical` - Foundational theory
- `#applied` - Production systems
- `#experimental` - Research prototypes

---

*Generated automatically from papers_database.json*
"""

    return readme


def main():
    readme = generate_readme()

    with open("README_NEW.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("Generated README_NEW.md with multi-view organization")


if __name__ == "__main__":
    main()
