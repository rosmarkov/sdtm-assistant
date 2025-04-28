import typer
import json
import csv
from pathlib import Path
from .validator import validate_mapping_entry_enhanced

app = typer.Typer()

def load_input_file(input_file, file_format):
    with open(input_file, "r") as f:
        if file_format == "jsonl":
            return [json.loads(line) for line in f if line.strip()]
        else:
            return json.load(f)

@app.command()
def validate(
    input: Path = typer.Option(..., "--input", help="Path to the draft mapping input file"),
    output: Path = typer.Option(..., "--output", help="Path to save the validated output"),
    model: str = typer.Option(..., "--model", help="Model to use (e.g., gpt-4o)"),
    format: str = typer.Option("jsonl", "--format", help="Input file format (json or jsonl)"),
    verbose: bool = typer.Option(False, "--verbose", help="Print validation progress"),
):
    """Validate draft SDTM mappings."""
    
    mappings = load_input_file(input, format)

    validated = []

    for idx, entry in enumerate(mappings):
        validated_entry = validate_mapping_entry_enhanced(entry, model)
        validated.append(validated_entry)

        if verbose:
            typer.echo(f"Validated {idx+1}/{len(mappings)}")

    # Save output based on format
    if format == "jsonl":
        with open(output, "w") as f_out:
            for entry in validated:
                f_out.write(json.dumps(entry) + "\n")
    elif format == "json":
        with open(output, "w") as f_out:
            json.dump(validated, f_out, indent=2)
    elif format == "csv":
        if validated:
            keys = validated[0].keys()
            with open(output, "w", newline="") as f_out:
                writer = csv.DictWriter(f_out, fieldnames=keys)
                writer.writeheader()
                writer.writerows(validated)
        else:
            typer.secho("Warning: No validated entries to save in CSV.", fg=typer.colors.YELLOW)

    typer.secho(f"Validation complete. {len(validated)} fields validated. Saved to {output}", fg=typer.colors.GREEN)

@app.command()
def version():
    """Show the CLI version."""
    typer.echo("sdtm-assistant v0.1.0")

if __name__ == "__main__":
    app()