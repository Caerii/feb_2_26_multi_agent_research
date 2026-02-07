# Multi-Agent AI Research - February 2-6, 2026

## Exec Summary

Total papers analyzed: **132 multi-agent systems** from arXiv cs.AI

**Key themes emerging:**
- Agentic coordination protocols (CommCP, CoWork-X, Learning to Share)
- Multi-agent memory systems (Graph-based Agent Memory survey)
- Dynamic topology management (DyTopo, TKG-Thinker)
- Efficiency breakthroughs (RL-VLA³: 59-127% throughput gains; WideSeek-R1 width scaling)
- Agent self-improvement (Group-Evolving Agents, Empirical-MCTS, AgentArk distillation)
- Application-specific benchmarks (PieArena MBA negotiation, H-AdminSim hospital admin)
- Healthcare agentic evaluation (7-dimensional taxonomy)
- Scientific domain agents (Quntur: quantum chemistry research collaborator)
- Software engineering agents (star topology test generation, document retrieval)
- Multi-expert orchestration interpretability (INFORM causal vs relational importance)
- 3D scene understanding (multi-agent scene graph generation)
- Distributed training optimization (LoRDO ~10× communication reduction)
- Collaborative planning (KG-guided multi-robot replanning)
- Agent scaling theory (diversity beats quantity; K* effective channels)
- Automated orchestration (AOrchestra tuple abstraction)
- Dynamic communication topology (TodyComm policy gradient)
- Routing collapse mitigation (EquiRouter decision-aware ranking)
- Actor-Refiner search collaboration (Search-R2 targeted correction)
- Proactive intent modeling (IntentRL RL framework)
- Compositional skill synthesis (Agentic Proposing synthetic trajectories)
- Framework benchmarking (MAFBench unified evaluation)
- Process verification (MAS-ProVe cross-paradigm study)
- Division of labor patterns (Analyzer-Reasoner-Executor for time series)
- Synthetic data generation (Socratic-Geo autonomous data-model coupling)
- Traffic coordination (MADT graph attention for intersection coordination)
- Multi-turn interaction strategies (MedSAM-Agent clinical fidelity rewards)
- Security task automation (CVE-Factory expert-level CVE task generation)
- Memory-based scaling (MeKi ROM-based knowledge injection with zero latency)
- Auction-based coordination (SALE freelancer marketplace strategy bidding)
- Wide Research paradigm (WideSeek dynamic hierarchical agent forking)
- Production observability (Agentic Observability ReAct for alert triage)
- PR-grounded long-horizon (daVinci-Agency chain-of-PR trajectory mining)
- Bandwidth-efficient communication (information bottleneck + vector quantization)
- Self-evolving coordination (governed protocol modification with invariants)
- Collective intelligence (SuperBrain swarm co-evolution to meta-intelligence)
- Privacy-preserving swarms (MPC-encrypted LLM UAV coordination)
- Human-swarm teaming (LLM-CRF bridges intention-to-action gap in SAR)
- Graph-based tool planning (tool knowledge graph fusion with domain knowledge)
- Agent action ordering (AOAD-MAT explicit sequence prediction in MARL)
- Convention-based cooperation (augmented action space with implicit knowledge sharing)
- Hierarchical agentic reasoning (multi-strategy coordination for science)
- Interpretable alignment (rubric-based reward models for long-horizon tasks)
- FSM-based orchestration (finite-state machine routing for desktop automation)
- Knowledge-aware routing (privacy-preserving KB relevance signals)
- Visual planning agents (VLLM zero-shot physical task planning)
- PDDL-LLM coordination (separated team-level and robot-level planning)
- LLM coordination benchmark (pure coordination settings with ToM evaluation)
- Linguistic negotiation effects (language choice shifts agent outcomes)

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
| PieArena | 2602.05302 | MBA negotiation benchmark with behavioral profiling |
| SocialVeil | 2602.05115 | Social intelligence barriers (45% mutual understanding reduction) |
| GAMMS | 2602.05105 | Lightweight multi-agent simulation framework |
| CommCP | 2602.06038 | LLM-based communication with conformal prediction |
| Learning to Share | 2602.05965 | Parallel agentic memory reuse across teams |
| LinguistAgent | 2602.05493 | Dual-agent workflow for linguistic annotation |
| Towards Science of Collective AI | 2602.05289 | Collaboration gain metric Γ for scientific MAS |
| Data-Centric Interpretability (MARL) | 2602.05183 | SAE-based LLM MARL training analysis |
| CoWork-X | 2602.05004 | Skill-based HTN retrieval with co-evolution |
| Group-Evolving Agents (GEA) | 2602.04837 | Open-ended self-improvement via experience sharing |
| PCE (Assumptions to Actions) | 2602.04326 | Uncertainty-aware planning for embodied agents |
| Agent-Omit | 2602.04284 | Adaptive thought/observation omission |
| Empirical-MCTS | 2602.04248 | Continuous evolution via dual-experience MCTS |
| INFORM | 2602.04291 | Causal analysis for multi-expert orchestration |
| MA3DSG | 2602.04152 | Multi-agent 3D scene graph generation |
| KGLAMP | 2602.04129 | KG-guided multi-robot planning/replanning |
| WideSeek-R1 | 2602.04634 | Width scaling via MARL for info seeking (4B≈671B) |
| Agent Scaling via Diversity | 2602.03794 | Information-theoretic framework: 2 diverse ≈ 16 homogeneous |
| AOrchestra | 2602.03786 | Automated sub-agent creation (16.28% improvement) |
| TodyComm | 2602.03688 | Task-oriented dynamic communication topology |
| Conversational Inertia | 2602.03664 | Context Preference Learning for multi-turn agents |
| EquiRouter | 2602.03478 | Decision-aware ranking (17% cost reduction) |
| Search-R2 | 2602.03647 | Actor-Refiner collaboration for search reasoning |
| IntentRL | 2602.03468 | Proactive user-intent agents via RL |
| Agentic Proposing | 2602.03279 | Compositional skill synthesis with trajectories |
| Understanding Multi-Agent LLM Frameworks | 2602.03128 | MAFBench unified evaluation for frameworks |
| MAS-ProVe | 2602.03053 | Process verification across paradigms |
| Visual Reasoning over Time Series (MAS4TS) | 2602.03026 | Analyzer-Reasoner-Executor paradigm |
| Socratic-Geo | 2602.03414 | Synthetic data generation via multi-agent |
| MADT (Traffic Coordination) | 2602.02903 | Multi-agent traffic via sequence modeling |
| SALE (Strategy Auctions) | 2602.02751 | Auction-based scaling for small agents |
| WideSeek | 2602.02636 | Dynamic hierarchical Wide Research |
| daVinci-Agency | 2602.02619 | Long-horizon via PR-grounded synthesis |
| Live-Evo | 2602.02369 | Online evolution of agentic memory |
| ProcMEM | 2602.01869 | Reusable procedural memory via Non-Parametric PPO |
| ROMA | 2602.01848 | Recursive Open Meta-Agent for long-horizon tasks |
| Persuasion Propagation | 2602.00851 | Belief-level intervention impact on agent behavior |
| InfoReasoner | 2602.00845 | Information gain reward for retrieval reasoning |
| World Models | 2602.00785 | Intermediary between agents and real world |
| L²-VMAS | 2602.00471 | Dual latent memory for visual multi-agent |
| DebateOCR | 2602.00454 | Cross-modal compression for multi-agent debate |
| Synapse | 2602.00911 | Federated knowledge exchange for tool-routed LLMs |
| ADP-MA | 2602.00307 | Meta-agents for autonomous data processing |
| A-Evolve | 2602.00359 | Agentic evolution for LLM adaptation |
| SECP | 2602.02170 | Self-evolving coordination protocols with governance |
| Multi-Agent Teams Hold Experts Back | 2602.01011 | Self-organizing team performance study |
| DeALOG | 2602.00996 | Decentralized log-mediated reasoning framework |
| SuperBrain | 2509.00510 | LLM-assisted swarm intelligence for collective AI |
| PrivLLMSwarm | 2512.06747 | Privacy-preserving LLM UAV swarms |
| Human-Swarm Teaming | 2511.04042 | LLM-based disaster rescue framework |
| Graph-Based In-Context Planning | 2510.24690 | Tool knowledge graphs for planning |
| AOAD-MAT | 2510.13343 | Agent order of action decisions in MARL |
| Hanabi Conventions | 2412.06333 | Action space augmentation for cooperation |
| Differential Voting | 2601.18824 | Axiomatically diverse preference aggregation |
| Beyond Majority Voting | 2510.01499 | Higher-order LLM aggregation algorithms |
| MASTER | 2512.13930 | Hierarchical multi-agent LLM reasoning for materials discovery |
| ARCANE | 2512.06196 | Multi-agent framework for interpretable alignment |
| Agentic Reasoning Survey | 2601.12538 | Comprehensive agentic reasoning survey |
| SMAGDi | 2511.05528 | Socratic interaction graph distillation for efficiency |
| AutoTool | 2512.13278 | Dynamic tool selection for agentic reasoning |
| Agentic Lybic | 2509.11067 | Multiagent execution with tiered orchestration |
| Multi-Agent Orchestration Survey | 2601.13671 | Architectures, protocols, enterprise adoption |
| KBA Orchestration | 2509.19599 | Knowledge base-aware routing for MAS |
| Wonderful Team | 2407.19094 | Zero-shot physical task planning with visual LLMs |
| PIP-LLM | 2510.22784 | PDDL-IP with LLMs for multi-robot coordination |
| LLM-Coordination | 2310.03903 | Benchmark for LLM multi-agent coordination |
| VirTLab | 2510.08242 | Interactive 2D environments for team dynamics |
| The Language of Bargaining | 2601.04387 | Linguistic effects in LLM negotiations |

