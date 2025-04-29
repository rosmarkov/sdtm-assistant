# sdtm-assistant: Agentic workflow for Study Data Tabulation Model (SDTM)-compliant dataset generation

**sdtm-assistant** is a prototype system demonstrating how agentic workflows powered by large language models (LLMs) can automate the conversion of clinical trial data into the **Study Data Tabulation Model (SDTM)** format.

SDTM is the regulatory standard required for clinical study submissions to agencies like the FDA. Traditionally, SDTM mapping is a manual, error-prone, and cognitively demanding task for biostatisticians, often contributing to fatigue and project delays.
This project explores how an agent-based AI architecture can **reduce manual effort, increase traceability, and maintain regulatory compliance** by shifting the human role from executor to reviewer.

## What This Project Covers
* **Synthetic clinical dataset generation**
* **Dataset exploration and feature profiling**
* **LLM-driven draft SDTM mapping**
* **Chain-of-thought (CoT) validation for mapping quality**
* **Command-Line Interface (CLI) for operational use**
* **Full audit trace of decisions for regulatory traceability**

Rather than replacing human validation, the system augments biostatisticians with draft mappings, structured reasoning outputs, and validation recommendations.

## Key techniques
Key techniques include: 
*	**Zero-shot prompting** with extended instruction sets to guide LLMs toward structured, machine- and human-readable outputs.
*	**Chain-of-thought (CoT)** prompting to encourage step-by-step validation reasoning.
*	**Human-in-the-loop** review stages to reduce hallucination risks and maintain clinical compliance.
*	**Extensible modular architecture**, allowing for independent improvement of system components.

## Solution overview
The agentic workflow consists of the following components:
*	**Study Data Generator**: Utilizes LLMs to create synthetic clinical datasets, simulating real-world scenarios for testing the mapping process.
*	**Study Data Explorer**: Analyzes generated datasets to identify and summarize source fields, preparing them for mapping.
*	**SDTM Auto-Mapping**: Applies LLMs to suggest draft mappings from source fields to SDTM domains and variables, incorporating reasoning for each suggestion.
*	**SDTM Validator**: Employs chain-of-thought prompting with LLMs to validate draft mappings, ensuring compliance with controlled terminologies and identifying potential issues.
*	**Command-Line Interface (CLI)**: Provides a user-friendly interface to execute the workflow, allowing for input of draft mappings and output of validated results in various formats (JSON, CSV).

The following table provides a brief overview of the method and technology used with each component. 

|Component              |Method                               |	Technology      |
|-----------------------|-------------------------------------|-----------------|
|Study Data Generator	  |Prompted synthetic record generation	|4o-mini, Python  |
|Study Explorer	        |Basic statistical profiling	        |Pandas           |
|SDTM Auto-Mapping	    |Zero-shot LLM prompting	            |gpt-4o-mini      |
|SDTM Validator	        |Chain-of-thought reasoning	          |gpt-4o           |
|Command-Line Interface (CLI)	| Typer CLI framework            |Typer, Python   |

## Why This Matters
* **Flexibility**: Handles diverse Electronic Data Capture (EDC) inputs — crucial in the U.S., where no unified electronic health record (EHR) system exists.
* **Transparency**: Every mapping decision is documented with structured reasoning for full auditability.
* **Cognitive relief**: Reduces cognitive load by offloading repetitive tasks to AI agents while maintaining oversight.


