# Multi-Agent AI Research - February 2-6, 2026

## Exec Summary

Total papers analyzed: **43 multi-agent systems** from arXiv cs.AI

**Key themes emerging:**
- Agentic coordination protocols (CommCP, CoWork-X, Learning to Share)
- Multi-agent memory systems (Graph-based Agent Memory survey)
- Dynamic topology management (DyTopo, TKG-Thinker)
- Efficiency breakthroughs (RL-VLA³: 59-127% throughput gains; WideSeek-R1 width scaling)
- Agent self-improvement (Group-Evolving Agents, Empirical-MCTS, AgentArk distillation)
- Application-specific benchmarks (PieArena MBA negotiation, H-AdminSim hospital admin)
- Healthcare agentic evaluation (7-dimensional taxonomy)

---

## Papers

### Multi-Agent Core Research

| Paper | ID | Focus |
|-------|-----|-------|
| DyTopo | 2602.06039 | Dynamic topology routing with semantic matching |
| AgenticPay | 2602.06008 | Multi-agent negotiation benchmark for transactions |
| M²-Miner | 2602.05429 | GUI agent data mining with specialized roles |
| TKG-Thinker | 2602.05818 | Temporal knowledge graph reasoning via agentic RL |
| Graph-based Agent Memory | 2602.05665 | 18-author survey on agent memory systems |
| ProAct | 2602.05327 | Agentic lookahead for long-horizon planning |
| Internet of Agentic AI | 2602.03145 | Distributed coalition formation |
| AgentXRay | 2602.05353 | Workflow reconstruction (white-boxing black-box agents) |
| PieArena | 2602.05302 | MBA negotiation with behavioral profiling |
| H-AdminSim | 2602.05407 | Hospital admin with FHIR integration |
| SocialVeil | 2602.05115 | Social intelligence barriers (45% mutual understanding reduction) |
| GAMMS | 2602.05105 | Lightweight multi-agent simulation framework |
| CommCP | 2602.06038 | LLM-based communication with conformal prediction |
| Learning to Share | 2602.05965 | Parallel agentic memory reuse across teams |
| AI Agent Supply Chains | 2602.05524 | Structured decision prompts for inventory |
| LinguistAgent | 2602.05493 | Dual-agent workflow for linguistic annotation |
| Towards Science of Collective AI | 2602.05289 | Collaboration gain metric Γ for scientific MAS |
| Data-Centric Interpretability (MARL) | 2602.05183 | SAE-based LLM MARL training analysis |
| CoWork-X | 2602.05004 | Skill-based HTN retrieval with co-evolution |
| Group-Evolving Agents (GEA) | 2602.04837 | Open-ended self-improvement via experience sharing |
| WideSeek-R1 | 2602.04634 | Width scaling via MARL for info seeking (4B≈671B) |
| Vibe AIGC | 2602.04575 | Content generation via agentic orchestration |
| PCE (Assumptions to Actions) | 2602.04326 | Uncertainty-aware planning for embodied agents |
| Agent-Omit | 2602.04284 | Adaptive thought/observation omission |
| Empirical-MCTS | 2602.04248 | Continuous evolution via dual-experience MCTS |
| OMG-Agent | 2602.04144 | Missing modality generation (coarse-to-fine workflow) |
| Agentic AI Healthcare Taxonomy | 2602.04813 | 7-dimension evaluation framework (49 studies) |

### Efficiency & Infrastructure

| Paper | ID | Focus |
|-------|-----|-------|
| RL-VLA³ | 2602.05765 | Full asynchronism: 59-127% throughput improvement |
| S3-CoT | 2602.01982 | Succinct Chain-of-Thought with System 1/2 cognitive |
| SpecMD | 2602.03921 | MoE caching with Least-Stale eviction |
| SAR-RAG | 2602.04712 | SAR target recognition with RAG |
| DARWIN | 2602.05848 | Self-improving evolutionary GPT |
| DeepRead | 2602.05014 | Structure-aware agentic document QA |
| AgentArk | 2602.03955 | Distills multi-agent intelligence into single model |

### Applications & Specialization

| Paper | ID | Focus |
|-------|-----|-------|
| PL-Distill | 2602.01547 | Audio-Language: 8.4B→1.1B compression |
| OmniVideo-R1 | 2602.05847 | Audio-visual reasoning pipeline |
| Human Bias Emulation | 2602.05597 | Decision modeling with GPT agents |
| Structured Context Engineering | 2602.05447 | File-native agentic systems (9,649 experiments) |
| Capture the Flags | 2602.05523 | Agentic LLM evaluation via semantic transformations |

### Methodology & Safety

