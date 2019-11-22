import glob, os, shutil
import zipfile

def delete_previous_files(path):
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)

def unzip_files(zip_dir = "data/marvel_movies_srt/zip/", directory_to_extract_to = "data/marvel_movies_srt/srt/"):
    delete_previous_files(directory_to_extract_to)

    for file in glob.glob(zip_dir + "*.zip"):
        print("Unzipping: ",os.path.split(file)[-1])

        try:
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(directory_to_extract_to)
        except:
            print("Error occured.")

if __name__ == "__main__":
    unzip_files

