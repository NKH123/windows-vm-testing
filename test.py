from google.cloud import storage

bucket_name = "automation-interns"
destination_file_name = ("./stuff.txt")
source_blob_name = "stuff.txt"
storage_client = storage.Client()
blobs = storage_client.list_blobs(bucket_name)
for blob in blobs:
  print(blob.name)