from pathlib import Path


def load_prompt(filename: str) -> str:

    current_file = Path(__file__)

    project_root = current_file.parents[3]

    prompt_path = (
        project_root
        / "prompts"
        / filename
    )

    # 如果沒有副檔名，自動補 .md
    if prompt_path.suffix == "":
        prompt_path = prompt_path.with_suffix(".md")

    return prompt_path.read_text(
        encoding="utf-8"
    )