> 🎥 YouTube Playlist: [Watch the full tutorial series](https://www.youtube.com/playlist?list=PLMmMgFk39zKU7pDC4exRYB6575zcJuNoC)


# 📄 Talk With Your Bills

An end-to-end AI-powered expense tracker that extracts structured data from image-based bills/invoices, stores it in a database, and lets you **view**, **filter**, and **chat** with your expense data using natural language.

---

## ✨ Features

- **Image Preprocessing** — Cleans bill images using OpenCV (grayscale, noise removal, binarization) for better OCR accuracy
- **OCR Extraction** — Extracts raw text from bill images using Tesseract
- **AI-Powered Parsing** — Uses a local LLM (Ollama) to convert raw text into structured JSON (invoice number, date, amounts, etc.)
- **Auto-Categorization** — Each line item is automatically categorized (Food, Travel, Utilities, etc.) by the LLM
- **SQLite Storage** — Parsed data is stored in a local SQLite database
- **Interactive Dashboard** — Streamlit frontend with dynamic filters by category and invoice number
- **Natural Language Chat** — Ask questions about your expenses in plain English; the LLM generates SQL queries and returns results

---

## 🏗️ Architecture

```
bill_image/                  → Raw bill images (input)
    │
    ▼
[image_cleaning.py]          → OpenCV preprocessing (grayscale, blur, binarization)
    │
    ▼
image_cleaning_one_folder/   → Cleaned images (output)
    │
    ▼
[ocr_processor.py]           → Tesseract OCR → extracted_text.txt
    │
    ▼
[parser.py]                  → Splits text by bill, calls LLM agents
    ├── [ollama1.py + prompt1.py]  → Agent 1: Extract structured JSON from raw text
    └── [ollama2.py + prompt2.py]  → Agent 2: Categorize each line item
    │
    ▼
[data_insertion.py]          → Insert structured data into SQLite
    │
    ▼
[frontend2.py]               → Streamlit dashboard + chat interface
    └── [ollama3.py + prompt3.py]  → Agent 3: Convert user questions to SQL
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Image Preprocessing | OpenCV (`opencv-python`) |
| OCR | Tesseract (`pytesseract`) |
| LLM | Ollama (phi3:3.8b) |
| Database | SQLite |
| Frontend | Streamlit |
| Data Handling | Pandas |
| Filters | streamlit-dynamic-filters |

---

## 📋 Prerequisites

1. **Python 3.8+**
2. **Tesseract OCR** — [Download & Install](https://github.com/UB-Mannheim/tesseract/wiki)
3. **Ollama** — [Download & Install](https://ollama.com/) and pull the model:
   ```bash
   ollama pull phi3:3.8b
   ```

---

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/talk_with_your_bills.git
   cd talk_with_your_bills
   ```

2. Install Python dependencies:
   ```bash
   pip install opencv-python pytesseract pandas streamlit streamlit-dynamic-filters
   ```

3. Create the required folders:
   ```bash
   mkdir bill_image
   mkdir image_cleaning_one_folder
   ```

4. Update the Tesseract path in `ocr_processor.py` to match your installation:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\path\to\tesseract.exe"
   ```

---

## 📖 Usage

### Step 1: Add your bill images
Place your bill images (`.jpg`, `.jpeg`, `.png`) into the `bill_image/` folder.

### Step 2: Clean the images
```bash
python image_cleaning.py
```

### Step 3: Extract text using OCR
```bash
python ocr_processor.py
```

### Step 4: Create the database table
```bash
python table_creation.py
```

### Step 5: Parse and insert data
```bash
python data_insertion.py
```
This runs the LLM to extract structured data and categorize each expense.

### Step 6: Launch the dashboard
```bash
streamlit run frontend2.py
```

---

## 💬 Chat Examples

Once the dashboard is running, try asking questions like:

- "Show me all expenses in the Food category"
- "What is the total amount billed by Amazon?"
- "List all invoices from January 2025"
- "Which category has the highest spending?"

The LLM converts your question into a SQL query and returns the result as a table.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `image_cleaning.py` | Preprocesses bill images using OpenCV |
| `ocr_processor.py` | Runs Tesseract OCR on cleaned images |
| `parser.py` | Orchestrates LLM extraction and categorization |
| `ollama1.py` | LLM Agent 1 — Extracts structured JSON from invoice text |
| `ollama2.py` | LLM Agent 2 — Categorizes each line item |
| `ollama3.py` | LLM Agent 3 — Converts user questions to SQL queries |
| `prompt1.py` | Prompt template for data extraction |
| `prompt2.py` | Prompt template for categorization |
| `prompt3.py` | Prompt template for natural language to SQL |
| `table_creation.py` | Creates the SQLite database and table |
| `data_insertion.py` | Inserts parsed data into the database |
| `frontend1.py` | Streamlit dashboard (table + filters) |
| `frontend2.py` | Streamlit dashboard (table + filters + chatbot) |
| `ocr_master.db` | SQLite database file |
| `extracted_text.txt` | Raw OCR output |

---

## 📊 Database Schema

**Table: `ocr_line_items`**

| Column | Type | Description |
|--------|------|-------------|
| `Invoice_No` | TEXT | Unique invoice identifier (PK) |
| `line_item_id` | INTEGER | Line item serial number (PK) |
| `Issue_Date` | TEXT | Date of the invoice |
| `billed_to` | TEXT | Who was billed |
| `billed_by` | TEXT | Who issued the bill |
| `Description` | TEXT | Service/item description |
| `Category` | TEXT | Auto-assigned category |
| `Amount` | REAL | Amount for the line item |
| `Grand_Total` | REAL | Total invoice amount |
| `source_file` | TEXT | Original image filename |

---

## 🏷️ Expense Categories

- Food
- Logistic
- Drinks
- Travel
- Grocery Expense
- Utilities
- Other

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests. Suggestions and improvements are welcome!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
