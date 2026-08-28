# Tools and Libraries

## 1. Crossref REST API

A primary source for DOI-linked scholarly metadata. Useful for resolving a DOI, comparing title/author/venue fields, and detecting identifier mismatches. The public REST API requires no signup; a polite request with contact information is recommended for responsible use.

[Official documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)

## 2. OpenAlex

An open scholarly knowledge graph covering works, authors, sources, institutions, topics, and related entities. Particularly useful for title/author searches when a DOI is missing or a generated citation is noisy.

[API reference](https://help.openalex.org/api/)

## 3. Semantic Scholar API

Provides programmatic access to scholarly-paper metadata, citation graphs, authors, abstracts, and related research. It is useful for candidate retrieval and citation-network exploration.

[Official API documentation](https://api.semanticscholar.org/api-docs/)

## 4. GROBID

A machine-learning toolkit for extracting structured bibliographic information, references, and document structure from scientific PDFs. Useful for converting papers into machine-readable evidence and citation records before downstream verification.

[Official repository](https://github.com/grobidOrg/grobid)

## 5. Zotero

A reference-management platform with a versioned Web API. Useful for maintaining a verified local bibliography and exporting structured citation metadata rather than manually copying reference strings.

[Web API documentation](https://www.zotero.org/support/dev/web_api)

## 6. DOI System / DOI Handbook

The DOI Handbook documents identifier syntax, resolution, metadata, and interoperability. It is useful when designing reliable identifier-based verification workflows.

[DOI Handbook](https://www.doi.org/doi-handbook/html/)

## 7. Pyserini

A reproducible information-retrieval toolkit supporting sparse, dense, and hybrid retrieval. It is useful for evidence retrieval and candidate-paper ranking in citation-verification pipelines.

[Official repository](https://github.com/castorini/pyserini)

## 8. scispaCy

Scientific/biomedical NLP pipelines built on spaCy. Useful for sentence segmentation, entity extraction, and domain-specific preprocessing in scientific-text verification systems.

[Official repository](https://github.com/allenai/scispacy)
