## Description

This repository includes a GitHub Actions workflow that performs automated security scanning on Python code using **Bandit** and uploads the results to **GitHub Code Scanning** in SARIF format.

## Workflow Overview

The security scan workflow:

- Checks out the repository  
- Installs Python 3.11  
- Installs Bandit  
- Runs Bandit and generates a JSON report  
- Converts JSON to SARIF  
- Uploads the SARIF results to GitHub Code Scanning


## SARIF to GHAS
<img width="929" height="925" alt="SARIF to GHAS Integration" src="https://github.com/user-attachments/assets/31d4069c-8cc2-425c-a47b-4de89091ec61" />

## Secuity Tab
<img width="948" height="627" alt="Security Tab" src="https://github.com/user-attachments/assets/51d88e16-30dd-4a65-9073-10af670b7a80" />

## Alerts
<img width="930" height="547" alt="alert(1)" src="https://github.com/user-attachments/assets/cefc6c07-3511-432c-9f74-a3ad1a495938" />
<img width="941" height="581" alt="alert(2)" src="https://github.com/user-attachments/assets/0c9942d1-3e46-4266-a2ef-0a355d57dc8b" />
<img width="945" height="571" alt="alert(3)" src="https://github.com/user-attachments/assets/4cebfd89-8c8d-4468-a1ac-faf2df2b1598" />
<img width="939" height="530" alt="alert(4)" src="https://github.com/user-attachments/assets/673727c8-24ac-4e29-b4a7-0878215a7183" />
<img width="944" height="552" alt="alert(5)" src="https://github.com/user-attachments/assets/0ca814e2-7a71-4879-a877-b05f1d72c6c6" />
<img width="944" height="538" alt="alert(6)" src="https://github.com/user-attachments/assets/1b871a32-1218-4114-9365-f23563f19aa6" />

