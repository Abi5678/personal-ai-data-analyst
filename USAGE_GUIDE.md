# Personal AI Data Analyst - Usage Guide

## Quick Start

### Step 1: Verify Installation

Run the test script to ensure everything is working:

```bash
cd personal_ai_data_analyst
python3 test_analyst.py
```

You should see "All tests passed!" if everything is set up correctly.

### Step 2: Launch the Application

```bash
streamlit run app.py
```

This will open your default web browser with the application running at `http://localhost:8501`

### Step 3: Upload Your Data

- Click "Browse files" button
- Select a CSV, Excel (.xlsx, .xls), or JSON file
- The data will be automatically loaded and analyzed

### Step 4: Explore Your Data

The system will automatically generate suggestions based on your data structure:

- **Numeric columns** → Histograms, scatter plots, summary statistics
- **Categorical columns** → Top value counts, frequency analysis
- **DateTime columns** → Time series analysis, monthly aggregations
- **Mixed data** → Correlation matrices, anomaly detection

## Built-in Analysis Types

### 1. Dataset Summary
**Prompt**: "Summarize the dataset in 5 bullet points"

**Output**:
- Total rows and columns
- Column types
- Missing values
- Numeric column count
- Categorical insights

### 2. Categorical Analysis
**Prompt**: "Show the top 10 counts for the categorical column 'Product'"

**Output**: Table showing the most frequent values

### 3. Statistical Summary
**Prompt**: "Show summary statistics for numeric columns"

**Output**: Count, mean, std, min, 25%, 50%, 75%, max for each numeric column

### 4. Distribution Visualization
**Prompt**: "Create a histogram of the numeric column 'Sales'"

**Output**: Histogram chart showing distribution

### 5. Relationship Analysis
**Prompt**: "Create a scatter plot comparing 'Sales' (x) vs 'Units' (y)"

**Output**: Scatter plot showing correlation

### 6. Ranking
**Prompt**: "Show the top 10 rows sorted by 'Sales' descending"

**Output**: Table with highest values first

### 7. Time Series
**Prompt**: "Create a time series of monthly sum of 'Sales' using the datetime column 'Date'"

**Output**: Table or chart showing monthly trends

### 8. Correlation
**Prompt**: "Show the correlation matrix heatmap for numeric columns"

**Output**: Heatmap showing relationships between all numeric columns

### 9. Anomaly Detection
**Prompt**: "Find rows that look like anomalies using z-score > 3"

**Output**: Table of outlier rows

## Using the LLM Feature (Optional)

### Install Ollama

1. Visit https://ollama.ai and download Ollama for your OS
2. Install it
3. Pull a model:
   ```bash
   ollama pull llama3.1
   ```

### Enable in the App

1. In the sidebar, check "Use local LLM (ollama) for custom prompts"
2. Verify the model name matches your installed model (default: llama3.1)

### Custom Queries

Now you can ask natural language questions:

- "Calculate the moving average of Sales over 3 periods"
- "Show me products where Sales is greater than average"
- "Create a bar chart of total Sales by Category"
- "Find the percentage of Sales by Region"

The LLM will generate Python code, which will be executed safely.

## Tips for Best Results

### 1. Column Names
The system works best when your data has clear column names. If prompts fail, check that:
- Column names are quoted correctly in the prompt
- Column names match exactly (case-sensitive)

### 2. Data Types
- Numeric columns should contain numbers
- Date columns should be in a parseable format (YYYY-MM-DD recommended)
- Categorical columns work best with 50 or fewer unique values

### 3. Performance
- For large files (>10MB), expect longer load times
- Charts are limited to reasonable sizes automatically
- Use the "Preview data" expander to verify your data loaded correctly

### 4. Custom Prompts
When writing custom prompts:
- Be specific about column names (use quotes)
- Mention the type of output you want (table, chart, statistics)
- Reference the built-in prompts as examples

## Example Workflow

Let's analyze the included `sample_data.csv`:

1. **Upload the file** → sample_data.csv
2. **Run first prompt** → "Summarize the dataset in 5 bullet points"
   - See overview: 26 rows, 6 columns
   - Identify numeric: Sales, Units
   - Identify categorical: Product, Category, Region

3. **Explore distributions** → "Create a histogram of the numeric column 'Sales'"
   - See that laptops dominate high values

4. **Check relationships** → "Show the correlation matrix heatmap for numeric columns"
   - Discover if Sales and Units correlate

5. **Find insights** → "Show the top 10 counts for the categorical column 'Category'"
   - Electronics appears most frequently

6. **Deep dive** → "Show the top 10 rows sorted by 'Sales' descending"
   - Laptops are highest revenue items

## Troubleshooting

### "Failed to load file"
- Check file format (CSV, XLSX, JSON)
- Verify file is not corrupted
- Try opening in Excel/text editor first

### "Execution error"
- Column name might be misspelled
- Column might not exist
- Data type might not match operation (e.g., histogram on text column)

### "This is a custom prompt that the app cannot convert"
- Either enable LLM in sidebar
- Or rephrase to match a built-in pattern
- Check the suggested prompts for examples

### "LLM unavailable"
- Install Ollama: https://ollama.ai
- Pull a model: `ollama pull llama3.1`
- Verify it's running: `ollama list`

## Data Privacy

All processing happens locally:
- No data is sent to external servers (unless you modify the code)
- Ollama runs entirely on your machine
- Temporary files are created for charts but not uploaded anywhere

## Advanced: Understanding the Code Flow

1. **Upload** → `load_data()` in analyst.py
2. **Detect** → `_detect_column_types()` identifies numeric, datetime, categorical
3. **Suggest** → `suggest_prompts()` generates relevant questions
4. **Convert** → `prompt_to_code()` translates prompt to Python
5. **Execute** → `run_code()` runs code safely in isolated namespace
6. **Display** → Streamlit shows result (text, table, or image)

For custom prompts with LLM enabled:
1. Prompt sent to Ollama via `ask_llm()`
2. LLM returns Python code in markdown block
3. Code extracted and executed via `run_code()`
4. Result displayed

## Next Steps

- Try your own datasets
- Modify `analyst.py` to add new prompt patterns
- Customize the UI in `app.py`
- Add new chart types (seaborn, plotly)
- Integrate with databases instead of files
- Add authentication for multi-user deployments

## Support

If you encounter issues:
1. Check the terminal where you ran `streamlit run app.py` for error messages
2. Run the test script: `python3 test_analyst.py`
3. Verify all dependencies: `pip install -r requirements.txt`
4. Check that your data file is valid

Happy analyzing!
