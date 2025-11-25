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
    """
    Streams a MERMAID image directly from the public S3 bucket.

    Returns a PIL.Image in RGB mode.
    """
    key = f"mermaid/{image_id}_thumbnail.png" if thumbnail else f"mermaid/{image_id}.png"
    
    try:
        resp = s3.get_object(Bucket=bucket, Key=key)
        img = Image.open(io.BytesIO(resp["Body"].read())).convert("RGB")
        return img
    except Exception as e:
        raise RuntimeError(f"Could not load image {image_id} from S3. Key tried: {key}. Error: {e}")

