import os
import shutil
import argparse

debugOutput = True;

# Define your Downloads folder path and target folder paths
download_folder = "/Users/erniejohnson/Downloads"
target_folders = {
    ".pdf": "/Users/erniejohnson/Downloads/Documents",
    ".jpg": "/Users/erniejohnson/Downloads/Images",
    ".mp4": "/Users/erniejohnson/Downloads/Videos",
    ".zip": "/Users/erniejohnson/Downloads/ZipFiles",
    ".dmg": "/Users/erniejohnson/Downloads/AppFiles",
}

def ensure_folder_exists(folder_path):
  if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def should_move(source_path, target_path):
  return not os.path.exists(target_path)

def sort_files(move_files=False):
    move_counts = {target: 0 for target in target_folders.values()}

    for root, _, files in os.walk(download_folder):
        if debugOutput:
          print ("ROOT:",root)
          
        if root != download_folder:
            continue  # Skip subdirectories

        for filename in files:
            source_path = os.path.join(root, filename)
            _, extension = os.path.splitext(filename)

            # Check if a target folder exists for the extension
            target_folder = target_folders.get(extension, None)

            if target_folder:
                ensure_folder_exists(target_folder)  # Create the target folder if it doesn't exist
                target_path = os.path.join(target_folder, filename)

                if should_move(source_path, target_path) and move_files:
                    shutil.move(source_path, target_path)
                    move_counts[target_folder] += 1
                else:
                    move_counts[target_folder] += 1

                if move_files:
                    print(f"Moved {source_path} to {target_path}")
                else:
                    print(f"Will move {source_path} to {target_path}")

    return move_counts

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sort files in the Downloads folder.")
  parser.add_argument("-move", action="store_true", help="Move the files (default is to show what will be moved)")

  args = parser.parse_args()

  print("Sorting files in Downloads folder...")
  move_counts = sort_files(move_files=args.move)

  print("")
  if args.move:
    print("File sorting complete (files have been moved).")
  else:
    print("File sorting preview (no files have been moved).")

  print("\nTarget Folder\t\t\t\tFileCount")
  for target_folder, count in move_counts.items():
    print(f"{target_folder}\t{count}")