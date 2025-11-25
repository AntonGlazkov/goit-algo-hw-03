import os
import shutil
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    parser.add_argument("dest_dir", nargs="?", default="dist")
    return parser.parse_args()


def copy_files_recursive(source_dir, dest_dir):
    try:
        items = os.listdir(source_dir)
    except (PermissionError, FileNotFoundError, OSError) as e:
        print(f"Помилка доступу до директорії '{source_dir}': {e}")
        return

    for item in items:
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            copy_files_recursive(item_path, dest_dir)
        elif os.path.isfile(item_path):
            copy_file_to_sorted_dir(item_path, dest_dir)


def copy_file_to_sorted_dir(file_path, dest_root):
    _, ext = os.path.splitext(file_path)
    if ext:
        ext_name = ext[1:].lower()
    else:
        ext_name = "no_extension"

    target_dir = os.path.join(dest_root, ext_name)

    try:
        os.makedirs(target_dir, exist_ok=True)
    except OSError as e:
        print(f"Помилка створення директорії '{target_dir}': {e}")
        return

    dest_path = os.path.join(target_dir, os.path.basename(file_path))

    try:
        shutil.copy2(file_path, dest_path)
    except (PermissionError, FileNotFoundError, OSError) as e:
        print(f"Помилка копіювання файлу '{file_path}' у '{dest_path}': {e}")


def main():
    args = parse_args()
    copy_files_recursive(args.source_dir, args.dest_dir)


if __name__ == "__main__":
    main()
