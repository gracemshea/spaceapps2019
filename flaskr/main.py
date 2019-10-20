
from flask import Flask, request, Response
from google.cloud import storage
import pdb

app = Flask('__name__')

@app.route("/upload_csv", methods=["POST"])
def upload_csv():
  file = request.files.get("file")
  if file == None:
    return Response(status=400)
  else:
    success = upload("spaceapps2019", file, file.filename)
    if success:
      return Response(status=200)
    else:
      return Response(status=400)


def upload(bucket_name, source_file, destination_blob_name):
  """Uploads a file to the bucket."""
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  try:
    blob.upload_from_file(source_file)
  except:
    return None
  else:
    return('File {} uploaded to {}.'.format(
      source_file,
      destination_blob_name))

    

  
