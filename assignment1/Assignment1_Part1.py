# %% [markdown]
# # Assignment 1 - Part 1: Regular Expressions and Date Extraction
# 
# **Course:** Natural Language Processing
# 
# **Total Points:** 10 points (contributes to 50% of Assignment 1)
# 
# ---
# 
# ## Instructions
# 
# 1. Complete all the functions marked with `# YOUR CODE HERE`
# 2. **DO NOT** change the function names or their signatures
# 3. Each function must return the exact type specified
# 4. Test your functions by running the test cells
# 5. When finished:
#    - Export this notebook as a Python file (.py)
#    - **Name the file:** `LASTNAME_FIRSTNAME_assignment1_part1.py`
#    - Example: `DUPONT_Jean_assignment1_part1.py`
#    - Push to your GitHub repository
#    - Send the .py file by email to: **yoroba93@gmail.com**
# 
# ---
# 
# ## Assignment Overview
# 
# In this assignment, you'll work with messy medical data and use regex to extract relevant information.
# 
# Each line of the `dates.txt` file corresponds to a medical note. Each note has a date that needs to be extracted, but dates are encoded in many different formats.
# 
# **Date formats you may encounter:**
# - `04/20/2009; 04/20/09; 4/20/09; 4/3/09`
# - `Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009`
# - `20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009`
# - `Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009`
# - `Feb 2009; Sep 2009; Oct 2010`
# - `6/2008; 12/2009`
# - `2009; 2010`
# 
# ---

# %% [markdown]
# ## Setup

# %%
import pandas as pd
import numpy as np
import re
from datetime import datetime

# Load the data
doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
print(f"Loaded {len(df)} medical notes")
print("\nFirst 5 notes:")
print(df.head())

# %% [markdown]
# ---
# 
# ## Question 1 (1 point)
# 
# **Write a regex pattern to extract dates in the format `MM/DD/YY` or `MM/DD/YYYY`.**
# 
# Examples: `03/25/93`, `6/18/85`, `5/24/1990`, `1/25/2011`
# 
# *This function should return a list of all matched date strings.*

# %%
def question_one():
    """
    Extract all dates in MM/DD/YY or MM/DD/YYYY format.
    
    Returns:
        list: List of matched date strings
    """
    pattern = r"\b\d{1,2}/\d{1,2}/\d{2,4}\b" 
    
    results = []
    for note in df:
        matches = re.findall(pattern, note)
        results.extend(matches)
    
    return results

# Test your function
q1_result = question_one()
print(f"Found {len(q1_result)} dates")
print(f"First 10: {q1_result[:10]}")

# %% [markdown]
# ---
# 
# ## Question 2 (1 point)
# 
# **Write a regex pattern to extract dates with month names.**
# 
# Examples: `Mar-20-2009`, `March 20, 2009`, `Mar 20 2009`, `Mar. 20, 2009`
# 
# *This function should return a list of all matched date strings.*

# %%
def question_two():
    """
    Extract all dates with month names (e.g., Mar 20, 2009).
    
    Returns:
        list: List of matched date strings
    """
    pattern = r"[A-Za-z]{3} \d{1,2}, \d{4}"  
    
    results = []
    for note in df:
        matches = re.findall(pattern, note)
        results.extend(matches)
    
    return results

# Test your function
q2_result = question_two()
print(f"Found {len(q2_result)} dates")
print(f"First 10: {q2_result[:10]}")

# %% [markdown]
# ---
# 
# ## Question 3 (1 point)
# 
# **Write a regex pattern to extract dates in the format `DD Month YYYY`.**
# 
# Examples: `20 Mar 2009`, `20 March 2009`, `20 Mar. 2009`
# 
# *This function should return a list of all matched date strings.*

# %%
def question_three():
    """
    Extract all dates in DD Month YYYY format.
    
    Returns:
        list: List of matched date strings
    """
    
    pattern = r"\b\d{1,2} [A-Za-z]{3} \d{4}\b" 
    
    results = []
    for note in df:
        matches = re.findall(pattern, note)
        results.extend(matches)
    
    return results

# Test your function
q3_result = question_three()
print(f"Found {len(q3_result)} dates")
print(f"First 10: {q3_result[:10]}")

# %% [markdown]
# ---
# 
# ## Question 4 (1 point)
# 
# **Write a function that uses regex to extract all email addresses from a given text.**
# 
# Test text is provided below.
# 
# *This function should return a list of email addresses.*

