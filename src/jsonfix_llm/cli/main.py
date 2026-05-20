import sys

import typer
from typer.core import TyperGroup

from jsonfix_llm import extract_code, repair_json


class NaturalOrderGroup(TyperGroup):
    def parse_args(self, ctx, args):
        if args and args[0] in self.commands:
            return super().parse_args(ctx, args)
        return super().parse_args(ctx, ["repair", *args])


app = typer.Typer(cls=NaturalOrderGroup)


@app.command()
def repair(
    file: str = typer.Argument(None, help="JSON file to repair (stdin if omitted)"),
    output: str = typer.Option(None, "-o", "--output", help="Write output to file"),
    stats: bool = typer.Option(False, "--stats", help="Show repair statistics"),
):
    if file:
        with open(file, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    result = repair_json(text, rich=stats)
    if stats:
        typer.echo(result.fixed)
        typer.echo(f"// Repaired: {result.was_repaired}", err=True)
        fixes_summary = ", ".join(result.fixes) if result.fixes else "none"
        typer.echo(f"// Fixes applied: {fixes_summary}", err=True)
        typer.echo(f"// Errors: {result.error_count}", err=True)
        if result.errors:
            for err in result.errors:
                typer.echo(f"//   - {err}", err=True)
    else:
        output_text = result if isinstance(result, str) else result.fixed
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(output_text)
        else:
            typer.echo(output_text)


@app.command()
def extract(
    file: str = typer.Argument(None, help="File to extract from (stdin if omitted)"),
    language: str = typer.Option("python", "--language", "-l",
                                  help="Programming language to extract"),
    output: str = typer.Option(None, "-o", "--output", help="Write output to file"),
    all_blocks: bool = typer.Option(False, "--all", help="Extract all matching blocks"),
):
    if file:
        with open(file, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    result = extract_code(text, language=language, all=all_blocks)
    output_text = "\n---\n".join(result) if isinstance(result, list) else result

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(output_text)
    else:
        typer.echo(output_text)


if __name__ == "__main__":  # pragma: no cover
    app()
