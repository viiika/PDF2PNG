import os
import subprocess
from tqdm import tqdm
import argparse

def convert_pdf(file_path, output_dir, resolution=400):
    file_name = os.path.basename(file_path)
    file_name = file_name.split(".")[0]

    results = subprocess.run(
        ["gs", "-dNOPAUSE", "-sDEVICE=png16m", f"-r{resolution}", 
         f"-sOutputFile={output_dir}/{file_name}-%02d.png", f"{file_path}", "-dBATCH"],
        stdout=subprocess.PIPE
    )

def main():
    parser = argparse.ArgumentParser(description="Convert PDF files to PNG images.")
    parser.add_argument("-i", "--input_dir", type=str, help="Directory containing PDF files.")
    parser.add_argument("-o", "--output_dir", type=str, help="Directory to save converted PNG files.")
    parser.add_argument("-r", "--resolution", type=int, default=400, help="Resolution of the output images (default: 400).")
    
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    total_files = 0
    for root, dirs, files in os.walk(args.input_dir):
        for file in tqdm(files):
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                convert_pdf(file_path, args.output_dir, args.resolution)
                total_files += 1

    print(f"{total_files} PDF files converted. Images are saved in '{args.output_dir}' directory.")
    print(f"{len(os.listdir(args.output_dir))} images in output directory.")

if __name__ == "__main__":
    main()
