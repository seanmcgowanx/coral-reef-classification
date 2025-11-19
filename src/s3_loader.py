import boto3
from botocore.config import Config
from botocore import UNSIGNED
import io
from PIL import Image

# Anonymous S3 client for MERMAID public bucket
s3 = boto3.client(
    "s3",
    region_name="us-east-1",
    config=Config(signature_version=UNSIGNED)
)

def get_image_s3(image_id: str, thumbnail: bool = False, 
                 bucket: str = "coral-reef-training"):
    key = f"mermaid/{image_id}_thumbnail.png" if thumbnail else f"mermaid/{image_id}.png"
    resp = s3.get_object(Bucket=bucket, Key=key)
    return Image.open(io.BytesIO(resp["Body"].read()))
