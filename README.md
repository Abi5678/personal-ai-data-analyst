# Personal AI Data Analyst

An intelligent data analysis tool that converts natural language questions into Python code and executes them safely.

## Features

- **Smart Data Loading**: Automatically handles CSV, Excel, and JSON files
- **Intelligent Suggestions**: Detects column types and suggests relevant analyses
- **Deterministic Analysis**: Common queries are converted directly to code without LLM
- **LLM Integration**: Optional Ollama integration for custom queries
- **Safe Execution**: Code runs in a sandboxed environment
- **Visual Output**: Supports text, tables, and matplotlib charts

## Architecture

1. **Ingest**: Load any flat file (CSV, Excel, JSON)
2. **Detect**: Algorithmically understand column types (Numeric vs. Categorical)
3. **Reason**: Convert natural language into Python code
4. **Execute**: Run code in a sandboxed environment and return results

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Install Ollama for custom LLM queries:
```bash
# Install Ollama from https://ollama.ai
ollama pull llama3.1
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Upload your CSV, Excel, or JSON file

3. Choose from suggested analyses or write your own custom prompt

4. Click "Run analysis" to see results

## How It Works

### Built-in Prompts (No LLM Required)

The tool recognizes common data analysis patterns and converts them directly to code:

- Dataset summaries
- Top value counts for categorical columns
- Summary statistics for numeric columns
- Histograms and scatter plots
- Time series analysis
- Correlation matrices
- Anomaly detection using z-scores

### Custom Prompts (LLM Optional)

For custom queries, you can enable the local LLM option in the sidebar. The system will:
1. Send your prompt to Ollama
2. Extract the generated Python code
3. Execute it safely
4. Display the results

## Example Prompts

- "Summarize the dataset in 5 bullet points"
- "Create a histogram of the numeric column 'Age'"
- "Show the correlation matrix heatmap for numeric columns"
- "Find rows that look like anomalies using z-score > 3"
- "Show the top 10 rows sorted by 'Sales' descending"

## Safety Features

- Code execution in isolated namespace
- No file system access beyond temporary files
- Automatic cleanup of matplotlib figures
- Error handling and user-friendly messages

## Files

- `analyst.py`: Core analysis engine with data loading, prompt conversion, and execution
- `app.py`: Streamlit frontend interface
- `requirements.txt`: Python dependencies

## Why This Approach?

LLMs are excellent at understanding language but poor at math. Instead of asking the AI to calculate averages directly, we ask it to write the code that does the calculation. This combines:

- **Linguistic power of AI**: Understanding natural language queries
- **Computational precision of Python**: Accurate calculations and visualizations

You move from being the person who types the code to the person who designs the system that writes the code.
