#!/bin/bash
echo Setting up S3 Bucket for local stack

awslocal s3api create-bucket --bucket <YOUR_S3_BUCKET_NAME_HERE>

# Define CORS config
cat << EOF > localstack-s3-cors-config.json
{
    "CORSRules": [
        {
            "AllowedHeaders": [
                "*"
            ],
            "AllowedMethods": [
                "GET",
                "PUT"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": [
                "Access-Control-Allow-Origin",
                "Access-Control-Allow-Methods",
                "Access-Control-Allow-Headers",
                "ETag"
            ]
        }
    ]
}
EOF

awslocal s3api put-bucket-cors --bucket <YOUR_S3_BUCKET_NAME_HERE> --cors-configuration file://localstack-s3-cors-config.json
awslocal s3api get-bucket-cors --bucket <YOUR_S3_BUCKET_NAME_HERE>
