#
# Sort your downloads folder!
# 1) skips any existing folders
# 2) defaults to 'safe mode' - no files will move - only shows what "would move"
# 3) run with -h for a list of options
#

devName = "ErnieJohnson.ca"
appVersion = "1.0.0"
appName = "MoveThis!"


import os
import shutil
import argparse
import sys

debugOutput = False;


# Define your Downloads folder path and target folder paths
download_folder = "/Users/erniejohnson/Downloads"
unsorted_folder = "/Users/erniejohnson/Downloads/UnknownFiles"
target_folders = {
    ".pdf": "/Users/erniejohnson/Downloads/Documents",
    ".jpg": "/Users/erniejohnson/Downloads/Images",
    ".png": "/Users/erniejohnson/Downloads/Images",
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
    skipped_folders = 0;

    for root, _, files in os.walk(download_folder):
        if debugOutput:
          print ("ROOT:",root)

        if root != download_folder:
            skipped_folders +=1 # TODO this counter isn't working properly
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
            else:
                print(f"MOVING {source_path} TO {unsorted_folder}") # TODO - build this section out

    return move_counts, skipped_folders


def colorize_text(text,color):
  RED_COLOR = "\033[91m"
  BLUE_COLOR = "\033[36m"
  RESET_COLOR = "\033[0m"

  if color =='red':
    COLOR_UNIT = RED_COLOR
  elif color == 'blue':
    COLOR_UNIT = BLUE_COLOR

  return f"{COLOR_UNIT}{text}{RESET_COLOR}"

#
# main application:

if sys.platform != 'darwin':
    print(colorize_text("This script is intended to run on macOS only.","red"))
    sys.exit(1)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Sort files in the Downloads folder.")
  parser.add_argument("-move", action="store_true", help="Move the files (default is to only show what will be moved)")
  parser.add_argument("-about", action="store_true", help="About the app, version and developer info.")
  parser.add_argument("-debug", action="store_true", help="Force debut output to ON.")

  args = parser.parse_args()

  if args.about:
    appNameColored = colorize_text(appName,'blue')
    print (f"{appNameColored} - v{appVersion}")
    print (f"written by: {devName}")
    exit()

  if args.debug:
    debugOutput = args.debug

  print("Sorting files in Downloads folder...")
  move_counts, skipped_files = sort_files(move_files=args.move)

  print("")
  if args.move:
    print("File sorting complete (files have been moved).")
  else:
    print("File sorting preview (no files have been moved).")

  print("\nTarget Folder\t\t\t\tFileCount")
  for target_folder, count in move_counts.items():
    counter_text = colorize_text(count,'red')
    print(f"{target_folder}\t{counter_text}")

  print(f"\nSkipped files: {skipped_files}")