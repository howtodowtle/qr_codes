import argparse
from pathlib import Path

import qrcode


def get_link(file):
    return f"https://raw.githubusercontent.com/howtodowtle/qr_codes/main/data/{file.parent.name}/{file.name}"


def create_qr_code(file, output_folder):
    data = get_link(file=file)
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = (Path(output_folder) / file.parent.name) / f"{file.stem}.png"
    img.save(filename)


def process_folder(folder, output_folder):
    files = [x for x in folder.iterdir() if x.is_file() and x.suffix == ".txt"]
    for file in files:
        create_qr_code(file=file, output_folder=output_folder)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", "-f", type=str, default="data", help="Parent folder to process")
    parser.add_argument("--output_folder", "-o", type=str, default="codes", help="Output folder")
    return parser.parse_args()


def main():
    args = parse_args()
    parent_folder = Path(args.folder)
    output_folder = Path(args.output_folder)

    folders = [x for x in parent_folder.iterdir() if x.is_dir() and not "combined" in x.name]

    for folder in folders:
        process_folder(folder=folder, output_folder=output_folder)


if __name__ == "__main__":
    main()
