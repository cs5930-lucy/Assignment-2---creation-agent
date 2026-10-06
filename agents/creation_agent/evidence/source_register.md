# RAG creation source register

Checked in this ChatGPT/Codex session on 2026-10-06. Authoritative source pages and relevant RAG method sections were inspected. This is assistant verification, not a claim that Lucy personally read all papers.

## S1: Vaswani et al., Attention Is All You Need

Date: 2017-06-12. URL: https://arxiv.org/abs/1706.03762

Supports: Transformer architecture supports parallelizable sequence modelling.

Claim limit: Architecture predecessor; not evidence about RAG value or Chinese/English product accuracy.

## S2: Mike Lewis et al., BART: Denoising Sequence-to-Sequence Pre-training

Date: 2019-10-29. URL: https://arxiv.org/abs/1910.13461

Supports: BART introduced denoising pretraining for sequence-to-sequence generation.

Claim limit: Generation predecessor; its benchmark results do not establish this application.

## S3: Karpukhin et al., Dense Passage Retrieval for Open-Domain Question Answering

Date: 2020-04-10. URL: https://arxiv.org/abs/2004.04906

Supports: DPR used learned dense representations to retrieve passages.

Claim limit: Retrieval predecessor; relevance is not document authority or approval.

## S4: Patrick Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

Date: 2020-05-22. URL: https://arxiv.org/abs/2005.11401

Supports: RAG combined a pretrained generator with external retrieval for knowledge-intensive generation.

Claim limit: Methods sections 2.2 and 2.3 identify DPR and BART: https://arxiv.org/html/2005.11401v4 . Original fine-tuned RAG differs from a modern retrieve-then-prompt workflow. This is a milestone, not the origin of all retrieval-assisted NLP.

## S5: Liu et al., Lost in the Middle: How Language Models Use Long Contexts

Date: 2023-07-06. URL: https://arxiv.org/abs/2307.03172

Supports: Tested models were sensitive to the position of relevant information in long contexts.

Claim limit: Contrary evidence: supplying information does not ensure it is used correctly. Does not establish failure rates of all present-day models.

## S6: Amazon Web Services, Amazon Bedrock Knowledge Bases

Date: Living documentation; retrieved 2026-10-06. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html

Supports: Provider documentation describes retrieval and generation from proprietary sources, including citations.

Claim limit: Evidence of packaged provider support, not independent reliability, adoption prevalence, ROI, or vendor selection advice.

## Interpretation and gaps

The convergence explanation is analytical synthesis. Pretrained components and reusable document indexes lowered the need to create every component from scratch, a technical/economic inference from S2-S4. Demand for revisable, inspectable knowledge is documented in S4. Pressure to reuse product knowledge in bilingual marketing is a scenario assumption. No source establishes textile market demand, cost savings, bilingual accuracy or company readiness. No actual product corpus is supplied.
