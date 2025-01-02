import boto3
from botocore.exceptions import NoCredentialsError

BUCKET_NAME = "bucket-name"

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to S3 bucket and check permissions."""
    s3 = boto3.client('s3')

    # Set object name as file name if not provided
    if object_name is None:
        object_name = file_name

    try:
        # Upload file
        s3.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded successfully.")

        # Verify permissions
        check_permissions(bucket, object_name)

    except NoCredentialsError:
        print("Credentials not available.")

def check_permissions(bucket, object_name):
    """Check public access permission of the uploaded object."""
    s3 = boto3.client('s3')
    acl = s3.get_object_acl(Bucket=bucket, Key=object_name)
    print(f"Permissions for {object_name}: {acl['Grants']}")

# Upload a file
upload_file("about.html", BUCKET_NAME)

