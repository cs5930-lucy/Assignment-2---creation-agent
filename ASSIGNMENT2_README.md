# Lucy Shen | Assignment 2 Creation Agent

Case: RAG for bilingual textile product-content drafting in a hypothetical manufacturer. All organizational details are explicitly assumed. This repository implements the course's analytical Creation Agent using ChatGPT as runtime; it does not implement the proposed RAG content application.

The original frozen core and tools are unchanged. Student files are in agents/creation_agent. The baseline, revision, cases, built packets, JSON outputs, sources and records are preserved. Working agent version: 0.2-student.

## Run locally from the repository root

```bash
python tools/build_prompt.py --agent agents/creation_agent --case agents/creation_agent/cases/primary.json --out agents/creation_agent/prompts/primary_new_prompt.txt
python tools/validate_response.py agents/creation_agent/responses/primary_response_v0_2.json
python tools/check_frozen_core.py
python agents/creation_agent/check_submission.py
```

For a new run, submit the generated packet to ChatGPT and save its returned JSON as a new response file. Do not replace the baseline. Refresh the source snapshot for new current claims. No OpenAI API key is required.

## Integration

Preserve all 11 common input fields and 13 output fields with their types. Keep all three finding levels distinct. Pass claim/date/source/limit evidence and uncertainty to the orchestrator. Recommendations are creation-lens implications, never production authorization. Hand off diffusion, adoption/readiness, implementation, security, costs, compliance and risk acceptance. No independent reliability evaluation is available.

## Pending student actions

Review and accept or revise the hypothetical case, judgment and reflection. Publish this working repository to your own GitHub repository and enter the real URL in the Agent Record. Local branch and commit evidence are provided in the submission VERSION_RECORD.txt. No GitHub repository URL is invented. The provided Git bundle preserves the local commits for import.
