#!/usr/bin/env python3
"""
Extract papers from README.md and create tagged JSON database
"""

import re
import json


def extract_papers_from_table(content):
    """Extract papers from markdown table format"""
    papers = []
    # Pattern: | Paper Name | ID | Focus |
    pattern = r"\| ([^|]+) \| (\d{4}\.\d{5}) \| ([^|]+) \|"

    for match in re.finditer(pattern, content):
        paper_name = match.group(1).strip()
        paper_id = match.group(2).strip()
        focus = match.group(3).strip()
        papers.append(
            {
                "id": paper_id,
                "name": paper_name,
                "focus": focus,
                "tags": {
                    "use_case": [],
                    "technical": [],
                    "application": [],
                    "scalability": [],
                    "maturity": [],
                },
            }
        )

    return papers


def assign_tags(paper):
    """Assign tags based on paper content"""
    name = paper["name"].lower()
    focus = paper["focus"].lower()
    combined = name + " " + focus

    # Use-Case Tags
    use_case_tags = []
    if any(x in combined for x in ["team", "group", "formation", "coalition", "hmat"]):
        use_case_tags.append("#team-formation")
    if any(
        x in combined
        for x in ["governance", "normative", "norm", "kelsenian", "commitment"]
    ):
        use_case_tags.append("#governance")
    if any(
        x in combined
        for x in ["communication", "comm", "message", "signal", "broadcast"]
    ):
        use_case_tags.append("#communication")
    if any(
        x in combined
        for x in ["negotiation", "bargain", "auction", "deal", "transaction", "trading"]
    ):
        use_case_tags.append("#negotiation")
    if any(
        x in combined
        for x in [
            "memory",
            "remember",
            "recall",
            "episodic",
            "semantic",
            "latentmem",
            "mki",
            "bmam",
        ]
    ):
        use_case_tags.append("#memory")
    if any(
        x in combined for x in ["federated", "federation", "privacy", "local learning"]
    ):
        use_case_tags.append("#federated")
    if any(
        x in combined for x in ["economic", "market", "auction", "pricing", "incentive"]
    ):
        use_case_tags.append("#economic")
    if any(
        x in combined for x in ["supply", "inventory", "logistics", "scm", "delivery"]
    ):
        use_case_tags.append("#supply-chain")
    if any(
        x in combined
        for x in ["task allocation", "scheduling", "assignment", "workload"]
    ):
        use_case_tags.append("#task-allocation")
    if any(
        x in combined
        for x in ["large scale", "massive", "swarm", "hive", "1000", "2000"]
    ):
        use_case_tags.append("#large-scale")
    if any(
        x in combined
        for x in ["safety", "security", "shield", "rogue", "attack", "risk"]
    ):
        use_case_tags.append("#safety")
    if any(x in combined for x in ["verification", "prove", "formal", "logic", "ltl"]):
        use_case_tags.append("#verification")
    if any(
        x in combined
        for x in ["human", "human-agent", "collaboration", "warmth", "competence"]
    ):
        use_case_tags.append("#human-in-loop")

    # Technical Tags
    technical_tags = []
    if any(x in combined for x in ["marl", "multi-agent rl", "reinforcement"]):
        technical_tags.append("#marl")
    if any(
        x in combined
        for x in ["deep learning", "neural", "transformer", "llm", "language model"]
    ):
        technical_tags.append("#deep-learning")
    if any(
        x in combined for x in ["planning", "pddl", "htn", "task planning", "lookahead"]
    ):
        technical_tags.append("#planning")
    if any(x in combined for x in ["pddl", "planning domain"]):
        technical_tags.append("#pddl")
    if any(x in combined for x in ["llm", "language model", "gpt", "transformer"]):
        technical_tags.append("#llm")
    if any(
        x in combined
        for x in ["formal", "logic", "verification", "ltl", "probabilistic"]
    ):
        technical_tags.append("#formal-methods")
    if any(x in combined for x in ["game theory", "nash", "equilibrium", "bargaining"]):
        technical_tags.append("#game-theory")
    if any(
        x in combined for x in ["simulation", "simulator", "framework", "benchmark"]
    ):
        technical_tags.append("#simulation")
    if any(x in combined for x in ["benchmark", "evaluation", "dataset"]):
        technical_tags.append("#benchmark")

    # Application Tags
    app_tags = []
    if any(
        x in combined
        for x in ["supply", "inventory", "logistics", "scm", "delivery", "chain"]
    ):
        app_tags.append("#supply-chain-logistics")
    if any(x in combined for x in ["finance", "trading", "market", "economic"]):
        app_tags.append("#finance-trading")
    if any(x in combined for x in ["medical", "healthcare", "hospital", "clinical"]):
        app_tags.append("#healthcare")
    if any(x in combined for x in ["manufacturing", "production", "factory"]):
        app_tags.append("#manufacturing-ops")
    if any(
        x in combined
        for x in ["scientific", "discovery", "materials", "drug", "chemistry"]
    ):
        app_tags.append("#scientific-discovery")
    if any(
        x in combined
        for x in ["telecom", "network", "wireless", "5g", "6g", "spectrum"]
    ):
        app_tags.append("#telecom")
    if any(
        x in combined
        for x in ["robot", "vehicle", "autonomous", "physical", "embodied"]
    ):
        app_tags.append("#robotics")

    # Scalability Tags
    scale_tags = []
    if any(x in combined for x in ["2 ", "two ", "dual", "pair", "bilateral"]):
        scale_tags.append("#scale-small")
    if any(x in combined for x in ["swarm", "multi", "several", "group"]):
        scale_tags.append("#scale-medium")
    if any(x in combined for x in ["100", "1000", "large", "massive", "hive", "many"]):
        scale_tags.append("#scale-large")
    if any(x in combined for x in ["2000", "10000", "massive", "emergent"]):
        scale_tags.append("#scale-massive")

    # Maturity Tags
    maturity_tags = []
    if "survey" in combined or "review" in combined:
        maturity_tags.append("#survey")
    if any(x in combined for x in ["theoretical", "framework", "formal", "analysis"]):
        maturity_tags.append("#theoretical")
    if any(
        x in combined for x in ["application", "deployed", "production", "real-world"]
    ):
        maturity_tags.append("#applied")
    if "experimental" in combined or "prototype" in combined:
        maturity_tags.append("#experimental")

    # If no tags assigned, add general tags
    if not use_case_tags:
        use_case_tags.append("#general")
    if not technical_tags:
        technical_tags.append("#general")
    if not app_tags:
        app_tags.append("#general")
    if not scale_tags:
        scale_tags.append("#scale-medium")
    if not maturity_tags:
        maturity_tags.append("#experimental")

    paper["tags"]["use_case"] = use_case_tags
    paper["tags"]["technical"] = technical_tags
    paper["tags"]["application"] = app_tags
    paper["tags"]["scalability"] = scale_tags
    paper["tags"]["maturity"] = maturity_tags

    return paper


def main():
    # Read README.md
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Extract papers
    papers = extract_papers_from_table(content)
    print(f"Extracted {len(papers)} papers from table")

    # Assign tags
    for paper in papers:
        assign_tags(paper)

    # Create database
    database = {
        "metadata": {
            "total_papers": len(papers),
            "last_updated": "2026-02-07",
            "source": "arXiv cs.AI",
            "focus": "Multi-agent systems for virtual AI organizations",
        },
        "papers": {p["id"]: p for p in papers},
    }

    # Save to JSON
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    print(f"Created papers_database.json with {len(papers)} papers")

    # Generate tag statistics
    tag_stats = {
        "use_case": {},
        "technical": {},
        "application": {},
        "scalability": {},
        "maturity": {},
    }

    for paper in papers:
        for category, tags in paper["tags"].items():
            for tag in tags:
                tag_stats[category][tag] = tag_stats[category].get(tag, 0) + 1

    print("\nTag Statistics:")
    for category, tags in tag_stats.items():
        print(f"\n{category.upper()}:")
        for tag, count in sorted(tags.items(), key=lambda x: -x[1]):
            print(f"  {tag}: {count}")


if __name__ == "__main__":
    main()