### Efficiency & Infrastructure

| Paper | ID | Focus |
|-------|-----|-------|
| RL-VLA³ | 2602.05765 | Full asynchronism: 59-127% throughput improvement |
| S3-CoT | 2602.01982 | Succinct Chain-of-Thought with System 1/2 cognitive |
| SpecMD | 2602.03921 | MoE caching with Least-Stale eviction |
| DARWIN | 2602.05848 | Self-improving evolutionary GPT |
| DeepRead | 2602.05014 | Structure-aware agentic document QA |
| AgentArk | 2602.03955 | Distills multi-agent intelligence into single model |
| LoRDO | 2602.04396 | Distributed low-rank optimization (~10× comm reduction) |
| Med-MMFL | 2602.04416 | Multimodal federated learning benchmark |
| Blockchain FL | 2602.04384 | Blockchain FL for retail forecasting |
| FedKRSO | 2602.03019 | Communication/memory efficient FL fine-tuning |
| SparVAR | 2602.04361 | Training-free sparse attention (>5× faster) |
| MeKi | 2602.03359 | Memory-based expert knowledge injection |
| RAP | 2602.02599 | KV-Cache compression via RoPE-aligned pruning |
| SIDiffAgent | 2602.02051 | Self-improving diffusion agent with memory database |
| Bandwidth-Efficient Multi-Agent Comm | 2602.02035 | Information bottleneck + vector quantization |
| COLT | 2602.01935 | Lightweight multi-LLM collaboration via shared MCTS |
| TABX | 2602.01665 | High-throughput sandbox battle simulator |
| Less is More | 2504.16408 | Quality-guided distillation for structured reasoning |

### Methodology & Safety

| Paper | ID | Focus |
|-------|-----|-------|
| LLM Risk Assessment | 2602.04358 | Systems Engineering classification framework |
| THOR | 2602.05424 | Inductive link prediction for hyper-relational KGs |
| MoE Expert Selection Attack | 2602.04105 | Security vulnerability in MoE routing |
| Understanding LLM Evaluators | 2602.05110 | Multi-evaluator framework with bias metrics |
| AgentRx | 2602.02475 | Agent failure diagnosis from execution trajectories |
| Drift-Bench | 2602.02455 | Cooperative breakdown diagnosis under input faults |
| Persuasion Propagation | 2602.00851 | Belief-level intervention framework |
| CAM | 2602.02138 | Causality-based analysis for code generation systems |
| 4C Framework | 2602.01942 | Human society-inspired agentic security framework |
| SafePred | 2602.01725 | Predictive guardrail via world models |
| MAEBE | 2506.03053 | Multi-agent emergent behavior evaluation framework |

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

