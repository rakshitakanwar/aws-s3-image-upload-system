# AWS S3 Image Upload System

A web application built using Python Flask and Amazon S3 that allows users to upload images directly to an AWS S3 bucket using AWS access credentials.

## Features

* Upload images to AWS S3 bucket
* Cloud-based image storage
* Flask backend integration
* Secure credential management using environment variables (.env)
* Simple and responsive interface

## Tech Stack

* Python
* Flask
* AWS S3
* HTML/CSS
* Boto3
* Python Dotenv

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Create virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Add AWS credentials in `.env`

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1
AWS_BUCKET_NAME=your_bucket_name
```

6. Run the application

```bash
python app.py
```

## Learning Outcome

This project helped in understanding cloud storage, AWS S3 integration, Flask backend development, file handling, and environment variable management.
