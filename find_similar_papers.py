#!/usr/bin/env python3
"""
Find similar papers using TF-IDF and cosine similarity
"""

import json
import re
from collections import defaultdict
from pathlib import Path
import math


def load_database():
    with open("papers_database.json", "r", encoding="utf-8") as f:
        return json.load(f)


def preprocess_text(text):
    """Clean and tokenize text"""
    if not text:
        return []
    # Lowercase and remove special chars
    text = re.sub(r"[^\w\s]", " ", text.lower())
    # Split and filter short words
    words = [w for w in text.split() if len(w) > 2]
    return words


def compute_tf_idf(papers):
    """Compute TF-IDF vectors for all papers"""
    print("Computing TF-IDF vectors...")

    # Build document frequency
    doc_freq = defaultdict(int)
    paper_words = {}

    for pid, paper in papers.items():
        # Combine title, abstract, and focus
        text = f"{paper.get('name', '')} {paper.get('abstract', '')} {paper.get('focus', '')}"
        words = preprocess_text(text)
        paper_words[pid] = words

        # Count unique words in this document
        unique_words = set(words)
        for word in unique_words:
            doc_freq[word] += 1

    # Compute IDF
    N = len(papers)
    idf = {}
    for word, freq in doc_freq.items():
        idf[word] = math.log(N / (freq + 1)) + 1

    # Compute TF-IDF vectors
    vectors = {}
    for pid, words in paper_words.items():
        tf = defaultdict(int)
        for word in words:
            tf[word] += 1

        # Normalize TF
        total_words = len(words)
        if total_words > 0:
            tf = {word: count / total_words for word, count in tf.items()}

        # Compute TF-IDF
        tfidf = {word: tf[word] * idf.get(word, 0) for word in tf}
        vectors[pid] = tfidf

    return vectors


def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two vectors"""
    # Get all unique words
    all_words = set(vec1.keys()) | set(vec2.keys())

    # Compute dot product and magnitudes
    dot_product = sum(vec1.get(word, 0) * vec2.get(word, 0) for word in all_words)
    mag1 = math.sqrt(sum(v**2 for v in vec1.values()))
    mag2 = math.sqrt(sum(v**2 for v in vec2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0

    return dot_product / (mag1 * mag2)


def find_similar_papers(paper_id, vectors, papers, top_n=10):
    """Find papers similar to given paper"""
    if paper_id not in vectors:
        return []

    target_vec = vectors[paper_id]
    similarities = []

    for pid, vec in vectors.items():
        if pid != paper_id:
            sim = cosine_similarity(target_vec, vec)
            if sim > 0:
                similarities.append((pid, sim))

    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_n]


def generate_similarity_report():
    """Generate similarity report for all papers"""
    database = load_database()
    papers = database["papers"]

    print(f"Analyzing {len(papers)} papers for similarity...")
    print()

    # Compute TF-IDF vectors
    vectors = compute_tf_idf(papers)

    # Find similar papers for each paper
    similarity_data = {}

    for i, (pid, paper) in enumerate(papers.items(), 1):
        if i % 50 == 0:
            print(f"  Processed {i}/{len(papers)} papers...")

        similar = find_similar_papers(pid, vectors, papers, top_n=5)
        similarity_data[pid] = similar

    # Save similarity data
    with open("paper_similarities.json", "w", encoding="utf-8") as f:
        json.dump(similarity_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("SIMILARITY ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"  Papers analyzed: {len(papers)}")
    print(f"  Similarity data saved to: paper_similarities.json")

    # Show sample
    print()
    print("Sample similar papers:")
    sample_pids = list(papers.keys())[:3]
    for pid in sample_pids:
        paper = papers[pid]
        print(f"\n  {paper['name'][:60]}...")
        print(f"  Similar to:")
        for sim_pid, score in similarity_data[pid][:3]:
            sim_paper = papers[sim_pid]
            print(f"    - {sim_paper['name'][:50]}... (score: {score:.3f})")


def main():
    generate_similarity_report()


if __name__ == "__main__":
    main()