### INFORM: Multi-Expert Orchestration Analysis
**ID:** 2602.04291
**Key:** Causal vs. relational importance disentanglement
**Approach:** Treats orchestration as explicit computation; decouples interaction structure, execution order, causal attribution
**Results:** Tested on GSM8K, HumanEval, MMLU with 10 8B experts (LLaMA-3.1, Qwen-3, DeepSeek-R1); routing dominance ≠ functional necessity; sparsely routed experts often structurally critical
**Impact:** Exposes causal/structural dependencies beyond accuracy; informs multi-agent system design

### MA3DSG: Multi-Agent 3D Scene Graph Generation
**ID:** 2602.04152
**Key:** Training-free graph alignment for large-scale environments
**Approach:** Multiple agents generate partial scene graphs; graph alignment algorithm merges into unified global graph
**Results:** MA3DSG-Bench supports diverse agent configurations and domain sizes
**Impact:** First scalable multi-agent 3D scene graph framework; enables collaborative single-agent systems

### KGLAMP: Knowledge Graph-Guided Multi-Robot Planning
**ID:** 2602.04129
**Key:** KG as persistent memory for heterogeneous robot teams
**Approach:** Structured KG encodes object relations, spatial reachability, robot capabilities; guides LLM in PDDL spec generation; triggers replanning on inconsistencies
**Results:** ≥25.5% performance improvement over LLM-only and PDDL-based variants on MAT-THOR benchmark
**Impact:** Addresses agent heterogeneity and dynamic environments; bridges symbolic and neural planning

### LoRDO: Distributed Low-Rank Optimization
**ID:** 2602.04396
**Key:** Low-rank + infrequent communication unification
**Approach:** Low-rank optimization framework with local updates and periodic synchronization; includes full-rank quasi-hyperbolic update for subspace exploration
**Results:** Near-parity with low-rank DDP at 125M-720M scale; ~10× communication reduction; improved performance in low-memory settings
**Impact:** Enables distributed training with bandwidth-limited interconnects

### Med-MMFL: Multimodal Federated Learning Benchmark
**ID:** 2602.04416
**Key:** First comprehensive medical MMFL benchmark
**Approach:** Evaluates 6 FL algorithms across 2-4 modalities (10 total medical modalities: text, pathology, ECG, X-ray, reports, MRI sequences)
**Results:** Tests segmentation, classification, modality alignment, VQA across iid/non-iid settings
**Impact:** Standardized evaluation for privacy-preserving medical AI; reproducibility framework with data/partitioning pipelines

### Blockchain Federated Learning for Retail
**ID:** 2602.04384
**Key:** Collaborative demand forecasting without data sharing
**Approach:** Blockchain-based FL across multiple grocery retailers for perishable goods demand forecasting
**Results:** FL models ≈ ideal shared-data performance; superior to isolated models; reduces waste and boosts efficiency (ISCC 2025)
**Impact:** Addresses data privacy in sustainable supply chain; collaborative learning across competitive retailers

### Tinker Tales: Child-AI Collaborative Storytelling
**ID:** 2602.04109
**Key:** Co-creative storytelling with tangible + voice interaction
**Approach:** Physical storytelling board with NFC-embedded toys (characters, places, items, emotions); mobile app mediates child-AI collaboration
**Results:** 10-child study shows children treat AI as attentive collaborator; scaffolding supports narrative coherence without diminishing agency
**Impact:** Model for child-AI co-creation beyond instructional settings; educational scaffolding design

### MedSAM-Agent: Multi-Turn Agentic RL for Medical Segmentation
**ID:** 2602.03320
**Key:** Multi-turn autonomous decision-making for interactive medical image segmentation
**Approach:** Hybrid prompting strategy for expert-curated trajectory generation; two-stage training pipeline with multi-turn end-to-end outcome verification and clinical-fidelity process reward design; promotes interaction parsimony and decision efficiency
**Results:** State-of-the-art performance across 6 medical modalities and 21 datasets
**Impact:** Bridges gap between single-turn rigid interaction and dynamic interactive potential

### CVE-Factory: Scaling Expert-Level Agentic Tasks for Code Security
**ID:** 2602.03012
**Key:** Multi-agent framework for automatic CVE task generation
**Approach:** Transforms sparse CVE metadata into fully executable agentic tasks through multi-agent collaboration
**Results:** 95% solution correctness, 96% environment fidelity vs human experts; 66.2% verified success on latest realistic vulnerabilities; LiveCVEBench: 190 tasks across 14 languages; Fine-tuned Qwen3-32B: 5.3%→35.8%, surpassing Claude 4.5 Sonnet
**Impact:** First large-scale scaling (1,000+ environments); continuous benchmarking of emerging threats including AI-tooling vulnerabilities

---

### SparVAR: Training-Free Sparse Visual Autoregressive
**ID:** 2602.04361
**Key:** Exploits VAR attention properties for acceleration
**Approach:** Dynamically predicts sparse attention pattern from sparse decision scale; cross-scale local sparse attention with block-wise efficient kernel
**Results:** >5× faster than FlashAttention; 1.57× speed-up while preserving details; 8B model generates 1024×1024 in ~1s; up to 2.28× with scale-skipping
**Impact:** Training-free acceleration enables high-resolution image generation without last-scale skipping

### MeKi: Memory-based Expert Knowledge Injection
**ID:** 2602.03359
**Key:** Storage-based LLM scaling with zero inference latency overhead
**Approach:** Equips each Transformer layer with token-level memory experts injecting pre-stored semantic knowledge; re-parameterization folds training parameters into compact static lookup table; offloads knowledge to ROM
**Results:** Significantly outperforms dense LLM baselines with identical inference speed
**Impact:** Decouples model capacity from computational cost; enables on-device LLM scaling via ROM instead of FLOPs

