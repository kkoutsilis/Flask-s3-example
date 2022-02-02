import os
from minio import Minio
from werkzeug.datastructures import FileStorage


class StorageService:
    def __init__(self) -> None:
        self.client = Minio(
            endpoint="localhost:9000",
            access_key="minio",
            secret_key="minio123",
            secure=False,
        )

    def create_bucket(self, bucket_name: str) -> None:
        self.client.make_bucket(bucket_name=bucket_name)

    def upload(self, bucket_name: str, file: FileStorage) -> dict:
        bucket_exists = self.client.bucket_exists(bucket_name)
        if not bucket_exists:
            self.create_bucket(bucket_name)
        file_size = os.fstat(file.fileno()).st_size

        res = self.client.put_object(bucket_name, file.filename, file, file_size)

        return {
            "name": res.object_name,
            "size": file_size,
            "etag": res.etag,
        }
