import json
import pickle


def save_to_text_file(data, output_file: str = "output/data.txt"):
    with open(output_file, "w") as fp:
        fp.write(str(data))


def save_to_json_file(data, output_file: str = "output/items.json"):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_to_pickle(data, output_file: str = "output/outfile"):
    with open(output_file, "wb") as fp:
        pickle.dump(data, fp)