### SALE (Strategy Auctions): Scaling Small Agents Through Auction-Based Coordination
**ID:** 2602.02751
**Key:** Freelancer marketplace-inspired agent coordination via strategy auctions
**Approach:** Agents bid with short strategic plans scored by cost-value mechanism; shared auction memory enables per-task routing and continual self-improvement without separate router training or full model execution
**Results:** Reduces reliance on largest agent by 53%; lowers overall cost by 35%; consistently improves upon largest agent's pass@1 with negligible overhead
**Impact:** Demonstrates systems-level view where gains come from market-inspired coordination, not larger models; enables efficient heterogeneous agent ecosystems

### WideSeek: Dynamic Hierarchical Multi-Agent Architecture for Wide Research
**ID:** 2602.02636
**Key:** Parallel information synthesis under complex constraints via agent scaling
**Approach:** Dynamic hierarchical architecture autonomously forks parallel sub-agents based on task requirements; unified training framework linearizes multi-agent trajectories with end-to-end RL; WideSeekBench benchmark for General Broad Information Seeking
**Results:** Demonstrates effectiveness of multi-agent scaling for Wide Research paradigm
**Impact:** Establishes new paradigm shift from Deep Research to Wide Research; shows agent scaling as promising direction for broad information retrieval

### daVinci-Agency: Long-Horizon Agency via PR-Grounded Trajectory Synthesis
**ID:** 2602.02619
**Key:** Authentic long-dependency data mining from Pull Request sequences
**Approach:** Three mechanisms mining structured supervision from chain-of-PRs: progressive task decomposition via continuous commits, long-term consistency enforcement via unified objectives, verifiable refinement from bug-fix trajectories
**Results:** 239 samples averaging 85k tokens and 116 tool calls; fine-tuning GLM-4.6 achieves 47% relative gain on Toolathlon
**Impact:** Preserves causal dependencies and iterative refinements essential for persistent goal-directed behavior; enables project-level full-cycle task modeling

### Agentic Observability: Automated Alert Triage
**ID:** 2602.02585
**Key:** Production-deployed ReAct agent for observability (Adobe E-Commerce)
**Approach:** Autonomous alert triage using ReAct paradigm;动态 identifies affected service, retrieves correlated logs across distributed systems, plans context-dependent actions (handbook, runbook, RAG code analysis)
**Results:** 90% reduction in mean time to insight vs manual triage; comparable diagnostic accuracy
**Impact:** Demonstrates order-of-magnitude reduction in enterprise triage latency; marks pivotal shift toward autonomous observability in production

### Understanding Agent Scaling in LLM-Based MAS via Diversity
**ID:** 2602.03794
**Key:** Diversity > homogeneous scaling for MAS performance
**Approach:** Information-theoretic framework showing performance bounded by intrinsic task uncertainty, not agent count; introduces K* effective channel metric
**Results:** 2 diverse agents match/exceed 16 homogeneous agents; homogeneous agents saturate early due to correlated outputs
**Impact:** Principled guidelines for diversity-aware MAS design; challenges naive scaling assumptions

### AOrchestra: Automated Sub-Agent Creation for Agentic Orchestration
**ID:** 2602.03786
**Key:** Framework-agnostic agent tuple abstraction (Instruction, Context, Tools, Model)
**Approach:** Central orchestrator concretizes tuple at each step: curates context, selects tools/models, delegates via automatic agent creation
**Results:** 16.28% relative improvement vs strongest baseline across GAIA, SWE-Bench, Terminal-Bench with Gemini-3-Flash; Pareto-efficient performance-cost trade-off
**Impact:** Reduces human engineering; enable plug-and-play diverse agents as task executors

### TodyComm: Task-Oriented Dynamic Communication for Multi-Round MAS
**ID:** 2602.03688
**Key:** Behavior-driven collaboration topology adaptation per round
**Approach:** Dynamic communication algorithm optimizing task utility via policy gradient; adapts to changing roles due to adversary, task progression, bandwidth
**Results:** Superior task effectiveness under dynamic adversary and communication budgets; retains token efficiency and scalability across 5 benchmarks
**Impact:** Addresses fixed topology limitation in realistic multi-round applications

### Mitigating Conversational Inertia in Multi-Turn Agents
**ID:** 2602.03664
**Key:** Addresses diagonal attention causing imitation bias in multi-turn agents
**Approach:** Context Preference Learning calibrates model to favor low-inertia over high-inertia responses; leverages context length differences for preference pairs
**Results:** Validated across 8 agentic environments and 1 deep research scenario; reduces conversational inertia with performance improvements
**Impact:** Resolves exploitation-exploration tension in few-shot LLM agents

### When Routing Collapses: EquiRouter for Degenerate Convergence
**ID:** 2602.03478
**Key:** Routing collapse - routers default to expensive models as budget increases
**Approach:** Decision-aware router (EquiRouter) directly learns model rankings instead of scalar performance scores; addresses objective-decision mismatch
**Results:** ~17% cost reduction at GPT-4-level performance on RouterBench vs strongest prior router
**Impact:** Restores small model utilization; fundamental fix for routing efficiency promises

### Search-R2: Actor-Refiner Collaboration for Search-Integrated Reasoning
**ID:** 2602.03647
**Key:** Multi-scale credit assignment via Actor-Refiner decomposition
**Approach:** Actor produces initial reasoning trajectories; Meta-Refiner selectively diagnoses and repairs flawed steps via cut-and-regenerate; hybrid reward (outcome + dense information density)
**Results:** Outperforms strong RAG and RL baselines across general and multi-hop QA datasets; superior accuracy with minimal overhead
**Impact:** Addresses sparse trajectory-level reward limitation; targeted intervention for search-integrated agents

### IntentRL: Proactive User-Intent Agents for Deep Research
**ID:** 2602.03468
**Key:** Reinforcement learning for proactive deep research agents
**Approach:** Formulates user-intent alignment as RL problem; agents learn to anticipate and proactively gather relevant information beyond explicit queries
**Results:** Demonstrates effectiveness on deep research benchmarks with improved coverage and relevance
**Impact:** Moves agentic systems from reactive to proactive; enables deeper research assistance

### Agentic Proposing: Compositional Skill Synthesis
**ID:** 2602.03279
**Key:** Modular skill composition via synthetic trajectories
**Approach:** Decomposes complex tasks into composable skills; uses synthetic trajectory generation for training; 30B solver achieves SOTA
**Results:** 91.6% on AIME25 with 11K synthetic trajectories; scales effectively with trajectory diversity
**Impact:** Demonstrates data-efficient skill learning; modular approach enables rapid skill acquisition

