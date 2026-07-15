from pathlib import Path


def load_prompt(filename: str) -> str:

    current_file = Path(__file__)

    project_root = current_file.parents[3]

    prompt_path = (
        project_root
        / "prompts"
        / filename
    )

    return prompt_path.read_text(
        encoding="utf-8"
    )