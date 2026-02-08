#!/usr/bin/env python3
"""
Generate trend analysis and visualizations
"""

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def analyze_trends():
    """Analyze trends in multi-agent research"""
    database = load_database()
    papers = database["papers"]

    print("Analyzing research trends...")
    print()

    # Trend 1: Papers per year
    papers_by_year = defaultdict(int)
    for pid, paper in papers.items():
        year = "20" + pid[:2]
        papers_by_year[year] += 1

    print("=" * 70)
    print("TREND 1: PUBLICATION VOLUME BY YEAR")
    print("=" * 70)
    print()
    print("| Year | Papers | Growth |")
    print("|------|--------|--------|")

    prev_count = 0
    for year in sorted(papers_by_year.keys()):
        count = papers_by_year[year]
        if prev_count > 0:
            growth = f"+{((count - prev_count) / prev_count * 100):.0f}%"
        else:
            growth = "-"
        print(f"| {year} | {count:4d} | {growth:6s} |")
        prev_count = count

    print()

    # Trend 2: Top tags over time
    print("=" * 70)
    print("TREND 2: RESEARCH TOPICS BY YEAR (Top 5 tags per year)")
    print("=" * 70)
    print()

    tags_by_year = defaultdict(lambda: defaultdict(int))
    for pid, paper in papers.items():
        year = "20" + pid[:2]
        for category, tags in paper.get("tags", {}).items():
            for tag in tags:
                tags_by_year[year][tag] += 1

    for year in sorted(tags_by_year.keys())[-5:]:  # Last 5 years
        print(f"\n{year}:")
        sorted_tags = sorted(
            tags_by_year[year].items(), key=lambda x: x[1], reverse=True
        )[:5]
        for tag, count in sorted_tags:
            tag_name = tag.replace("#", "").replace("-", " ").title()
            print(f"  {tag_name:25s} {count:3d} papers")

    print()

    # Trend 3: Application domains
    print("=" * 70)
    print("TREND 3: APPLICATION DOMAINS")
    print("=" * 70)
    print()

    app_counts = defaultdict(int)
    for paper in papers.values():
        for tag in paper.get("tags", {}).get("application", []):
            if tag != "#general":
                app_counts[tag] += 1

    sorted_apps = sorted(app_counts.items(), key=lambda x: x[1], reverse=True)
    print("| Domain | Papers | Percentage |")
    print("|--------|--------|------------|")
    for app, count in sorted_apps[:10]:
        app_name = app.replace("#", "").replace("-", " ").title()
        pct = count / len(papers) * 100
        print(f"| {app_name:30s} | {count:4d} | {pct:5.1f}% |")

    print()

    # Trend 4: Technical approaches
    print("=" * 70)
    print("TREND 4: TECHNICAL APPROACHES")
    print("=" * 70)
    print()

    tech_counts = defaultdict(int)
    for paper in papers.values():
        for tag in paper.get("tags", {}).get("technical", []):
            if tag != "#general":
                tech_counts[tag] += 1

    sorted_tech = sorted(tech_counts.items(), key=lambda x: x[1], reverse=True)
    print("| Approach | Papers | Percentage |")
    print("|----------|--------|------------|")
    for tech, count in sorted_tech[:10]:
        tech_name = tech.replace("#", "").replace("-", " ").upper()
        pct = count / len(papers) * 100
        print(f"| {tech_name:30s} | {count:4d} | {pct:5.1f}% |")

    print()

    # Trend 5: Scalability trends
    print("=" * 70)
    print("TREND 5: SCALABILITY FOCUS")
    print("=" * 70)
    print()

    scale_counts = defaultdict(int)
    for paper in papers.values():
        for tag in paper.get("tags", {}).get("scalability", []):
            scale_counts[tag] += 1

    sorted_scale = sorted(scale_counts.items(), key=lambda x: x[1], reverse=True)
    print("| Scale | Papers | Percentage |")
    print("|-------|--------|------------|")
    for scale, count in sorted_scale:
        scale_name = scale.replace("#scale-", "").replace("-", " ").title()
        pct = count / len(papers) * 100
        print(f"| {scale_name:30s} | {count:4d} | {pct:5.1f}% |")

    print()
    print("=" * 70)
    print("TREND ANALYSIS COMPLETE")
    print("=" * 70)

    # Save trend report
    report = {
        "papers_by_year": dict(papers_by_year),
        "tags_by_year": {k: dict(v) for k, v in tags_by_year.items()},
        "application_domains": dict(app_counts),
        "technical_approaches": dict(tech_counts),
        "scalability_focus": dict(scale_counts),
        "generated_at": datetime.now().isoformat(),
    }

    with open("trends_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\nTrend report saved to: trends_report.json")


def main():
    analyze_trends()


if __name__ == "__main__":
    main()
