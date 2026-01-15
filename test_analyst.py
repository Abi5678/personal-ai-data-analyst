"""
Simple test script to verify analyst.py functions work correctly.
Run this before starting the Streamlit app to ensure everything is set up correctly.
"""

import pandas as pd
from analyst import load_data, suggest_prompts, prompt_to_code, run_code

def test_basic_functionality():
    print("Testing Personal AI Data Analyst...\n")

    # Test 1: Load data
    print("1. Testing data loading...")
    try:
        df = load_data("sample_data.csv")
        print(f"   ✓ Data loaded successfully: {len(df)} rows, {len(df.columns)} columns")
    except Exception as e:
        print(f"   ✗ Failed to load data: {e}")
        return

    # Test 2: Generate suggestions
    print("\n2. Testing prompt suggestions...")
    try:
        suggestions = suggest_prompts(df)
        print(f"   ✓ Generated {len(suggestions)} suggestions:")
        for i, s in enumerate(suggestions[:3], 1):
            print(f"      {i}. {s}")
    except Exception as e:
        print(f"   ✗ Failed to generate suggestions: {e}")
        return

    # Test 3: Convert prompt to code
    print("\n3. Testing prompt-to-code conversion...")
    try:
        test_prompt = "Show summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for numeric columns."
        code = prompt_to_code(test_prompt, df)
        if code:
            print(f"   ✓ Successfully converted prompt to code")
        else:
            print(f"   ✗ No code generated for prompt")
    except Exception as e:
        print(f"   ✗ Failed to convert prompt: {e}")
        return

    # Test 4: Execute code
    print("\n4. Testing code execution...")
    try:
        result = run_code(df, code)
        if result['type'] == 'dataframe':
            print(f"   ✓ Code executed successfully")
            print(f"   Result type: {result['type']}")
            print(f"   Result shape: {result['df'].shape}")
        else:
            print(f"   ✓ Code executed, result type: {result['type']}")
    except Exception as e:
        print(f"   ✗ Failed to execute code: {e}")
        return

    print("\n✓ All tests passed! You're ready to run the Streamlit app.")
    print("\nTo start the app, run:")
    print("  streamlit run app.py")

if __name__ == "__main__":
    test_basic_functionality()