# %%
def question_four(text):
    """
    Extract all email addresses from text.
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of email addresses
    """
    
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  
    
    return re.findall(pattern, text)

# Test your function
test_text = """
Contact us at support@company.com or sales@company.org.
You can also reach john.doe@email.co.uk or jane_doe123@university.edu.
Invalid emails: @invalid.com, user@, not-an-email
"""

q4_result = question_four(test_text)
print(f"Found emails: {q4_result}")

# %% [markdown]
# ---
# 
# ## Question 5 (1 point)
# 
# **Write a function that uses regex to clean text by:**
# 1. Removing all digits
# 2. Removing all punctuation except spaces
# 3. Converting to lowercase
# 4. Removing extra whitespace
# 
# *This function should return the cleaned string.*

# %%
def question_five(text):
    """
    Clean text by removing digits, punctuation, and normalizing whitespace.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Cleaned text
    """

    cleaned = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    cleaned = re.sub(r'\d+', '', cleaned)  # Remove digits
    cleaned = cleaned.lower()  # Convert to lowercase
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()  # Normalize whitespace
    return cleaned 

# Test your function
test_text = "Hello, World! 123 This is a TEST... with 456 numbers!!!"
q5_result = question_five(test_text)
print(f"Original: '{test_text}'")
print(f"Cleaned:  '{q5_result}'")
# Expected: 'hello world this is a test with numbers'

# %% [markdown]
# ---
# 
# ## Question 6 (2 points)
# 
# **Write a function that extracts and validates phone numbers.**
# 
# Valid formats:
# - `XXX-XXX-XXXX`
# - `(XXX) XXX-XXXX`
# - `XXX.XXX.XXXX`
# - `XXX XXX XXXX`
# 
# *This function should return a list of phone numbers in standardized format `XXX-XXX-XXXX`.*

# %%
def question_six(text):
    """
    Extract phone numbers and return them in XXX-XXX-XXXX format.
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of phone numbers in XXX-XXX-XXXX format
    """

    pattern = r"(?:\((\d{3})\)|(\d{3}))[\s\.\-](\d{3})[\s\.\-](\d{4})"
    matches = re.findall(pattern, text)
    standardized = []
    for g1, g2, g3, g4 in matches:
        area = g1 if g1 else g2
        digits = f"{area}{g3}{g4}"
        standardized.append(f"{digits[:3]}-{digits[3:6]}-{digits[6:]}")
    return standardized

# Test your function
test_text = """
Call us at 123-456-7890 or (555) 123-4567.
You can also reach us at 888.555.1234 or 999 888 7777.
Invalid: 12-34-5678, 1234567890
"""

q6_result = question_six(test_text)
print(f"Found phones: {q6_result}")
# Expected: ['123-456-7890', '555-123-4567', '888-555-1234', '999-888-7777']

# %% [markdown]
# ---
# 
# ## Question 7 (3 points)
# 
# **This is the main challenge: Extract all dates from the medical notes and sort them chronologically.**
# 
# **Rules:**
# - Assume all dates in `xx/xx/xx` format are `mm/dd/yy`
# - Assume all 2-digit years are from the 1900s (e.g., `1/5/89` is January 5th, 1989)
# - If the day is missing (e.g., `9/2009`), assume it is the 1st day of the month
# - If the month is missing (e.g., `2010`), assume it is January 1st
# 
# *This function should return a pandas Series of length 500, where the values are the original indices sorted by date in ascending chronological order.*
# 
# **Example:**
# ```python
# # If original series was:
# #    0    1999
# #    1    2010
# #    2    1978
# # Your function should return:
# #    0    2    (1978 is earliest)
# #    1    0    (1999 is second)
# #    2    1    (2010 is latest)
# ```

