import json


def save_to_text_file(data, output_file: str = "output/data.txt"):
    with open(output_file, "w") as fp:
        fp.write(str(data))


def save_to_json_file(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
