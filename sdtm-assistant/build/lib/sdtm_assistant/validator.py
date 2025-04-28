
import openai
import json

def validate_mapping_entry_enhanced(mapping_entry, model_name="gpt-4o"):
    prompt = f"""
You are an SDTM 3.3 clinical data validator agent.

You are reviewing a draft mapping from a clinical CDMS source field to an SDTM target field.

Here is the draft mapping:
- Source Field: {mapping_entry['source_field']}
- Draft Target Field: {mapping_entry['target_field']}
- Draft Transformation Needed: {mapping_entry['transformation_needed']}
- Draft Reasoning: {mapping_entry['draft_reasoning']}

Your job is to validate it and produce a highly structured output.

IMPORTANT: Respond ONLY with a single pure JSON object.
"""

    try:
        response = openai.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        validated_output = response.choices[0].message.content.strip()
        validated_output = validated_output.replace("```json", "").replace("```", "").strip()
        validated_json = json.loads(validated_output)
        return validated_json

    except Exception as e:
        print(f"Validation failed: {e}")
        return None
