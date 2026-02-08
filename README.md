# Multi-Agent AI Research

**Total Papers:** 407 multi-agent systems from arXiv cs.AI  
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

- **407 papers** with complete metadata
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