### Understanding Multi-Agent LLM Frameworks
**ID:** 2602.03128
**Key:** MAFBench unified evaluation for framework impact
**Approach:** Comprehensive benchmark testing different framework choices (memory, communication, routing) on multiple tasks
**Results:** Framework choices increase latency 100x+ for minor accuracy gains; identifies optimal configurations
**Impact:** Provides evidence for framework design decisions; highlights performance-cost trade-offs

### MAS-ProVe: Process Verification Across Paradigms
**ID:** 2602.03053
**Key:** Verification study across 3 paradigms and 4 context strategies
**Approach:** Evaluates process verification effectiveness across different MAS paradigms and context management strategies
**Results:** Identifies best combinations of verification approaches and context strategies
**Impact:** Advances understanding of verification in multi-agent systems; provides guidelines

### Visual Reasoning over Time Series (MAS4TS)
**ID:** 2602.03026
**Key:** Multi-agent Analyzer-Reasoner-Executor paradigm
**Approach:** Three-agent collaboration: Analyzer extracts insights, Reasoner performs reasoning, Executor produces answers for time series data
**Results:** Effective on visual reasoning benchmarks with time series data
**Impact:** Demonstrates multi-agent division of labor for complex temporal reasoning

### Socratic-Geo: Synthetic Data Generation and Geometric Reasoning
**ID:** 2602.03414
**Key:** Multi-agent interaction for autonomous geometric reasoning data synthesis
**Approach:** Teacher agent generates parameterized Python scripts with reflective feedback (Reflect for solvability, RePI for visual validity); Solver optimizes reasoning via preference learning; Generator distills programmatic drawing into visual generation; dynamic coupling of data synthesis with model learning
**Results:** Socratic-Solver achieves 49.11 on six benchmarks using 25% of baseline data; Socratic-Generator achieves 42.4% on GenExam (SOTA for open-source, approaching Gemini-2.5-Flash-Image at 43.1%); starting from only 108 seed problems
**Impact:** Fully autonomous framework addressing extreme scarcity of high-quality geometric reasoning image-text pairs; establishes new SOTA for open-source geometric reasoning models

### MADT: Multi-Agent Decision Transformer for Traffic Coordination
**ID:** 2602.02903
**Key:** Spatiotemporal sequence modeling for multi-intersection traffic coordination
**Approach:** Extends Decision Transformer to multi-agent settings: (1) graph attention for spatial dependencies between intersections, (2) temporal transformer encoder for traffic dynamics, (3) return-to-go conditioning for target performance; reformulates traffic control as sequence modeling problem
**Results:** Reduces average travel time by 5-6% compared to strongest baseline; superior coordination among adjacent intersections on synthetic and real-world scenarios
**Impact:** Enables offline learning from historical traffic data; sample-efficient alternative to RL for multi-agent traffic coordination

### Live-Evo: Online Evolution of Agentic Memory
**ID:** 2602.02369
**Key:** Continuous memory evolution from feedback
**Approach:** Online framework for agentic memory that evolves based on continuous user feedback
**Results:** Demonstrates effective memory adaptation over time
**Impact:** Enables agents to learn and improve from real-world interactions

### ProcMEM: Reusable Procedural Memory
**ID:** 2602.01869
**Key:** Non-Parametric PPO for memory reuse
**Approach:** Procedural memory system enabling skill reuse across tasks via Non-Parametric PPO
**Results:** Shows transferability of learned procedures
**Impact:** Reduces need for retraining in multi-agent systems

### ROMA: Recursive Open Meta-Agent
**ID:** 2602.01848
**Key:** Long-horizon task recursion
**Approach:** Hierarchical meta-agent that recursively decomposes long-horizon tasks
**Results:** Handles complex multi-step planning effectively
**Impact:** Advances long-horizon planning in agentic systems

### AgentRx: Agent Failure Diagnosis
**ID:** 2602.02475
**Key:** Trajectory-based failure diagnosis
**Approach:** Analyzes execution trajectories to diagnose agent failures
**Results:** Effective fault identification and localization
**Impact:** Improves reliability of multi-agent deployments

### Drift-Bench: Cooperative Breakdown Diagnosis
**ID:** 2602.02455
**Key:** Input fault scenarios
**Approach:** Benchmark for diagnosing cooperative failures under input faults
**Results:** Provides standardized evaluation of robustness
**Impact:** Enables better testing of multi-agent resilience

### SIDiffAgent: Self-Improving Diffusion Agent
**ID:** 2602.02051
**Key:** Memory database for diffusion
**Approach:** Self-improving agent with diffusion model and memory database
**Results:** Demonstrates continuous learning capability
**Impact:** Combines generative models with agentic memory

### Persuasion Propagation: Belief-Level Interventions
**ID:** 2602.00851
**Key:** Multi-agent belief dynamics
**Approach:** Framework for belief-level interventions that propagate through agent networks
**Results:** Shows significant impact on collective behavior
**Impact:** Advances understanding of influence in multi-agent systems

### InfoReasoner: Information Gain Reward
**ID:** 2602.00845
**Key:** Information-theoretic retrieval
**Approach:** Reward system based on information gain for retrieval reasoning
**Results:** Improves retrieval efficiency and relevance
**Impact:** Optimizes information access in agentic workflows

### World Models: Agent-World Intermediaries
**ID:** 2602.00785
**Key:** Environment modeling
**Approach:** World models act as intermediaries between agents and real world
**Results:** Better planning and decision-making
**Impact:** Reduces direct world interaction costs

### L²-VMAS: Dual Latent Memory for Visual MAS
**ID:** 2602.00471
**Key:** Visual multi-agent memory
**Approach:** Dual latent memory system for visual multi-agent environments
**Results:** Improved coordination in vision tasks
**Impact:** Advances visual multi-agent research

### DebateOCR: Cross-Modal Multi-Agent Debate
**ID:** 2602.00454
**Key:** OCR via debate
**Approach:** Multi-agent debate framework for OCR with cross-modal compression
**Results:** High accuracy for text recognition
**Impact:** Novel application of debate to computer vision

