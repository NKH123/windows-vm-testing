import os
from pathlib import Path
from google.cloud import storage

bucket_name = "automation-interns"
destination_file_name = ("./stuff.txt")
source_blob_name = "stuff.txt"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)
# blob.download_to_filename(destination_file_name)
bucket.list_blobs()




storage_client = storage.Client()
blobs = storage_client.list_blobs(bucket_name, prefix="test/execute_macro/code/")
for blob in blobs:
  print(blob.name)
  cur_dir = os.getcwd()
  destination_path = Path(cur_dir + "/../execte/action/code/")
  # destination_file_path = Path(destination_file_path
  if blob.name[len(blob.name)-1] == '/':
  	print("Making directory Destination path : ", destination_path)
  	os.makedirs(destination_file_path, exist_ok=True)
  else:
      print("Downloading file Destination path : ", destination_path)
      os.makedirs(destination_path, exist_ok=True)
      source = Path(blob.name)
      destination_file_path = Path(destination_path + source.name)
      print("Destination file path: ", destination_file_path)
      blob.download_to_filename(destination_file_path)
