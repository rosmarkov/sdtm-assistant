# sdtm-assistant
Agentic workflow for SDTM-compliant dataset generation

## Solution overview
The agentic workflow consists of the following components:
*	Study Data Generator: Utilizes LLMs to create synthetic clinical datasets, simulating real-world scenarios for testing the mapping process.
*	Study Data Explorer: Analyzes generated datasets to identify and summarize source fields, preparing them for mapping.
*	SDTM Auto-Mapping: Applies LLMs to suggest draft mappings from source fields to SDTM domains and variables, incorporating reasoning for each suggestion.
*	SDTM Validator: Employs chain-of-thought prompting with LLMs to validate draft mappings, ensuring compliance with controlled terminologies and identifying potential issues.
*	Command-Line Interface (CLI): Provides a user-friendly interface to execute the workflow, allowing for input of draft mappings and output of validated results in various formats (JSON, CSV).

