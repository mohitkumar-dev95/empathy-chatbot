import os
import tarfile
import urllib.request
import pandas as pd

def main():
    url = "https://dl.fbaipublicfiles.com/parlai/empatheticdialogues/empatheticdialogues.tar.gz"
    tar_path = "empatheticdialogues.tar.gz"
    extract_dir = "empatheticdialogues"

    if not os.path.exists(extract_dir): # or check for train.csv
        print("Downloading dataset...")
        try:
            urllib.request.urlretrieve(url, tar_path)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading: {e}")
            return

        print("Extracting dataset...")
        try:
            with tarfile.open(tar_path, "r:gz") as tar:
                tar.extractall()
            print("Extraction complete.")
        except Exception as e:
            print(f"Error extracting: {e}")
            return
    else:
        print("Dataset directory already exists.")

    # Locate train.csv
    csv_path = None
    possible_paths = [
        "empatheticdialogues/train.csv",
        "train.csv"
    ]
    
    for p in possible_paths:
        if os.path.exists(p):
            csv_path = p
            break
            
    if not csv_path:
        print("Could not find train.csv")
        # List current dir to debug if needed
        print("Current directory:", os.listdir("."))
        if os.path.exists("empatheticdialogues"):
             print("Inside empatheticdialogues:", os.listdir("empatheticdialogues"))
        return

    print(f"Loading from {csv_path}...")
    try:
        df = pd.read_csv(csv_path, on_bad_lines='skip')
        print("\nDataset Info:")
        print(df.info())
        print("\nFirst 5 Rows:")
        print(df.head())
    except Exception as e:
        print(f"Error loading CSV: {e}")

if __name__ == "__main__":
    main()
