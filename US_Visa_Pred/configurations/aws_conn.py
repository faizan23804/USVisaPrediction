import boto3
import os
from US_Visa_Pred.constant.pipeline_info import (
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_ACCESS_KEY_ID_ENV_KEY,
    REGION_NAME,
)

class S3Client:

    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """
        Creates a singleton S3 client/resource using env credentials
        """

        if S3Client.s3_resource is None or S3Client.s3_client is None:

            access_key = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
            secret_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

            if access_key is None:
                raise Exception(f"Environment variable {AWS_ACCESS_KEY_ID_ENV_KEY} is not set")
            if secret_key is None:
                raise Exception(f"Environment variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set")

            # 🔥 STRIP WHITESPACE / NEWLINES
            access_key = access_key.strip()
            secret_key = secret_key.strip()
            region_name = region_name.strip()

            S3Client.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region_name,
            )

            S3Client.s3_client = boto3.client(
                "s3",
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region_name,
            )

        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client