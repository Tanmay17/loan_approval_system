# Loan Approval System

## Overview
A simplified, scalable loan approval system that evaluates loan applications, calculates risk, and approves or rejects applications based on predefined criteria.

## Features
- Loan application submission
- Risk assessment based on credit score, debt-to-income ratio, employment status, etc.
- Loan approval or rejection based on risk score and predefined criteria
- RESTful API for submitting and checking loan applications
- Queue-based architecture using RabbitMQ
- Data storage using MongoDB
- Monitoring and logging mechanisms
- Unit and integration tests

## Setup

### Prerequisites
- Python 3.8+
- MongoDB
- RabbitMQ

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Tanmay17/loan_approval_system.git
    cd loan_approval_system
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Start MongoDB and RabbitMQ:
    ```sh
    docker-compose up -d
    ```

### Running the Application
```sh
uvicorn app.main:app --reload
