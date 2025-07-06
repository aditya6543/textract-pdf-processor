# 🧠 Textract PDF Processor

A Python automation script to process large PDF documents with AWS Textract.

This tool allows you to:

- ✂️ Split large PDFs into 10-page chunks  
- ☁️ Upload them to AWS S3  
- 🤖 Run Textract to extract text content  
- 📁 Save the extracted results as clean, structured JSON files  

Ideal for:
- Training LLMs from PDFs  
- Extracting structured data from invoices, contracts, reports  
- Automating document pipelines for cloud-based applications
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