# Working with images in the API

## Creating a new image for a Product
- Call the Create Product for User endpoint
    ```
    /users/<user_id>/product/
    ```
- The response will contain an array of images, each with the shape:
    ```json
    {
        "image_id": "fae48821-c464-4157-a3ca-6a10768fb727",
        "put_url": "https://0.0.0.0:4566/s3-images-kli-99/fae48821-c464-4157-a3ca-6a10768fb727?AWSAccessKeyId=localstack_placeholder&Signature=EQHS7vEQvZimnVee9gm3Nan5Bi0%3D&content-type=multipart%2Fform-data&Expires=1686360907",
        "get_url": "https://0.0.0.0:4566/s3-images-kli-99/fae48821-c464-4157-a3ca-6a10768fb727?AWSAccessKeyId=localstack_placeholder&Signature=5V84MojO%2FfkXEdsnQTPUPdVsaJw%3D&Expires=1686360907"
    }
    ```
    - The `put_url` field contains a Pre-signed AWS S3 URL with `PutObject` permissions, allowing the client to upload an image to the server's S3 bucket

## Creating a new image for an existing product
- Use the Create Image for Product endpoint
    ```
    POST /product/<product_id>/image/
    ```
- The response will again have a `put_url` field which will allow image uploads to S3

## Updating an existing image
- Use the Update Image for Product Endpoint
    ```
    PUT /product/<product_id>/image/<image_id>/
    ```
- The response will have a `put_url` field which will allow the client to overwrite the existing image on S3

## Deleting an image
- Use the Delete Image endpoint
    ```
    DELETE /product/<product_id>/image/<image_id>/
    ```
- The response will be empty; The image deletion on S3 and in DB will be handled by the server
