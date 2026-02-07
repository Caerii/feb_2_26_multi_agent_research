#!/usr/bin/env python3
"""
Refined paper tagger with better keyword matching
"""

import json
import re


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def refined_tagging(paper):
    """Improved tagging with better keyword detection"""
    name = paper["name"].lower()
    focus = paper["focus"].lower()
    combined = name + " " + focus

    # Clear existing tags
    paper["tags"] = {
        "use_case": [],
        "technical": [],
        "application": [],
        "scalability": [],
        "maturity": [],
    }

    # Use-Case Detection (more specific patterns)
    use_case_patterns = {
        "#team-formation": [
            r"\b(team|group|formation|coalition|hmat|bilateral|swarm)\b",
            r"\borganiz|structur\b",
        ],
        "#governance": [
            r"\b(governance|norm|kelsenian|commitment|protocol|agreement)\b",
            r"\b(deontic|obligation|permission)\b",
        ],
        "#communication": [
            r"\b(communicat|signal|broadcast|message|bandwidth|topology)\b",
            r"\bcommcp|todycomm\b",
        ],
        "#negotiation": [
            r"\b(negotiat|auction|bargain|deal|transaction|trading|economic|market|price)\b",
            r"\bagenticpay|sale\b",
        ],
        "#memory": [
            r"\b(memory|remember|recall|episodic|semantic|latentmem|mki|bmam|knowledge|mem)\b",
            r"\bforget|retriev|stor\b",
        ],
        "#federated": [
            r"\b(federated|fedmrl|federated learning|privacy|local.*learning)\b",
            r"\bfedk|federated\b",
        ],
        "#supply-chain": [
            r"\b(supply|inventory|logistics|scm|delivery|chain|warehouse|replenish)\b",
            r"\bmabim|synapse.*delivery\b",
        ],
        "#task-allocation": [
            r"\b(task.*alloc|scheduling|assignment|workload|load.*management)\b",
            r"\ballocat|distribut\b",
        ],
        "#large-scale": [
            r"\b(1000|2000|massive|swarm|hive|large.*scale|many.*agent)\b",
            r"\bemergent|collective.*intelligence\b",
        ],
        "#safety": [
            r"\b(safety|security|shield|rogue|attack|risk|vulnerab|protect)\b",
            r"\bsafe|secure\b",
        ],
        "#verification": [
            r"\b(verification|prove|formal|logic|ltl|temporal|verify|proof)\b",
            r"\bmas-prove|prov\b",
        ],
        "#human-in-loop": [
            r"\b(human|human-agent|collaboration|warmth|competence|hmat|human.*ai)\b",
            r"\buser|person\b",
        ],
    }

    for tag, patterns in use_case_patterns.items():
        for pattern in patterns:
            if re.search(pattern, combined):
                if tag not in paper["tags"]["use_case"]:
                    paper["tags"]["use_case"].append(tag)
                break

    # Technical Detection
    technical_patterns = {
        "#marl": [
            r"\b(marl|multi-agent.*rl|reinforcement|madrl|mappo|maddpg)\b",
            r"\bactor.*critic|policy\b",
        ],
        "#deep-learning": [
            r"\b(deep.*learn|neural|transformer|cnn|rnn|backprop)\b",
            r"\bnetwork.*architect|layer\b",
        ],
        "#llm": [
            r"\b(llm|language.*model|gpt|transformer|bert|llama|qwen|deepseek)\b",
            r"\blarge.*language|foundation.*model\b",
        ],
        "#planning": [
            r"\b(planning|pddl|htn|lookahead|planner|schedule)\b",
            r"\btask.*plan|action.*plan\b",
        ],
        "#pddl": [
            r"\b(pddl|planning.*domain|domain.*language)\b",
            r"\bpddl|domain.*definition\b",
        ],
        "#formal-methods": [
            r"\b(formal|logic|verification|ltl|ctl|modal|proof)\b",
            r"\bspecification|formalism\b",
        ],
        "#game-theory": [
            r"\b(game.*theory|nash|equilibrium|bargain|auction|mechanism.*design)\b",
            r"\bstrategic|payoff\b",
        ],
        "#simulation": [
            r"\b(simulation|simulator|framework|environment|world)\b",
            r"\bsimulat|emulat\b",
        ],
        "#benchmark": [
            r"\b(benchmark|dataset|evaluation|metric|assessment|test)\b",
            r"\benchmark|dataset\b",
        ],
    }

    for tag, patterns in technical_patterns.items():
        for pattern in patterns:
            if re.search(pattern, combined):
                if tag not in paper["tags"]["technical"]:
                    paper["tags"]["technical"].append(tag)
                break

    # Application Detection
    app_patterns = {
        "#supply-chain-logistics": [
            r"\b(supply.*chain|inventory|logistics|warehouse|delivery|shipping|scm)\b",
            r"\bmabim|replenish\b",
        ],
        "#finance-trading": [
            r"\b(finance|trading|market|stock|portfolio|investment|banking)\b",
            r"\btrading|financial\b",
        ],
        "#healthcare": [
            r"\b(health|medical|healthcare|clinical|hospital|patient|diagnosis|treatment)\b",
            r"\bmedaide|medical\b",
        ],
        "#manufacturing-ops": [
            r"\b(manufacturing|production|factory|assembly|industrial|operation)\b",
            r"\bcpms|manufacturing\b",
        ],
        "#scientific-discovery": [
            r"\b(scientific|discovery|research|materials|drug|chemistry|biology|physics)\b",
            r"\bmaterials|drug.*discovery\b",
        ],
        "#telecom": [
            r"\b(telecom|network|wireless|5g|6g|spectrum|radio|bandwidth|ran)\b",
            r"\bmmwave|spectrum|telecommunication\b",
        ],
        "#robotics": [
            r"\b(robot|robotic|vehicle|autonomous|embodied|physical|drone|uav|swarm.*robot)\b",
            r"\brobot|vehicl|autonomous\b",
        ],
    }

    for tag, patterns in app_patterns.items():
        for pattern in patterns:
            if re.search(pattern, combined):
                if tag not in paper["tags"]["application"]:
                    paper["tags"]["application"].append(tag)
                break

    # Scalability Detection
    scale_patterns = {
        "#scale-small": [
            r"\b(2.*agent|two.*agent|pair|bilateral|dual|small.*team)\b",
            r"\b2-|two-|pair\b",
        ],
        "#scale-medium": [
            r"\b(multi.*agent|several|group|team|medium.*scale)\b",
            r"\b10.*agent|small.*swarm\b",
        ],
        "#scale-large": [
            r"\b(100.*agent|1000.*agent|large.*scale|hundreds|many.*agent)\b",
            r"\b100-|1000-|large\b",
        ],
        "#scale-massive": [
            r"\b(1000\+|massive|swarm|emergent|collective|thousands)\b",
            r"\bhive|massive|emergent\b",
        ],
    }

    for tag, patterns in scale_patterns.items():
        for pattern in patterns:
            if re.search(pattern, combined):
                if tag not in paper["tags"]["scalability"]:
                    paper["tags"]["scalability"].append(tag)
                break

    # If no scale detected, default to medium
    if not paper["tags"]["scalability"]:
        paper["tags"]["scalability"].append("#scale-medium")

    # Maturity Detection
    maturity_patterns = {
        "#survey": [
            r"\b(survey|review|overview|taxonomy|comprehensive.*study)\b",
            r"\bsurvey|review\b",
        ],
        "#theoretical": [
            r"\b(theoretical|framework|formal|analysis|proof|theorem|lemma)\b",
            r"\btheory|foundational\b",
        ],
        "#applied": [
            r"\b(applied|deployed|production|real.*world|industrial|commercial)\b",
            r"\bdeployment|practical\b",
        ],
        "#experimental": [
            r"\b(experimental|prototype|implementation|evaluation|empirical)\b",
            r"\bexperiment|test\b",
        ],
    }

    for tag, patterns in maturity_patterns.items():
        for pattern in patterns:
            if re.search(pattern, combined):
                if tag not in paper["tags"]["maturity"]:
                    paper["tags"]["maturity"].append(tag)
                break

    # If no maturity detected, default to experimental
    if not paper["tags"]["maturity"]:
        paper["tags"]["maturity"].append("#experimental")

    # Add defaults if empty
    if not paper["tags"]["use_case"]:
        paper["tags"]["use_case"].append("#general")
    if not paper["tags"]["technical"]:
        paper["tags"]["technical"].append("#general")
    if not paper["tags"]["application"]:
        paper["tags"]["application"].append("#general")

    return paper


def main():
    database = load_database()
    papers = database["papers"]

    print(f"Retagging {len(papers)} papers with refined patterns...")

    # Retag all papers
    for paper_id, paper in papers.items():
        refined_tagging(paper)

    # Save updated database
    with open("papers_database.json", "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    # Generate statistics
    tag_stats = {
        "use_case": {},
        "technical": {},
        "application": {},
        "scalability": {},
        "maturity": {},
    }

    for paper in papers.values():
        for category, tags in paper["tags"].items():
            for tag in tags:
                tag_stats[category][tag] = tag_stats[category].get(tag, 0) + 1

    print("\nRefined Tag Statistics:")
    for category, tags in tag_stats.items():
        print(f"\n{category.upper()}:")
        for tag, count in sorted(tags.items(), key=lambda x: -x[1]):
            print(f"  {tag}: {count}")

    print(f"\n[OK] Updated papers_database.json with refined tags")


if __name__ == "__main__":
    main()
