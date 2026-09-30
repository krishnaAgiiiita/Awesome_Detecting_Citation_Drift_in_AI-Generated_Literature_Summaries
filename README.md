# Awesome Citation Drift in AI-Generated Literature

A curated research resource on **detecting citation drift in AI-generated literature summaries**. It connects an AI-assisted research paper and its citation-integrity audit with verified scholarly literature, datasets, tools, open-source implementations, and learning resources. The repository emphasizes the distinction between **bibliographic validity** (does the cited work exist and do its metadata match?) and **claim-level support** (does the source actually support the generated statement?).

> **Student:** Krishna Agarwal  
> **Roll No.:** MSE2026008  
> **Programme:** M.Tech IT (Specialization in SE & A)  
> **Topic ID:** T17  
> **Assigned topic:** Detecting Citation Drift in AI-Generated Literature  
> **AI environment for original paper:** Consensus, Deep Research mode, 21 August 2026

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Curated Research Papers](#curated-research-papers)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Verification Method](#verification-method)
- [Repository Structure](#repository-structure)
- [License and Copyright](#license-and-copyright)

## Overview

Citation drift describes the ways an AI-generated literature summary can separate from its evidence base. It is broader than a fabricated reference: a real publication may be cited with mutated metadata, attached to a claim it does not support, or summarized beyond the scope of its findings. The problem is especially important for large language models (LLMs) used in literature review, evidence synthesis, related-work drafting, and research discovery, where fluent prose can make incorrect attribution appear authoritative.

A useful detection pipeline therefore treats citation integrity as a **multi-stage information-retrieval and verification problem**. First, a citation must be resolved to a real scholarly work and its bibliographic fields checked. Next, relevant evidence must be retrieved from the source. The generated statement should then be decomposed into atomic claims and aligned with evidence spans. Finally, a support judgment determines whether the retrieved evidence entails, contradicts, or fails to substantiate the claim. Retrieval-augmented generation (RAG), citation-attribution benchmarks, scientific claim-verification datasets, and automated bibliographic checking all contribute to this pipeline, but none eliminates the need for careful validation.

This repository collects resources across these layers. It also preserves the original AI-assisted paper and the corresponding citation-integrity audit as the experimental artifacts for Lab 1. The curated literature is organized around foundational citation distortion, LLM factuality and citation generation, attribution and verification, retrieval-grounded methods, and evaluation benchmarks.

## AI-Assisted Research Paper

### *Detecting Citation Drift in AI-Generated Literature Summaries*

The original AI-assisted paper surveys citation drift as a layered problem involving reference existence, metadata integrity, evidence retrieval, claim attribution, and support judgment. It reviews retrieval-augmented and citation-aware systems and identifies fine-grained, domain-robust evaluation as a major open direction.

**Artifact:** [`AI_Assisted_Research_Paper.pdf`](paper/Detecting_Citation_Drift_in_AI_Generated_Literature_Summaries.pdf)

The paper contains approximately 4,701 words, 10 major sections, and 60 references as recorded in the accompanying audit report.

## Citation Integrity Audit

The accompanying audit preserves the systematic sampling and verification exercise performed on the AI-generated bibliography. Ten references were selected using the prescribed sampling rule: the first three, last three, and four distributed through the middle of the 60-reference bibliography. The audit classified seven as fully verified (A), three as wrong/incomplete metadata (B), and one as a Frankenstein-style citation (C) in its detailed classification table; the report records an 85% authenticity score and 80% prediction accuracy.

**Artifact:** [`Citation_Integrity_Audit.pdf`](citation-audit/Citation_Integrity_Audit.pdf)

> The audit is an experimental record. The curated research collection below is a separate set of resources selected for this repository and should not be interpreted as a claim that every reference in the original AI-generated bibliography was verified.

## Curated Research Papers

See [`references/references.md`](references/references.md) for the full collection. It contains more than the required 20 scholarly papers and organizes them into meaningful research categories.

### Categories

- **Foundations and citation distortion** — classic work on miscitation, citation bias, and propagation.
- **LLM citation reliability and factuality** — empirical audits of generated references and summaries.
- **Citation attribution and verification** — claim-to-source alignment, citation integrity, and hallucination detection.
- **Retrieval-grounded generation** — RAG and self-reflective grounding methods relevant to reducing drift.
- **Benchmarks and evaluation** — datasets and metrics for citation generation, attribution, and factuality.

## Datasets

See [`datasets/datasets.md`](datasets/datasets.md). Recommended starting points include **SciFact**, **CiteME**, **CiteWorth**, **CL-SciSumm**, **S2ORC**, and **SciDocs**. These cover scientific claim verification, citation attribution, cite-worthiness, scientific summarization, large-scale scientific corpora, and scholarly-document representation/evaluation.

## Tools and Libraries

See [`tools/tools.md`](tools/tools.md) for scholarly metadata and document-processing infrastructure including Crossref, OpenAlex, Semantic Scholar, GROBID, Zotero, and DOI resources.

## GitHub Implementations

See [`implementations/github-repositories.md`](implementations/github-repositories.md). The collection includes research implementations such as Citation-Integrity, CiteGuard, CiteAudit, ALCE, Self-RAG, Long-Form Factuality, SciFact, and S2ORC.

## Tutorials and Learning Resources

See [`tutorials/tutorials.md`](tutorials/tutorials.md) for authoritative documentation and learning material covering DOI resolution, Crossref/OpenAlex metadata retrieval, Semantic Scholar data access, GROBID document parsing, ACL bibliographic exports, and scientific claim-verification resources.

## Verification Method

Resources were curated using the following procedure:

1. Prefer publisher, DOI registry, conference proceedings, institutional, or official project pages.
2. Match **title, authors, year, venue, and identifier** before adding a scholarly paper.
3. For software, prefer the official project repository or documentation.
4. For datasets, record provenance, intended task, and license where available.
5. Link to papers rather than redistributing copyrighted PDFs.
6. Treat AI-generated references as candidate leads, never as verification evidence.

This workflow follows the course instruction sheet's requirement for independent verification and its warning against blindly pasting AI-generated resource lists.

## Repository Structure

```text
awesome-citation-drift/
├── README.md
├── paper/
│   └── AI_Assisted_Research_Paper.pdf
├── citation-audit/
│   └── Citation_Integrity_Audit.pdf
├── references/
│   └── references.md
├── datasets/
│   └── datasets.md
├── tools/
│   └── tools.md
├── implementations/
│   └── github-repositories.md
├── tutorials/
│   └── tutorials.md
└── LICENSE
```

## License and Copyright

Original repository documentation is licensed under **CC BY 4.0**. The included AI-assisted paper and citation-audit report are the student's own assignment artifacts. Third-party papers, datasets, software, trademarks, and linked resources remain subject to their respective licenses and copyright terms. This repository does **not** redistribute third-party research-paper PDFs.