### Synapse: Federated Knowledge Exchange
**ID:** 2602.00911
**Key:** Tool-routed LLM federation
**Approach:** Federated knowledge exchange for tool-routed LLMs
**Results:** Effective knowledge sharing without data sharing
**Impact:** Enables collaborative LLM ecosystems

### ADP-MA: Meta-Agents for Data Processing
**ID:** 2602.00307
**Key:** Autonomous meta-agents
**Approach:** Meta-agents for autonomous data pipeline processing
**Results:** Efficient data handling at scale
**Impact:** Reduces manual pipeline engineering

### A-Evolve: Agentic Evolution for LLMs
**ID:** 2602.00359
**Key:** Position paper on evolution
**Approach:** Framework for agentic evolution to adapt LLMs over time
**Impact:** Sets direction for self-adapting language models

### SECP: Self-Evolving Coordination Protocol
**ID:** 2602.02170
**Key:** Governed protocol self-modification
**Approach:** Coordination protocols with validated self-modification while preserving formal invariants
**Results:** Recursive modification increased proposal coverage from 2 to 3 while preserving all invariants
**Impact:** Foundation for governed multi-agent systems in safety-critical domains

### CAM: Causality-Based Analysis for Code Generation
**ID:** 2602.02138
**Key:** Intermediate feature importance quantification
**Approach:** Causality framework analyzing intermediate outputs in multi-agent code generation systems
**Results:** Hybrid backend achieves 7.2% Pass@1 improvement; feature pruning reduces 66.8% token consumption
**Impact:** Provides actionable insights for MACGS design; enables failure repair

### Bandwidth-Efficient Multi-Agent Communication
**ID:** 2602.02035
**Key:** Information bottleneck + vector quantization
**Approach:** Compression + discretization with gated communication mechanism
**Results:** 181.8% performance improvement vs no-communication; 41.4% bandwidth reduction
**Impact:** Enables deployment in bandwidth-constrained environments (swarms, fleets, sensor networks)

### 4C Framework: Human Society-Inspired Security
**ID:** 2602.01942
**Key:** Four-dimensional risk organization
**Approach:** Core (integrity), Connection (trust), Cognition (reasoning), Compliance (governance)
**Impact:** Shifts from system-centric to behavioral integrity preservation

### COLT: Lightweight Multi-LLM Collaboration
**ID:** 2602.01935
**Key:** Shared MCTS reasoning substrate
**Approach:** Single shared MCTS tree enables cross-model value propagation; model-aware tree policy
**Results:** Small LLMs match large model performance with reduced cost
**Impact:** Avoids heavy external machinery; enables cost-effective multi-LLM collaboration

### SafePred: Predictive Guardrail via World Models
**ID:** 2602.01725
**Key:** Long-term risk prediction
**Approach:** World model predicts short- and long-term risks; step-level interventions + task-level re-planning
**Results:** 97.6% safety performance; 21.4% task utility improvement vs reactive baselines
**Impact:** Addresses delayed risk emergence in computer-using agents

### TABX: High-Throughput Sandbox Battle Simulator
**ID:** 2602.01665
**Key:** JAX-accelerated MARL environment
**Approach:** Reconfigurable multi-agent tasks with granular parameter control
**Impact:** Enables systematic investigation of trade-offs; scalable foundation

### Multi-Agent Teams Hold Experts Back
**ID:** 2602.01011
**Key:** Self-organizing team performance gap
**Approach:** Study of unconstrained coordination; conversational analysis of expertise leveraging
**Results:** LLM teams fail to match expert performance (up to 37.6% loss); integrative compromise vs proper weighting
**Impact:** Reveals gap in harnessing collective expertise; trade-off between alignment and utilization

### DeALOG: Decentralized Log-Mediated Reasoning
**ID:** 2602.00996
**Key:** Shared natural-language log memory
**Approach:** Specialized agents (Table, Context, Visual, Summarizing, Verification) communicate via log
**Results:** Competitive performance on FinQA, TAT-QA, CRT-QA, WikiTableQuestions, FeTaQA, MultiModalQA
**Impact:** Enables collaborative error detection without central control; scalable modularity

### SuperBrain: LLM-Assisted Swarm Intelligence
**ID:** 2509.00510
**Key:** Collective intelligence via co-evolution
**Approach:** Subclass Brain (user-LLM cognitive dyads) → GA-assisted evolution → Swarm Intelligence coordination → Superclass Brain
**Results:** Framework demonstrated on UAV scheduling and keyword filtering; scalable architecture
**Impact:** Conceptual foundation for explainable, ethically aligned collective AI; standardizes knowledge exchange

### PrivLLMSwarm: Privacy-Preserving LLM UAV Swarms
**ID:** 2512.06747
**Key:** MPC-encrypted LLM inference for swarms
**Approach:** Secure Multi-Party Computation for transformer components + RL-fined GPT command generator
**Results:** High semantic accuracy with low encrypted inference latency; superior privacy-utility balance
**Impact:** Practical foundation for secure LLM-enabled swarms in privacy-sensitive IoT (smart-city, emergency response)

### Human-Swarm Teaming: Disaster SAR
**ID:** 2511.04042
**Key:** Bridge intention-to-action gap
**Approach:** LLM-CRF system for intention comprehension, hierarchical task decomposition, mission planning with real-time feedback
**Results:** 64.2% faster task completion; 7% higher success rate; 42.9% reduced cognitive workload (NASA-TLX)
**Impact:** Enables proactive partner swarms reducing manual monitoring in high-stakes scenarios

### Graph-Based In-Context Planning
**ID:** 2510.24690
**Key:** Tool knowledge graph fusion with domain knowledge
**Approach:** DeepResearch-inspired tool graph + document/SOP knowledge graph with deep-sparse integration
**Results:** Effective tool interaction modeling and improved plan generation
**Impact:** Links structural tool dependencies with procedural knowledge for tool-augmented reasoning

### AOAD-MAT: Agent Order of Action Decisions
**ID:** 2510.13343
**Key:** Explicit action order in MARL
**Approach:** Transformer-based actor-critic with subtask for predicting next agent; PPO-based loss
**Results:** Outperforms MAT and baselines on StarCraft Multi-Agent Challenge and Multi-Agent MuJoCo
**Impact:** Demonstrates effectiveness of adjusting agent order in sequential decision-making