# %%
def question_seven():
    """
    Extract dates from all medical notes and return indices sorted chronologically.
    
    Returns:
        pd.Series: Series of length 500 with original indices sorted by date
    """
    global df
    
    # 1. Define patterns using standard groups instead of named groups
    # We will extract: Month, Day, Year
    
    # Format: 03/25/93 or 3-25-1993
    p1 = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
    # Format: Mar 20, 2009 or March 20 2009
    p2 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?)\s+(\d{1,2})[?,\s]+(\d{4})'
    # Format: 20 Mar 2009
    p3 = r'(\d{1,2})\s+((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)\s+(\d{4})'
    # Format: March 2009 (No Day)
    p4 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*)\s+(\d{4})'
    # Format: 3/2009 (No Day)
    p5 = r'(\d{1,2})[/](\d{4})'
    # Format: 2009 (Year only)
    p6 = r'(\d{4})'

    # 2. Extract and fill a DataFrame manually to handle different structures
    # We use expand=True to get a DataFrame
    res = pd.DataFrame(index=df.index, columns=['month', 'day', 'year'])
    
    # helper to map month names
    m_map = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

    # Order of operations matters: start with the most specific (p1-p3) 
    # and use fillna to let less specific patterns fill the gaps.
    
    # Try P1
    ext1 = df.str.extract(p1)
    res['month'] = res['month'].fillna(ext1[0])
    res['day'] = res['day'].fillna(ext1[1])
    res['year'] = res['year'].fillna(ext1[2])
    
    # Try P2
    ext2 = df.str.extract(p2)
    res['month'] = res['month'].fillna(ext2[0].str[:3].map(m_map))
    res['day'] = res['day'].fillna(ext2[1])
    res['year'] = res['year'].fillna(ext2[2])
    
    # Try P3
    ext3 = df.str.extract(p3)
    res['day'] = res['day'].fillna(ext3[0])
    res['month'] = res['month'].fillna(ext3[1].str[:3].map(m_map))
    res['year'] = res['year'].fillna(ext3[2])

    # Try P4 (Month Year)
    ext4 = df.str.extract(p4)
    res['month'] = res['month'].fillna(ext4[0].str[:3].map(m_map))
    res['year'] = res['year'].fillna(ext4[1])

    # Try P5 (MM/YYYY)
    ext5 = df.str.extract(p5)
    res['month'] = res['month'].fillna(ext5[0])
    res['year'] = res['year'].fillna(ext5[1])
    
    # Try P6 (YYYY)
    ext6 = df.str.extract(p6)
    res['year'] = res['year'].fillna(ext6[0])

    # 3. Final Cleaning
    res['day'] = res['day'].fillna('1')
    res['month'] = res['month'].fillna('1')
    
    # Rule: 2-digit years are 1900s
    res['year'] = res['year'].apply(lambda x: '19'+str(x) if len(str(x)) == 2 else x)
    
    # 4. Convert to datetime and sort
    dates = pd.to_datetime(res)
    return pd.Series(dates.sort_values(kind='mergesort').index)

# Test your function
q7_result = question_seven()
print(f"Result length: {len(q7_result)}")
print(f"First 10 indices: {list(q7_result.head(10))}")
print(f"Last 10 indices: {list(q7_result.tail(10))}")

# %% [markdown]
# ---
# 
# ## Summary of Functions for Grading
# 
# Make sure all these functions are properly implemented before exporting:

# %%
# Run this cell to verify all functions exist and return correct types
print("Checking functions...")

try:
    r1 = question_one()
    assert isinstance(r1, list), "question_one should return a list"
    print("✓ question_one: OK")
except Exception as e:
    print(f"✗ question_one: {e}")

try:
    r2 = question_two()
    assert isinstance(r2, list), "question_two should return a list"
    print("✓ question_two: OK")
except Exception as e:
    print(f"✗ question_two: {e}")

try:
    r3 = question_three()
    assert isinstance(r3, list), "question_three should return a list"
    print("✓ question_three: OK")
except Exception as e:
    print(f"✗ question_three: {e}")

try:
    r4 = question_four("test@email.com")
    assert isinstance(r4, list), "question_four should return a list"
    print("✓ question_four: OK")
except Exception as e:
    print(f"✗ question_four: {e}")

try:
    r5 = question_five("Hello World 123")
    assert isinstance(r5, str), "question_five should return a string"
    print("✓ question_five: OK")
except Exception as e:
    print(f"✗ question_five: {e}")

try:
    r6 = question_six("123-456-7890")
    assert isinstance(r6, list), "question_six should return a list"
    print("✓ question_six: OK")
except Exception as e:
    print(f"✗ question_six: {e}")

try:
    r7 = question_seven()
    assert isinstance(r7, pd.Series), "question_seven should return a pandas Series"
    print("✓ question_seven: OK")
except Exception as e:
    print(f"✗ question_seven: {e}")

print("\nDone! Export this notebook as .py file when all functions pass.")

# %% [markdown]
# ---
# 
# ## Submission Checklist
# 
# - [ ] All 7 functions are implemented
# - [ ] All functions return the correct type
# - [ ] Notebook exported as Python file
# - [ ] File named: `LASTNAME_FIRSTNAME_assignment1_part1.py`
# - [ ] Pushed to GitHub repository
# - [ ] Sent to **yoroba93@gmail.com**