| Paper | ID | Focus |
|-------|-----|-------|
| LLM Risk Assessment | 2602.04358 | Systems Engineering classification framework |
| THOR | 2602.05424 | Inductive link prediction for hyper-relational KGs |
| MoE Expert Selection Attack | 2602.04105 | Security vulnerability in MoE routing |
| Understanding LLM Evaluators | 2602.05110 | Multi-evaluator framework with bias metrics |

---

## Detailed Summaries

### DyTopo: Dynamic Topology Routing
**ID:** 2602.06039
**Key:** Semantic matching for agent communication
**Approach:** Dynamic routing based on semantic compatibility between agents
**Impact:** Enables scalable multi-agent systems with heterogeneous capabilities

### AgenticPay: Multi-Agent Negotiation Benchmark
**ID:** 2602.06008
**Key:** Buyer-seller transaction scenarios
**Approach:** Standardized benchmark for evaluating multi-agent negotiation strategies
**Impact:** Provides reproducible framework for trading agent research

### M²-Miner: Multi-Agent MCTS Data Mining
**ID:** 2602.05429
**Key:** GUI agents with specialized roles
**Approach:** Multiple agents with distinct capabilities coordinating via MCTS
**Impact:** Complex task decomposition for data extraction from GUI applications

### TKG-Thinker: Temporal Knowledge Graph Reasoning
**ID:** 2602.05818
**Key:** Dynamic reasoning via agentic RL
**Approach:** Agents navigate temporal knowledge graphs to solve reasoning tasks
**Impact:** Advances in temporal understanding and reasoning for agentic systems

### Graph-based Agent Memory: Survey
**ID:** 2602.05665
**Key:** 18-author comprehensive survey
**Approach:** Taxonomy of memory architectures for multi-agent systems
**Impact:** Foundation for understanding memory in agent collectives

### ProAct: Agentic Lookahead Planning
**ID:** 2602.05327
**Key:** Long-horizon planning
**Approach:** GLAD + MC-Critic for foresighted decision-making
**Impact:** Enables agents to plan beyond immediate rewards

### Internet of Agentic AI
**ID:** 2602.03145
**Key:** Distributed coalition formation
**Approach:** Agents form临时 coalitions for collaborative tasks
**Impact:** Framework for large-scale distributed agentic ecosystems

### AgentXRay: Workflow Reconstruction
**ID:** 2602.05353
**Key:** White-boxing black-box agents
**Approach:** Reverse-engineer agent workflows from inputs/outputs
**Impact:** Improves interpretability and debugging of complex agents

### RL-VLA³: Full Asynchronism
**ID:** 2602.05765
**Key:** 59-127% throughput boost
**Approach:** Vision-Language-Action agents with asynchronous execution
**Impact:** Major efficiency gains for multi-modal agentic systems

### PieArena: MBA Negotiation Benchmark
**ID:** 2602.05302
**Key:** Behavioral profiling
**Approach:** Simulates MBA student negotiation scenarios
**Impact:** Realistic benchmark for human-like multi-agent negotiation

### H-AdminSim: Hospital Administration
**ID:** 2602.05407
**Key:** FHIR integration
**Approach:** Multi-agent simulation of hospital workflows
**Impact:** Healthcare-specific agentic system evaluation

### SocialVeil: Social Intelligence Barriers
**ID:** 2602.05115
**Key:** 45% mutual understanding reduction
**Approach:** Introduces communication barriers to study social intelligence
**Impact:** Insights into robustness of multi-agent communication

### GAMMS: Graph Simulation Framework
**ID:** 2602.05105
**Key:** Lightweight multi-agent simulation
**Approach:** Graph-based framework for testing multi-agent algorithms
**Impact:** Standardized testing environment for MAS research

### CommCP: Multi-Agent Coordination
**ID:** 2602.06038
**Key:** LLM-based communication
**Approach:** Conformal prediction for reliable agent communication
**Impact:** Addresses uncertainty in multi-agent message passing

### Learning to Share: Parallel Agentic Memory
**ID:** 2602.05965
**Key:** Cross-team memory reuse
**Approach:** Selective sharing of learned information between teams
**Impact:** Enables knowledge transfer in multi-team environments

### AI Agent Supply Chains
**ID:** 2602.05524
**Key:** Structured decision prompts
**Approach:** Decision templates for inventory management
**Impact:** Practical application of agentic planning

### LinguistAgent: Annotation Platform
**ID:** 2602.05493
**Key:** Dual-agent workflow
**Approach:** Two-agent system for linguistic annotation tasks
**Impact:** Automated data pipeline for NLP research

### Towards Science of Collective AI
**ID:** 2602.05289
**Key:** Collaboration gain metric Γ
**Approach:** Scientific framework for measuring multi-agent performance
**Impact:** Foundation for systematic MAS research

