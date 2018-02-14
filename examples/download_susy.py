import urllib.request
import gzip
import shutil

suzy_location = "https://archive.ics.uci.edu/ml/machine-learning-databases/00279/SUSY.csv.gz"
filename = "SUSY.csv"
compressed_filename = filename + ".gz"

print("Downloading Suzy Dataset from {} as {}".format(suzy_location, compressed_filename))

# Download the SUSY dataset
with urllib.request.urlopen(suzy_location) as response, open(compressed_filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

print("Download of {} Complete".format(compressed_filename))


print("Decompressing {} to {}".format(compressed_filename, filename))

# Decompress the SUSY dataset
with gzip.open(compressed_filename, 'rb') as f_in:
    with open(filename, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("The SUSY dataset is now downloaded and extracted as {}".format(filename))