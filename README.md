# 🧠 Textract PDF Processor

A Python automation tool to:
1. 📄 Split large PDFs into 10-page chunks
2. ☁️ Upload them to AWS S3
3. 🤖 Use Amazon Textract to extract text from each PDF
4. 📂 Save extracted data as JSON files

---

## 🚀 Features

- Fast and efficient for large PDFs
- Fully automated using AWS Textract
- Clean folder structure and JSON outputs
- Logs progress with clear symbols ✅ 📤 📁 ⏳

---

## 📦 Requirements

- Python 3.7+
- AWS credentials configured (`~/.aws/credentials`)
- IAM role with S3 and Textract permissions

Install required packages:

```bash
pip install boto3 PyPDF2