# RAG-Based Data Analysis Chatbot using Local LLMs
## Academic Context

This project was developed as part of academic work at **Blekinge Institute of Technology (BTH)**.

The goal of the project is to explore **Retrieval-Augmented Generation (RAG)** techniques for performing data analysis using locally hosted Large Language Models (LLMs). The system enables natural language interaction with structured datasets and generates analytical insights through a modular AI pipeline.
## Author

**Rami M V**
Student – Blekinge Institute of Technology
Program: Bachelor of Computer Science


This project implements a **Retrieval-Augmented Generation (RAG) based chatbot** that performs data analysis on datasets using **locally hosted Large Language Models (LLMs)**.

## Features

* Natural language dataset querying
* RAG-based response generation
* Local LLM integration
* Modular Python architecture
* Automated result summarization

## Project Structure

```
rag-data-analysis-chatbot
│
├── dataset/
│   └── dataset.csv
│
├── main.py
├── dataset_loader.py
├── query_generator.py
├── llm_interface.py
├── comparator.py
├── result_summarizer.py
│
├── requirements.txt
└── README.md
```

## Installation

Clone the repository

```
git clone https://github.com/MVRami/rag-data-analysis-chatbot.git
cd rag-data-analysis-chatbot
```

Install dependencies

```
pip install -r requirements.txt
```

Run the chatbot

```
python main.py
```
