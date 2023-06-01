from google.cloud import storage

client = storage.Client()

# creating a new storage bucket
new_bucket = client.create_bucket('python-bugs-storage-123')

# creating a file(blob) to be uploaded
new_blob = new_bucket.blob('test-folder/example_file.py')

# Uploading the file
new_blob.upload_from_filename(filename='example_file.py')