### Data-Centric Interpretability for LLM-based MARL
**ID:** 2602.05183
**Key:** SAE-based training analysis
**Approach:** Uses sparse autoencoders to interpret MARL training
**Impact:** Improves understanding of LLM in multi-agent RL

### CoWork-X: Experience-Optimized Co-Evolution
**ID:** 2602.05004
**Key:** Skill-based HTN retrieval
**Approach:** Hierarchical task networks with co-evolution
**Impact:** Dynamic skill acquisition in collaborative settings

### Group-Evolving Agents (GEA): Open-Ended Self-Improvement
**ID:** 2602.04837
**Key:** Experience sharing across group
**Approach:** Treats agent group as evolutionary unit for sharing/reuse
**Results:** 71.0% vs 56.7% on SWE-bench Verified; 88.3% vs 68.3% on Polyglot
**Impact:** Converts exploratory diversity into long-term progress; 1.4 vs 5 iterations for framework bug fixes

### Agentic AI Healthcare: Seven-Dimensional Taxonomy
**ID:** 2602.04813
**Key:** Evaluation framework for medical agents
**Approach:** 7 dimensions with 29 sub-dimensions across 49 studies (Cognitive, Knowledge, Interaction, Adaptation, Safety, Framework, Tasks)
**Results:** External Knowledge Integration ~76% implemented; Event-Triggered Activation ~92% not implemented; Drift Detection ~98% not implemented
**Impact:** Identifies gaps: Treatment Planning ~59% not implemented; Multi-Agent Design ~82% dominant pattern

### WideSeek-R1: Width Scaling via MARL
**ID:** 2602.04634
**Key:** Lead-agent-subagent framework with parallel execution
**Approach:** MARL-trained coordination for broad information seeking (20k tasks)
**Results:** WideSeek-R1-4B achieves 40.0% F1 on WideSearch ≈ DeepSeek-R1-671B
**Impact:** Width scaling enables small models to match large; gains scale with parallel subagents

### Vibe AIGC: Content Generation via Orchestration
**ID:** 2602.04575
**Key:** Meta-Planner with Commander-Vibe paradigm
**Approach:** User provides "Vibe" (aesthetic/logic); Meta-Planner deconstructs into agentic pipelines
**Impact:** Shifts from stochastic inference to logical orchestration; democratizes complex asset creation

### PCE: Planner-Composer-Evaluator for Embodied Agents
**ID:** 2602.04326
**Key:** Uncertainty-aware planning with decision trees
**Approach:** Converts LLM assumptions into structured decision tree (assumptions→actions)
**Results:** Outperforms communication-centric baselines on C-WAH and TDW-MAT; ICLR 2026
**Impact:** Reduces communication overhead; produces human-perceived efficient/trustworthy patterns

### Agent-Omit: Adaptive Thought/Observation Omission
**ID:** 2602.04284
**Key:** Selective omission training via RL
**Approach:** Cold-start data + omit-aware RL with dual sampling
**Results:** Agent-Omit-8B comparable to 7 frontier LLM agents; best efficiency trade-off
**Impact:** Adaptive behavior reduces redundant computation during multi-turn interactions

### Empirical-MCTS: Continuous Agent Evolution
**ID:** 2602.04248
**Key:** Dual-loop framework (local + global memory)
**Approach:** PE-EMP for local meta-prompt evolution + Memory Optimization Agent
**Results:** Outperforms stateless MCTS and experience-driven agents on AIME25, ARC-AGI-2, MathArena Apex
**Impact:** Transforms stateless search into continuous learning; accumulates wisdom across problems

### OMG-Agent: Missing Modality Generation
**ID:** 2602.04144
**Key:** Decoupled coarse-to-fine workflow
**Approach:** 3 stages: MLLM Semantic Planner, Evidence Retriever, Retrieval-Injected Executor
**Results:** 2.6-point gain on CMU-MOSI at 70% missing rate
**Impact:** Overcomes Semantic-Detail Entanglement; robust under extreme missingness

### S3-CoT: Succinct Chain-of-Thought
**ID:** 2602.01982
**Key:** System 1/2 dual cognitive
**Approach:** Concise reasoning with fast and slow thinking
**Impact:** Efficiency improvements for agentic reasoning

### SpecMD: MoE Caching
**ID:** 2602.03921
**Key:** Least-Stale eviction
**Approach:** Cache management for Mixture-of-Experts models
**Impact:** Performance optimization for large-scale models

### SAR-RAG: Retrieval Augmented
**ID:** 2602.04712
**Key:** SAR target recognition
**Approach:** RAG for Synthetic Aperture Radar analysis
**Impact:** Specialized application of retrieval-augmented systems

