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
blobs = storage_client.list_blobs(bucket_name)
for blob in blobs:
  print(blob.name)
  cur_dir = os.getcwd()
  destination_path = Path(cur_dir + "/" + blob.name)
  if destination_path.exists() is False:
      print("Destination path : ", destination_path)
      os.makedirs(destination_path)
  blob.download_to_filename(destination_path)
