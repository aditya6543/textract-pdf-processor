# Textract PDF Processor 📄🔍

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)

Textract PDF Processor is a simple Python-based utility that uses **Amazon Textract** to extract text from scanned or image-based PDF files. This tool is ideal for **OCR (Optical Character Recognition)** tasks, automating document parsing for further use in AI, machine learning, or data processing pipelines.

---

## 🧠 Why Textract?

AWS Textract is a machine learning service that goes beyond simple OCR to also identify fields, forms, and tables in scanned documents. It's highly scalable and accurate, making it perfect for enterprise and startup-grade document processing.

---

## 🚀 Features

- ✅ Extracts text from scanned PDFs using AWS Textract  
- 🗂️ Handles multi-page documents  
- ⚡ Simple CLI tool — no GUI required  
- 💾 Easily adaptable to save results as `.txt`, `.json`, etc.  
- 🔐 Uses your AWS credentials securely  

---

## 🧰 Requirements

- Python 3.6 or higher  
- AWS account with permission to use Textract  
- `boto3` (AWS SDK for Python)  

---

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:aditya6543/textract-pdf-processor.git
   cd textract-pdf-processor

2. Install dependencies

    pip install boto3


## 🔐 AWS Credentials Setup

Textract requires valid AWS credentials. You can configure them using any of the following methods:
1. Via AWS CLI (Recommended):

aws configure

It will ask for:

    AWS Access Key ID

    AWS Secret Access Key

    Default region (e.g., us-east-1)

    Output format (e.g., json)

2. Via Environment Variables:

export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key

## 📄 Usage

    Place your input PDF file in the same directory, or provide a full path.

    Open main.py and update the documentName variable:

documentName = "your-pdf-file.pdf"

Run the script:

    python main.py

The output will be printed in the terminal.

## 🔁 Optional: Save output to a .txt file

In main.py, replace:

print("Detected text: " + block['Text'])

with:

with open("output.txt", "a") as f:
    f.write(block['Text'] + "\n")

## 🧪 Sample Output

Detected text: Invoice Number: #45678  
Detected text: Date: 2024-01-01  
Detected text: Item Description: Cloud Hosting Service  
Detected text: Total Amount: ₹3,000  

## 📁 Recommended .gitignore

__pycache__/
*.pyc
.env
output.txt

## 🧠 Future Improvements

    Add support for uploading PDFs directly to S3

    Export to .json with structured data

    Support for processing multiple PDFs in batch

    Add UI (CLI menu or Streamlit web version)

    Save parsed data into SQL/NoSQL database

## 🤝 Contributing

Contributions are welcome!

    Fork the repository

    Create your feature branch:

git checkout -b feature/my-feature

Commit your changes:

git commit -m 'Add some feature'

Push to the branch:

    git push origin feature/my-feature

    Open a pull request

## 🙋‍♂️ Author

Made with ❤️ by Aditya Kapse
Feel free to connect on GitHub or suggest ideas and improvements.

## 📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.

## 🌐 Links

    https://docs.aws.amazon.com/textract
     
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html



