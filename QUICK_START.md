# Quick Start Guide

## 1. Install Dependencies (30 seconds)

```bash
pip install streamlit pandas matplotlib numpy scipy openpyxl
```

## 2. Test the Installation (10 seconds)

```bash
cd personal_ai_data_analyst
python3 test_analyst.py
```

Expected output: `✓ All tests passed!`

## 3. Launch the App (5 seconds)

```bash
streamlit run app.py
```

Your browser will open automatically at `http://localhost:8501`

## 4. Try It Out (1 minute)

1. Click "Browse files"
2. Upload `sample_data.csv` (included in this folder)
3. Click on the first suggestion: "Summarize the dataset..."
4. Click "Run analysis"
5. See the results!

## 5. Explore More

Try these suggested prompts:
- "Show the top 10 counts for the categorical column 'Product'"
- "Create a histogram of the numeric column 'Sales'"
- "Show the correlation matrix heatmap for numeric columns"

## Optional: Enable LLM for Custom Queries

### Install Ollama

```bash
# Visit https://ollama.ai and install for your OS
# Then pull a model:
ollama pull llama3.1
```

### Enable in App

1. In the sidebar, check "Use local LLM (ollama) for custom prompts"
2. Now try custom questions like:
   - "Show products where Sales > 500"
   - "Calculate the average Units by Category"

## That's It!

You now have a working AI Data Analyst. Upload your own CSV files and start exploring!

## Troubleshooting

**App won't start?**
```bash
pip install --upgrade streamlit
```

**Import errors?**
```bash
pip install -r requirements.txt
```

**File won't upload?**
- Make sure it's CSV, XLSX, or JSON format
- Check file isn't corrupted (open it in Excel first)

## Files Overview

- `analyst.py` - The brain (you don't need to touch this)
- `app.py` - The interface (customize if you want)
- `sample_data.csv` - Test dataset
- `test_analyst.py` - Verify everything works

## Next Steps

1. ✅ Got it working? Try your own datasets!
2. 📖 Read `USAGE_GUIDE.md` for detailed features
3. 🔧 Read `PROJECT_SUMMARY.md` to understand the architecture
4. 🚀 Customize and extend as needed!

---

**Total time to working app: ~2 minutes** ⏱️
