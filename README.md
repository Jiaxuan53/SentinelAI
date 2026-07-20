# SentinelAI - AI Risk Detection & Incident Prediction Module

## Overview

SentinelAI is an AI-driven security intelligence module designed to detect abnormal behaviours, identify potential security threats, calculate risk levels, and predict possible future incidents from enterprise activity logs.

With the increasing adoption of Large Language Models (LLMs) and AI-powered applications, organizations face new security challenges such as token theft, prompt injection attacks, abnormal API usage, and unexpected financial costs.

This module provides an automated security analysis pipeline that transforms raw enterprise logs into actionable security insights using anomaly detection, risk scoring, explainable AI, and incident prediction techniques.

---

# Module Responsibility

This repository represents **Member 1's AI Risk Detection and Incident Prediction Module**.

The module is responsible for:

- Generating enterprise security activity logs
- Performing log mining and feature extraction
- Detecting abnormal user behaviour using machine learning
- Calculating security risk scores
- Explaining detected threats
- Predicting possible future security incidents
- Providing recommended remediation actions

---

# System Workflow

The complete AI pipeline follows the workflow below:

Enterprise Logs
        |
        v
Log Mining & Feature Engineering
        |
        v
Machine Learning Anomaly Detection
        |
        v
Risk Score Generation
        |
        v
Explainable AI Analysis
        |
        v
Incident Prediction
        |
        v
Security Recommendations



---

# Features

## 1. Enterprise Log Generation

The system generates simulated enterprise activity logs containing both normal and malicious behaviours.

Generated scenarios include:

### Normal Activity

Represents regular employee behaviour:

- Normal API requests
- Stable session duration
- Normal cost consumption
- Trusted devices


### Token Theft Attack

Simulates unauthorized token usage:

Indicators:

- Extremely high API requests
- Multiple IP access
- Abnormal geographical locations
- Suspicious device usage


### Prompt Injection Attack

Simulates malicious LLM interactions:

Indicators:

- Extremely long prompts
- Suspicious prompt patterns
- AI instruction manipulation attempts


### Financial Abuse Attack

Simulates excessive AI service consumption:

Indicators:

- Abnormal API cost
- High resource usage
- Unexpected spending increase


### Account Compromise Attack

Simulates compromised user accounts:

Indicators:

- Multiple failed login attempts
- Unknown devices
- Suspicious login behaviour


---

# 2. Feature Engineering

Raw logs are converted into machine learning features.

Extracted features include:

| Feature | Description |
|---------|-------------|
| api_requests_last_minute | Number of API requests within one minute |
| estimated_cost | Estimated AI service cost consumption |
| failed_login_attempts | Number of unsuccessful login attempts |
| session_duration | Length of user session |
| prompt_length | Length of user prompt input |
| unique_ip_count | Number of different IP addresses accessing the service |
| prompt_injection | Indicator of suspicious prompt injection behaviour |


Output: data/features.csv


---

# 3. AI-Based Anomaly Detection

## Model Used

Isolation Forest


## Why Isolation Forest?

Isolation Forest is an unsupervised machine learning algorithm suitable for security anomaly detection because:

- It does not require large labelled datasets
- It identifies unusual behaviour patterns
- It is efficient for large-scale log analysis


The model analyses user behaviour patterns and identifies activities that significantly differ from normal behaviour.


Output:data/prediction_results.csv



Generated information:

- Prediction result
- Risk score
- Detected attack type


---

# 4. Risk Scoring

The system converts anomaly detection results into a risk score ranging from 0 to 100.


Example:

| Risk Score | Risk Level |
|------------|------------|
| 0 - 30 | Low |
| 30 - 70 | Medium |
| 70 - 100 | High |


Higher scores indicate higher possibility of security threats.

---

# 5. Explainable AI Engine

The Explainable AI module provides reasons behind detected risks.

Instead of only showing: Attack Detected


the system explains:

Example:
Threat:
Token Theft
Reasons:
High API request frequency detected
Token accessed from multiple IP addresses
Recommended Action:
Revoke compromised token
Terminate active sessions



This improves security decision-making by providing understandable explanations.

---

# 6. Incident Prediction

The incident prediction module estimates the possibility of future security incidents based on current risk behaviour.


Example output:
Incident Probability:
95%
Predicted Incident:
Possible Token Theft Incident
Reason:
Unauthorized API access behaviour detected



Supported predictions:

- Possible Token Theft Incident
- Possible AI Security Incident
- Possible Financial Risk Incident
- Possible Account Security Incident



---

# Technologies Used

## Programming Language

- Python


## Data Processing

- Pandas


## Machine Learning

- Scikit-learn
- Isolation Forest


## Model Management

- Joblib


---

# Installation

Clone this repository:

```bash
git clone https://github.com/Jiaxuan53/SentinelAI.git
