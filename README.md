# sdtm-assistant: Agentic workflow for Study Data Tabulation Model (SDTM)-compliant dataset generation

The project demonstrates an agentic workflow automating dataset conversion using Study Data Tabulation Model (SDTM). SDTM is used to report clinical studies results to the FDA in the US. This is a challenging task for biostatistians as it's effort-intensive, cognitively demanding, and requires full verification of accuracy and completeness of the SDTM dataset for regulatory compliance. In many cases this activity leads to fatigue and burnout.

The solution designs a modular, agentic system where autonomous agents powered by large language models (LLMs) perform discrete SDTM mapping tasks with human oversight. The methodology combines synthetic data generation, exploration, mapping draft generation, validation using reasoning chains, and operationalization through a Command-Line Interface (CLI).

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
