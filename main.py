import os
import time
import json
from PyPDF2 import PdfReader, PdfWriter
import boto3

# ========================
# 🔧 CONFIGURATION
# ========================
INPUT_PDF = "document.pdf"           # Input PDF (can be large)
CHUNK_FOLDER = "chunks"              # Where to save split PDFs
OUTPUT_FOLDER = "output_json"        # Where to save Textract JSONs
BUCKET = "your-s3-bucket-name"       # Your S3 bucket
S3_PREFIX = "uploads/"               # S3 folder prefix
REGION = "ap-south-1"                # AWS region
CHUNK_SIZE = 10                      # Pages per chunk

# ========================
# 📁 SETUP AWS CLIENTS
# ========================
s3 = boto3.client("s3", region_name=REGION)
textract = boto3.client("textract", region_name=REGION)

# ========================
# ✂️ PDF SPLITTER FUNCTION
# ========================
def split_pdf_into_chunks(input_pdf, output_folder, base_name, pages_per_chunk):
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    os.makedirs(output_folder, exist_ok=True)
    file_list = []

    for i in range(0, total_pages, pages_per_chunk):
        writer = PdfWriter()
        chunk_number = i // pages_per_chunk + 1
        output_filename = f"{base_name}-{chunk_number}.pdf"
        output_path = os.path.join(output_folder, output_filename)

        for j in range(i, min(i + pages_per_chunk, total_pages)):
            writer.add_page(reader.pages[j])

        with open(output_path, "wb") as f:
            writer.write(f)

        file_list.append(output_filename)
        print(f"✅ Created chunk: {output_path}")

    return file_list

# ========================
# 🚀 TEXTRACT UPLOAD + PROCESS
# ========================
def process_chunks(chunks, folder, output_folder, bucket, s3_prefix):
    os.makedirs(output_folder, exist_ok=True)

    for filename in chunks:
        local_path = os.path.join(folder, filename)
        s3_key = s3_prefix + filename

        print(f"\n📤 Uploading: {filename} to S3")
        s3.upload_file(local_path, bucket, s3_key)

        print(f"🚀 Starting Textract Job...")
        response = textract.start_document_text_detection(
            DocumentLocation={'S3Object': {'Bucket': bucket, 'Name': s3_key}}
        )
        job_id = response["JobId"]

        print(f"⏳ Waiting for Textract job to complete...")
        while True:
            result = textract.get_document_text_detection(JobId=job_id)
            status = result["JobStatus"]
            if status == "SUCCEEDED":
                print(f"✅ Textract done for {filename}")
                break
            elif status == "FAILED":
                print(f"❌ Textract failed for {filename}")
                break
            time.sleep(5)

        output_json = filename.replace(".pdf", ".json")
        output_path = os.path.join(output_folder, output_json)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"📁 Saved: {output_path}")

# ========================
# 🧠 MAIN FLOW
# ========================
if __name__ == "__main__":
    base_name = os.path.splitext(os.path.basename(INPUT_PDF))[0].replace(" ", "_")
    print(f"\n📂 Splitting PDF: {INPUT_PDF}")
    chunked_files = split_pdf_into_chunks(INPUT_PDF, CHUNK_FOLDER, base_name, CHUNK_SIZE)

    print(f"\n🤖 Running Textract on {len(chunked_files)} chunks...")
    process_chunks(chunked_files, CHUNK_FOLDER, OUTPUT_FOLDER, BUCKET, S3_PREFIX)

    print("\n✅ DONE: All chunks processed and JSONs saved.")