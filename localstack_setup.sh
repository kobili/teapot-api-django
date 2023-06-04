#!/bin/bash
echo Setting up S3 Bucket for local stack

awslocal s3api create-bucket --bucket s3-images-kli-99

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

awslocal s3api put-bucket-cors --bucket s3-images-kli-99 --cors-configuration file://localstack-s3-cors-config.json
awslocal s3api get-bucket-cors --bucket s3-images-kli-99
