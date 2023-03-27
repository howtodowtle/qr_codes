import argparse
from pathlib import Path


def split_string(large_string, name, group_name, output_folder, delimiter="--"):
    substrings = large_string.split(delimiter)
    substrings = substrings[1:]  # Remove the first empty substring
    for i, substring in enumerate(substrings):
        file_name = Path(output_folder) / f"{name}_{group_name}_{i + 1}.txt"
        with open(file_name, "w") as f:
            f.write(substring.strip())


def process_folder(folder, name, delimiter):
    large_txt_file = (folder.parent / "combined") / f"{folder.stem}.txt"
    if not large_txt_file.exists():
        print(f"Could not find {large_txt_file}")
        return
    with open(large_txt_file, "r") as f:
        large_string = f.read()
    split_string(large_string=large_string, name=name, group_name=folder.stem, output_folder=folder, delimiter=delimiter)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", "-f", type=str, default="data", help="Parent folder to process")
    parser.add_argument("--name", "-n", type=str, default="Lesepur_Berchtesgaden_QR_Code", help="Name")
    parser.add_argument(
        "--delimiter",
        "-d",
        type=str,
        required=False,
        default="--",
        help="Delimiter",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    parent_folder = Path(args.folder)
    name = args.name
    delimiter = args.delimiter

    folders = [x for x in parent_folder.iterdir() if x.is_dir() and not "combined" in x.name]

    for folder in folders:
        process_folder(folder=folder, name=name, delimiter=delimiter)


if __name__ == "__main__":
    main()