### Hanabi Conventions for Cooperation
**ID:** 2412.06333
**Key:** Augmented action space with conventions
**Approach:** Special cooperative actions spanning multiple time steps/agents based on human conventions
**Results:** Significant improvement on self-play and cross-play for various cooperator counts
**Impact:** Implicit knowledge sharing for partially observable multi-agent problems with limited communication

### Differential Voting: Axiomatic Aggregation
**ID:** 2601.18824
**Key:** Differentiable loss functions for diverse aggregation
**Approach:** Unifying framework constructing instance-wise losses corresponding to classical voting rules (BTL, Copeland, Kemeny)
**Results:** Formal analysis of calibration, gradient fields, and axiomatic properties for each loss
**Impact:** Makes preference aggregation explicit in RLHF; enables principled trade-offs between axioms and stability

### Beyond Majority Voting: Higher-Order Aggregation
**ID:** 2510.01499
**Key:** First + second-order information for LLM aggregation
**Approach:** Optimal Weight (OW) and Inverse Surprising Popularity (ISP) algorithms leveraging heterogeneity and correlation
**Results:** Consistently outperforms majority voting on synthetic datasets, UltraFeedback, MMLU, and ARMMAN healthcare
**Impact:** Addresses limitations of equal-weight voting for multi-agent LLM pipelines

### MASTER: Hierarchical Multi-Agent LLM Reasoning for Materials Discovery
**ID:** 2512.13930
**Key:** Multi-strategy coordination for autonomous scientific reasoning
**Approach:** MASTER framework with hierarchical multi-agent LLM reasoning: multimodal system translates natural language into DFT workflows, higher-level reasoning agents guide discovery through multiple strategies (single agent baseline, peer review, triage-ranking, triage-forms)
**Results:** Reasoning-driven exploration reduces required atomistic simulations by up to 90% relative to trial-and-error across CO adsorption on Cu-surface adatoms and M-N-C catalysts; reveals chemically grounded decisions
**Impact:** Accelerates materials discovery and marks new paradigm for autonomous scientific exploration via multi-agent collaboration

### ARCANE: Multi-Agent Framework for Interpretable Alignment
**ID:** 2512.06196
**Key:** Rubric-based reward models for long-horizon task alignment
**Approach:** Frames alignment as multi-agent collaboration problem; dynamic stakeholder preferences as natural-language rubrics (weighted sets of verifiable criteria); Group-Sequence Policy Optimization (GSPO) balances interpretability, faithfulness, and efficiency
**Results:** Evaluated on 219 labeled rubrics from GDPVal benchmark; produces compact, legible evaluations; enables configurable trade-offs (correctness vs. conciseness) without retraining
**Impact:** Promising path toward interpretable, test-time adaptive alignment for complex, long-horizon AI systems

### Agentic Reasoning Survey
**ID:** 2601.12538
**Key:** Comprehensive survey organizing agentic reasoning across three layers
**Approach:** Three-layer organization: (1) foundational agentic reasoning (single-agent capabilities in stable environments), (2) self-evolving agentic reasoning (feedback, memory, adaptation), (3) collective multi-agent reasoning (coordination, knowledge sharing, shared goals); distinguishes in-context reasoning (test-time interaction) from post-training reasoning
**Results:** Synthesizes representative frameworks across real-world applications and benchmarks in science, robotics, healthcare, autonomous research, mathematics
**Impact:** Unified roadmap bridging thought and action; outlines open challenges including personalization, long-horizon interaction, world modeling, scalable multi-agent training, governance

### SMAGDi: Socratic Multi-Agent Interaction Graph Distillation
**ID:** 2511.05528
**Key:** Interaction graph distillation for efficient reasoning
**Approach:** Distills five-agent Llama-based MAS debate dynamics into 6B Socratic decomposer-solver student; represents debate traces as directed interaction graphs with correctness labels and cross-agent edges; composite objective with language modeling, graph supervision, contrastive reasoning, embedding alignment
**Results:** Compresses 40B multi-agent system into 6B student while retaining 88% of accuracy on StrategyQA and MMLU; outperforms MAGDi, standard KD, fine-tuned baselines
**Impact:** Explicitly modeling interaction graphs enables small models to inherit multi-agent benefits while remaining efficient for real-world deployment

### AutoTool: Dynamic Tool Selection Integration for Agentic Reasoning
**ID:** 2512.13278
**Key:** Dynamic tool selection capability throughout reasoning trajectories
**Approach:** 200k dataset with explicit tool-selection rationales across 1,000+ tools and 100+ tasks; dual-phase optimization: (i) supervised and RL-based trajectory stabilization for coherent reasoning, (ii) KL-regularized Plackett-Luce ranking for consistent multi-step tool selection
**Results:** Trained Qwen3-8B and Qwen2.5-VL-7B; average gains: 6.4% in math & science reasoning, 4.5% in search-based QA, 7.7% in code generation, 6.9% in multimodal understanding; generalizes to unseen tools
**Impact:** Enables LLM agents to dynamically select from evolving toolsets during inference

### Agentic Lybic: Multi-Agent Execution with Tiered Orchestration
**ID:** 2509.11067
**Key:** FSM-based routing for adaptive desktop automation
**Approach:** Multi-agent system operating as finite-state machine with dynamic orchestration; Controller, Manager, three Workers (Technician for code, Operator for GUI, Analyst for decisions), Evaluator; FSM routing enables adaptive replanning and error recovery
**Results:** Achieves state-of-the-art 57.07% success rate on OSWorld benchmark in 50 steps; substantially outperforms existing methods
**Impact:** Principled multi-agent orchestration with continuous quality control provides superior reliability for generalized desktop automation

### Multi-Agent Orchestration Survey: Architectures, Protocols, Enterprise Adoption
**ID:** 2601.13671
**Key:** Unified architectural framework for orchestrated multi-agent systems
**Approach:** Integrates planning, policy enforcement, state management, and quality operations into coherent orchestration layer; defines Model Context Protocol (standardizes agent access to external tools) and Agent2Agent protocol (governs peer coordination, negotiation, delegation)
**Results:** Provides comprehensive treatments:bridging conceptual architectures with implementation-ready design principles for enterprise-scale AI ecosystems
**Impact:** Establishes interoperable communication substrate enabling scalable, auditable, policy-compliant reasoning across distributed agent collectives

