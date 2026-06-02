from flask import Flask, render_template, request
import boto3
import os
from dotenv import load_dotenv
from uuid import uuid4

# Force reload .env values
load_dotenv(override=True)

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

print("AWS_ACCESS_KEY_ID =", repr(AWS_ACCESS_KEY_ID))
print("AWS_REGION =", repr(AWS_REGION))
print("BUCKET_NAME =", repr(BUCKET_NAME))

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    image_url = None

    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            return "No file selected"

        try:
            print("Using bucket:", repr(BUCKET_NAME))

            filename = f"uploads/{uuid4()}-{file.filename}"

            s3.upload_fileobj(
                file,
                BUCKET_NAME,
                filename,
                ExtraArgs={"ContentType": file.content_type}
            )

            image_url = f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{filename}"

        except Exception as e:
            return f"Upload Error: {e}"

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)