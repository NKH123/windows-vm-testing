import os
from pathlib import Path
from google.cloud import storage



os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/neerajd/Downloads/Credentials/mocha-vm-experiments-f0dfbba7f499.json" 

bucket_name = "automation-interns"
storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
# blobs = storage_client.list_blobs(bucket_name, prefix="test/execute_macro/code/")
# for blob in blobs:
#   print(blob.name)
#   cur_dir = os.getcwd()
#   destination_path = Path(cur_dir + "/../execte/action/code/")
#   # destination_file_path = Path(destination_file_path
#   if blob.name[len(blob.name)-1] == '/':
#     print("Making directory Destination path : ", destination_path)
#     os.makedirs(destination_file_path, exist_ok=True)
#   else:
#       print("Downloading file Destination path : ", destination_path)
#       os.makedirs(destination_path, exist_ok=True)
#       source = Path(blob.name)
#       destination_file_path = Path(str(destination_path) + "\\" + str(source.name))
#       print("Destination file path: ", destination_file_path)
#       blob.download_to_filename(destination_file_path)
source_path = Path("../execute/action/output/")
destination_path = "test/execute_macro/output/"
files = os.listdir(source_path)
print("Files: ",files)
# try:
for file in files:
  print("File: ",file)  
  destination_blob_path = (destination_path + file)
  blob = bucket.blob(destination_blob_path)
  blob.upload_from_filename(str(source_path) + "/" + str(file))
# except Exception as exception:
  # print("Exception: ", exception)