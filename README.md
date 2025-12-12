## Description

This repository includes a GitHub Actions workflow that performs automated security scanning on Python code using **Bandit** and uploads the results to **GitHub Code Scanning** in SARIF format.

Project source: [text](https://github.com/PyCQA/bandit/tree/main)

## Workflow Overview

The security scan workflow:

- Checks out the repository  
- Installs Python 3.11  
- Installs Bandit  
- Runs Bandit and generates a JSON report  
- Converts JSON to SARIF  
- Uploads the SARIF results to GitHub Code Scanning


