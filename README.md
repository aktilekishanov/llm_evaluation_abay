# LLM Translation Evaluation Project

This project evaluates and compares the translation capabilities of different Large Language Models (LLMs) for Kazakh-English translation tasks.

## Project Overview

The project focuses on:
- Evaluating translation quality between Kazakh and English languages
- Comparing performance of different LLMs (ChatGPT and Gemini)
- Analyzing translation metrics and generating visualizations
- Assessing translation accuracy and quality

## Project Structure

- `Abay.ipynb`: Main Jupyter notebook containing the evaluation workflow
- `accessment_chatgpt.py`: Script for evaluating ChatGPT translations
- `accessment_gemini.py`: Script for evaluating Gemini translations
- `chat.py`: Utility script for chat interactions
- `golden.json`: Reference translations dataset
- `kazakh.json`: Original Kazakh text dataset
- `kazakh_translated.json`: ChatGPT translations
- `kazakh_translated_gemini.json`: Gemini translations
- `translation_evaluation.csv`: Detailed evaluation metrics
- `translation_evaluation_gemini.csv`: Gemini-specific evaluation metrics
- `average_scores.csv`: Aggregated scores for ChatGPT
- `average_scores_gemini.csv`: Aggregated scores for Gemini
- `translation_metrics_plot.png`: Visualization of translation metrics

## Setup

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Unix/macOS
# or
.\env\Scripts\activate  # On Windows
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the evaluation scripts:
```bash
python accessment_chatgpt.py  # For ChatGPT evaluation
python accessment_gemini.py   # For Gemini evaluation
```

2. Open `Abay.ipynb` in Jupyter Notebook to:
   - View the complete evaluation workflow
   - Generate visualizations
   - Analyze results

## Results

The project generates:
- Detailed translation evaluations in CSV format
- Average scores for each model
- Visual comparison of translation metrics
- Performance analysis of different LLMs

## Notes

- Ensure you have the necessary API keys for ChatGPT and Gemini
- The evaluation metrics include accuracy, fluency, and overall quality scores
- Results are saved in both CSV and JSON formats for further analysis 