### KBA Orchestration: Knowledge Base-Aware Privacy-Preserving Routing
**ID:** 2509.19599
**Key:** Privacy-preserving relevance signals from agent knowledge bases
**Approach:** Augments static descriptions with dynamic KB relevance signals; when static descriptions insufficient, orchestrator prompts subagents in parallel; each agent assesses task relevance against private KB, returns lightweight ACK without exposing data; signals populate shared semantic cache
**Results:** Significantly outperforms static description-driven methods in routing precision and overall system efficiency
**Impact:** Enables more accurate and adaptive task routing preserving agent autonomy and data confidentiality for large-scale systems

### Wonderful Team: Zero-Shot Physical Task Planning with Visual LLMs
**ID:** 2407.19094
**Key:** VLLM-based high-level physical task planning
**Approach:** Multi-agent Vision Large Language Model framework; provides image of robot's surroundings and task description, VLLM outputs sequence of actions; tightly integrated loop between perception, control, and planning
**Results:** 40% success rate improvement over NLaP on VimaBench; 30% improvement over Trajectory Generators on drawing/wiping tasks; 70% improvement on semantic reasoning tasks including environment rearrangement
**Impact:** Highlights rapid improvements of VLLMs; demonstrates VLLMs as viable option for some high-level robotic planning problems

### PIP-LLM: PDDL-Integer Programming with LLMs for Multi-Robot Coordination
**ID:** 2510.22784
**Key:** Separated team-level and robot-level planning for multi-robot coordination
**Approach:** PDDL-based team-level planning abstracts away robot assignment; IP-based robot-level planning explicitly optimizes travel costs, workload, respecting robot capabilities; translation into dependency graph guides robot-level planning with IP-based task allocation
**Results:** Improves plan success rate, reduces maximum and average travel costs, achieves better load balancing compared to baselines across diverse tasks
**Impact:** Avoids pitfalls of syntax-based decomposition; scales to larger teams through separation of planning from assignment

### LLM-Coordination: Benchmark for LLM Multi-Agent Coordination
**ID:** 2310.03903
**Key:** Pure coordination settings evaluating LLM coordination abilities
**Approach:** Two tasks: Agentic Coordination (LLMs act in pure coordination games), Coordination Question Answering (198 multiple-choice questions testing Environment Comprehension, ToM Reasoning, Joint Planning); Zero-Shot Coordination experiments test robustness to unseen partners
**Results:** LLM-Agents excel in environment-variable coordination but struggle with partner beliefs/intentions; significant room for improvement in ToM reasoning and joint planning; LLM agents exhibit robustness to unseen partners unlike RL methods
**Impact:** Indicates potential of LLMs as agents in pure coordination setups; underscores areas for improvement

### VirTLab: Interactive 2D Environments for Team Dynamics
**ID:** 2510.08242
**Key:** Customizable interactive simulations for studying human-AI team dynamics
**Approach:** System enabling users to design interactive, customizable 2D spatial environment simulations with LLM-based agents; build scenarios, assign roles, observe how agents coordinate, move, adapt over time; bridges team cognition behaviors with scalable agent-based modeling
**Results:** Aligns simulated outcomes with empirical evaluations and user study
**Impact:** Provides testbed for investigating how environments influence coordination, collaboration, emergent team behaviors; makes simulations accessible to technical and non-technical users

### The Language of Bargaining: Linguistic Effects in LLM Negotiations
**ID:** 2601.04387
**Key:** Language choice effects on multi-agent negotiation outcomes
**Approach:** Controlled multi-agent simulations across Ultimatum, Buy-Sell, and Resource Exchange games; test English vs. four Indic framings (Hindi, Punjabi, Gujarati, Marwadi) while holding game rules, model parameters, incentives constant
**Results:** Language choice can shift outcomes more strongly than changing models, reversing proposer advantages and reallocating surplus; effects are task-contingent: Indic languages reduce stability in distributive games yet induce richer exploration in integrative settings
**Impact:** Demonstrates that English-only evaluation yields incomplete conclusions; culturally-aware evaluation essential for fair deployment

### Less is More: Quality-Guided Distillation for Structured Reasoning
**ID:** 2504.16408
**Key:** Multi-agent framework with reverse-prompt induction for structured reasoning
**Approach:** Multi-agent framework for low-resource structural reasoning from only 24 labeled examples; reverse-prompt induction, retrieval-augmented reasoning synthesis via GPT-4o, dual-stage reward-guided filtering across three subtasks: question parsing, CoT parsing, step-level verification; all modules fine-tuned from Llama-3-8B-Instruct under unified LoRA+ setup
**Results:** Third-place winning approach in LLMSR@XLLM25; combines structure validation with reward filtering for few-shot and zero-shot prompts
**Impact:** Underscores value of controllable data distillation in enhancing structured inference under low-resource constraints

### MAEBE: Multi-Agent Emergent Behavior Evaluation Framework
**ID:** 2506.03053
**Key:** Framework for assessing emergent risks in multi-agent AI ensembles
**Approach:** Multi-Agent Emergent Behavior Evaluation using Greatest Good Benchmark and novel double-inversion question technique; evaluates moral preferences and emergent group dynamics including peer pressure and convergence behavior
**Results:** Ensembles exhibit phenomena like peer pressure influencing convergence even when guided by supervisor; moral reasoning not directly predictable from isolated agent behavior due to emergent group dynamics
**Impact:** Necessity of evaluating AI systems in interactive, multi-agent contexts; reveals novel emergent risks beyond single-agent safety

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
- **Research date:** Feb 2, 2026 (folder name reflects research date, not paper submission dates)
- **Source:** arXiv cs.AI category (papers from any date)
- **Scan status:** Entries 1-1400 of 1,516 total
- **Method:** WebFetch tool with markdown format
- **Focus:** Multi-agent/agentic systems with coordination, collaboration, or collective intelligence