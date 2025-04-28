
import typer
import json
import csv
from pathlib import Path
from .validator import validate_mapping_entry_enhanced

app = typer.Typer()

@app.command()
def validate(
    input: Path = typer.Option(..., help="Input JSON file with mappings."),
    output: Path = typer.Option(..., help="Output file path."),
    model: str = typer.Option("gpt-4o", help="OpenAI model name."),
    format: str = typer.Option("json", help="Output format: json or csv."),
    verbose: bool = typer.Option(False, help="Print progress to console."),
):
    """Validate draft SDTM mappings."""
    with open(input, "r") as f:
        mappings = json.load(f)

    validated = []
    for idx, entry in enumerate(mappings):
        result = validate_mapping_entry_enhanced(entry, model)
        if result:
            validated.append(result)
            if verbose:
                typer.echo(f"✅ Validated {idx+1}/{len(mappings)}: {entry['source_field']}")
        else:
            typer.echo(f"⚠️  Failed to validate {entry.get('source_field', 'UNKNOWN')}")

    if format == "json":
        with open(output, "w") as f:
            json.dump(validated, f, indent=2)
    elif format == "csv":
        if validated:
            keys = validated[0].keys()
            with open(output, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(validated)

    typer.secho(f"✅ Validation complete. {len(validated)} fields validated. Saved to {output}", fg=typer.colors.GREEN)

@app.command()
def version():
    """Show the CLI version."""
    typer.echo("sdtm-assistant v0.1.0")

if __name__ == "__main__":
    app()