### DARWIN: Self-Improving Network
**ID:** 2602.05848
**Key:** Evolutionary GPT
**Approach:** Genetic algorithm-based model improvement
**Impact:** Autonomous model optimization

### DeepRead: Document-Aware Search
**ID:** 2602.05014
**Key:** Structure-aware agentic QA
**Approach:** Leverages document structure for better QA
**Impact:** Improves document understanding for agents

### AgentArk: Distilling Multi-Agent Intelligence
**ID:** 2602.03955
**Key:** Multi-agent to single-agent distillation
**Approach:** 3 strategies: reasoning-enhanced fine-tuning, trajectory augmentation, process-aware distillation
**Impact:** Transforms test-time interactions into model weights; maintains reasoning of multi-agent with single-agent efficiency

### PL-Distill: Audio-Language Compression
**ID:** 2602.01547
**Key:** 8.4B→1.1B model compression
**Approach:** Knowledge distillation for multimodal models
**Impact:** Enables deployment of large audio-language models

### OmniVideo-R1: Audio-Visual Reasoning
**ID:** 2602.05847
**Key:** Multi-modal reasoning
**Approach:** Integrated audio-visual analysis pipeline
**Impact:** Advances multi-modal agentic reasoning

### Human Bias Emulation
**ID:** 2602.05597
**Key:** Decision modeling
**Approach:** GPT agents emulate human cognitive biases
**Impact:** Better modeling of human-AI interaction

### Structured Context Engineering
**ID:** 2602.05447
**Key:** File-native agentic systems
**Approach:** 9,649 experiments on context structure
**Impact:** Empirical insights into agent context management

### Capture the Flags
**ID:** 2602.05523
**Key:** Agentic LLM evaluation
**Approach:** Security competition-style evaluation
**Impact:** Novel framework for testing agent capabilities

### LLM Risk Assessment Framework
**ID:** 2602.04358
**Key:** Systems Engineering classification
**Approach:** Taxonomy of LLM risks from SE perspective
**Impact:** Structured approach to agent safety

### THOR: Inductive Link Prediction
**ID:** 2602.05424
**Key:** Hyper-relational knowledge graphs
**Approach:** Inductive learning for KG completion
**Impact:** Advances knowledge graph reasoning

### MoE Expert Selection Attack
**ID:** 2602.04105
**Key:** Security vulnerability
**Approach:** Attacks MoE routing mechanisms
**Impact:** Security concerns for large-scale models

### Understanding LLM Evaluators
**ID:** 2602.05110
**Key:** Bias metrics
**Approach:** Multi-evaluator framework with statistical analysis
**Impact:** Improves evaluation methodology

---

## Cross-Cutting Trends

### 1. Communication Protocols
- **Semantic routing** (DyTopo)
- **Conformal prediction** (CommCP)
- **Selective sharing** (Learning to Share)

### 2. Memory Systems
- Large-scale survey (18 authors)
- Cross-team knowledge transfer
- Graph-based architectures

### 3. Efficiency Breakthroughs
- Asynchronous execution (59-127% gains)
- Succinct reasoning (System 1/2)
- Model compression (8.4B→1.1B)

### 4. Specialized Benchmarks
- Negotiation (PieArena, AgenticPay)
- Healthcare (H-AdminSim)
- Security (Capture the Flags)

### 5. Interpretability Focus
- Agent workflow reconstruction
- SAE-based MARL analysis
- LLM evaluator bias metrics

### 6. Self-Improvement Paradigms
- Group-evolution with experience sharing
- Continuous empirical accumulation (Empirical-MCTS)
- Model distillation (AgentArk: multi→single agent)

### 7. Domain-Specific Evaluation
- Healthcare 7-dimensional taxonomy
- Negotiation benchmarks
- Missing modality generation workflows

---

## Research Directions Identified

### High Priority
1. Standard communication protocols for heterogeneous agents
2. Scalable memory architectures for large collectives
3. Async execution patterns for throughput optimization

### Medium Priority
1. Domain-specific benchmarks (healthcare, negotiation, security)
2. Interpretability tools for multi-agent systems
3. Knowledge transfer mechanisms between teams

### Emerging
1. Coalition formation in open environments
2. Social intelligence barriers and robustness
3. File-native agentic architectures

---

## Data Collection Notes
- **Date range:** Feb 2-6, 2026 (arXiv IDs: 2602.0xxxx)
- **Source:** arXiv cs.AI category
- **Scan status:** Entries 1-250 of 1,516 total
- **Method:** WebFetch tool with markdown format
- **Focus:** Multi-agent/agentic systems with coordination, collaboration, or collective intelligence