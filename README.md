# Business-Analysis-Agent
# 🧠 Agentic Business Surveillance & Decision Intelligence System

> An AI-driven decision intelligence platform that autonomously monitors business operations, detects risks, simulates outcomes, and assists managers with explainable, data-driven decisions.

Designed for multiple business domains — **e-commerce, food delivery, logistics, and marketplaces** — using a modular multi-agent architecture.

---

## 🚨 Problem Statement

Modern organizations rely heavily on dashboards and reports, but:

- Decision-making is **manual, slow, and reactive**
- Early warning signals are **hidden across multiple data sources**
- Managers often need only **specific insights**, not full system analysis

This project solves that by introducing an Agentic AI system that:

✅ Continuously monitors business data  
✅ Activates only the required agents  
✅ Produces human-readable executive insights  
✅ Supports natural-language decision queries  

---

## 💡 Solution Overview

The system uses **independent AI agents**, each responsible for a specific business intelligence task. Agents collaborate via a shared evolving state, enabling scalability and explainability.

### Core Capabilities

| Capability | Description |
|---|---|
| 🔍 Risk Surveillance | Detect abnormal seller or product behavior |
| 🧠 Root Cause Analysis | Explain why issues occurred |
| 🔄 Vendor Recommendations | Identify better alternatives |
| 📈 Demand Intelligence | Detect fast/slow-moving products |
| 📦 Inventory Risk Prediction | Predict stock-outs before they occur |
| 💰 Vendor Price Optimization | Recommend cost-effective vendors |
| 💬 Decision Chatbot | Answer natural-language business queries |

---

## 🏗️ Agentic Architecture

### Reactive Agents (Core)

| Agent | Role |
|---|---|
| **Surveillance Agent** | Detects abnormal seller or product behavior using orders and reviews |
| **Analysis Agent** | Explains why the issue occurred (severity, reasoning) |
| **Alternatives Agent** | Identifies better vendors offering similar quality or pricing |
| **Decision Agent** | Recommends actions with confidence scoring |
| **Business Analysis Agent** | Generates a pure-text executive summary for managers |

### Proactive Intelligence Agents

| Agent | Role |
|---|---|
| **Demand Intelligence Agent** | Detects fast-moving or slow-moving products |
| **Inventory Alert Agent** | Predicts potential stock-out risks before they occur |
| **Vendor Optimization Agent** | Recommends cost-effective vendors without quality loss |

### Conversational Layer

**Business Chat Agent** — Acts as a Decision Analyst, answering natural-language questions such as:
- *"What is the current risk?"*
- *"Why was this seller suspended?"*
- *"What happens if we delay action?"*
- *"Which vendor should we switch to?"*

---

## 🎯 Key Innovation — Agent Selection Layer

Not all scenarios require all agents. The system **intelligently activates only the relevant agents**, avoiding unnecessary computation.

| Role | Agents Activated |
|---|---|
| Chef | Review insights only |
| Supply Manager | Inventory & alternatives |
| Executive | Business summary |

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas |
| Architecture | Modular Agentic Workflow |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
Business Analysis Agent/
│
├── app.py
├── workflow/
│   └── orchestrator.py
├── agents/
│   ├── agent1_surveillance.py
│   ├── agent2_analysis.py
│   ├── agent3_alternatives.py
│   ├── agent4_decision.py
│   ├── business_analysis_agent.py
│   ├── demand_intelligence_agent.py
│   ├── inventory_alert_agent.py
│   └── vendor_price_optimization_agent.py
│
├── data/
│   ├── orders.csv
│   ├── reviews.csv
│   ├── sellers.csv
│   └── inventory.csv
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run app.py
```

### 3. Upload CSV Files

When prompted, upload your data files:
- `orders.csv` — Order transaction data
- `reviews.csv` — Customer reviews data
- `sellers.csv` — Seller/vendor data
- `inventory.csv` — Inventory stock data

---

## 📊 Output Highlights

- 📊 **Executive Summary** — Natural language business report
- ⚠️ **Risk Alerts** — Real-time anomaly detection
- 🔄 **Vendor Alternatives** — Smart replacement suggestions
- 📈 **Demand Insights** — Trend detection across products
- 📦 **Inventory Alerts** — Proactive stock-out warnings
- 💬 **Conversational Decision Support** — Chat-based query resolution

---

## 🌍 Real-World Impact

- ⚡ Faster decision-making
- 🛡️ Reduced operational risk
- 📦 Proactive inventory management
- 😊 Improved customer satisfaction
- 🔗 Scalable across industries


Note

This project demonstrates how **Agentic AI systems** can move businesses from reactive dashboards to **autonomous, explainable decision intelligence**.
