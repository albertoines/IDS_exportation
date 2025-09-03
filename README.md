# Centralized IOC Management System for NIDS

<p align="center">
  <img src="https://i.imgur.com/gK9vHh4.png" alt="Project Architecture Diagram" width="800"/>
</p>

<p align="center">
  <strong>Final Degree Project | University of Zaragoza</strong>
  <br />
  An automated system for detecting cyber threats on a network through centralized management of Indicators of Compromise (IOCs) and their export to Network Intrusion Detection Systems (NIDS).
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status: Completed">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.9+-yellowgreen" alt="Python">
  <img src="https://img.shields.io/badge/Shell-Bash-lightgrey" alt="Bash">
</p>

---

## 🇬🇧 Overview

This project implements a complete and automated infrastructure to enhance cybersecurity in home and SMB networks. The system collects threat intelligence (Indicators of Compromise - IOCs) from various open-source feeds, centralizes and processes them in a **MISP** instance, generates detection rules, and distributes them to Network Intrusion Detection Systems (**NIDS**) like **Suricata** and **Zeek**. Finally, all generated alerts are centralized and visualized in the **Elastic Stack (Kibana)** for efficient analysis.

The goal is to create a proactive, low-cost, and highly adaptable cybersecurity ecosystem capable of detecting real-time threats.

---

## 🚀 System Architecture

The system's workflow is fully automated and follows these steps:

1.  **Data Acquisition**: Python scripts periodically query threat intelligence feeds (Open Source Feeds and Twitter) to obtain new IOCs (IPs, domains, hashes, etc.).
2.  **Centralization and Management**: The IOCs are ingested and stored in **MISP (Malware Information Sharing Platform)**, which acts as the system's brain, managing the indicator lifecycle.
3.  **Rule Generation**: Daily, an automated process queries the MISP API to export active IOCs and converts them into native rule formats for **Suricata** and **Zeek**.
4.  **Rule Distribution**: The generated rules are pushed to a private GitHub repository, which serves as a secure and version-controlled distribution channel.
5.  **Deployment on NIDS**: The NIDS (deployed on a VM or Raspberry Pi) clone the repository to download and apply the latest rules.
6.  **Detection and Alerting**: **Suricata** and **Zeek** monitor network traffic. If a connection matches a rule, they generate an alert.
7.  **Log Centralization**: A **Filebeat** agent on the NIDS host collects the alerts (`eve.json`, `intel.log`) and securely sends them to **Elasticsearch**.
8.  **Visualization and Analysis**: **Kibana** connects to Elasticsearch to provide interactive dashboards, allowing an analyst to intuitively visualize and explore detected threats.

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **IOC Management** | <img src="https://www.misp-project.org/img/misp-logo.png" width=20/> **MISP** | Central platform to aggregate, correlate, and manage threat intelligence. |
| **Detection (NIDS)** | <img src="https://suricata.io/wp-content/uploads/2021/07/suricata-logo-1.png" width=20/> **Suricata** | Signature-based NIDS for detecting known attack patterns. |
| | <img src="https://zeek.org/wp-content/uploads/2021/08/zeek-logotype.png" width=20/> **Zeek** | Network analysis framework for flexible and in-depth traffic monitoring. |
| **Visualization** | <img src="https://static-www.elastic.co/v3/assets/bltefdd0b53724fa2ce/blt60184e63f3817163/5d091083995449557c63f2a1/logo-elastic-stack-lt.svg" width=20/> **Elastic Stack** | (Elasticsearch, Kibana, Filebeat) for ingesting, storing, and visualizing alerts. |
| **Automation** | 🐍 **Python** & `requests` | Scripts to interact with APIs (MISP, Twitter) and process data. |
| | 🐧 **Bash & Crontab** | For orchestrating and scheduling recurring tasks in the system. |
| **Infrastructure** | 📦 **Debian 11 (VMs)** | Server environment for deploying the main components. |
| | 🍓 **Raspberry Pi 4** | Demonstration of deployment in a real, low-cost home network environment. |
| **Distribution** | <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width=20/> **GitHub** | Private repository for versioning and secure distribution of rule files. |

## ✨ Key Features

*   ✅ **Fully Automated**: From IOC acquisition to alert visualization, the system operates without manual intervention thanks to `cron`.
*   ✅ **Multi-NIDS Support**: Simultaneous support for Suricata and Zeek, leveraging the strengths of each tool.
*   ✅ **Effective Centralization**: MISP as the single source of truth for IOCs and Elastic Stack for all generated alerts.
*   ✅ **Flexible and Scalable**: Easy to adapt to new IOC sources or deploy on larger networks.
*   ✅ **Open-Source Based**: Built entirely with open-source tools, making it accessible and free of licensing costs.
*   ✅ **Tested in Real Environments**: Validated in both a virtualized VM environment and a real home network using a Raspberry Pi 4.

## 🖼️ Results and Visualizations

Below are examples of the alerts and dashboards generated by the system.

#### Threat Detection in NIDS Logs
_Example of a malicious IP alert detected by **Suricata** (`fast.log`):_
```bash
08/28/2023-21:48:18.424819 [**] [1:275255421:1] MISP e2876 [] Outgoing To IP: 117.213.40.201 [**] [Classification: A Network Trojan was detected] [Priority: 4] {TCP} 192.168.153.2:52202 -> 117.213.40.201:80
```
Example of a malicious domain alert detected by Zeek (intel.log):
```JSON
{"ts":1693251968.906411, ..., "seen.indicator":"1105181.com", "seen.indicator_type":"Intel::DOMAIN", "seen.where":"DNS::IN_REQUEST", ...}
```
Dashboards in Kibana
Here you can insert screenshots of your Kibana dashboards.
Top Suricata Alerts:
<!-- ![Top Suricata Alerts](path/to/suricata_alerts_screenshot.png) -->
Network Traffic Detected by Zeek:
<!-- ![Zeek Traffic](path/to/zeek_traffic_screenshot.png) -->
Network Traffic Direction:
<!-- ![Traffic Direction](path/to/traffic_direction_screenshot.png) -->
🔧 Installation and Setup
The complete and detailed guide for installation and setup of each component can be found in the Appendices of the full Thesis Document:
Appendix E: MISP Installation.
Appendix F: Suricata and Zeek Installation.
Appendix G: Elastic Stack Installation and Configuration.
The automation scripts used in this project are available in this repository.
🔮 Future Work
Integrate more IOC feeds to enrich the MISP database.
Implement stricter IOC rotation policies (based on score) to improve efficiency.
Use IPS (Intrusion Prevention System) instead of NIDS to actively block detected threats.
Improve the security of rule transfer by exploring other protocols.
Create custom Kibana dashboards for deeper and more tailored analysis.
Author: Alberto Inés Medina
Supervisor: Álvaro Alesanco Iglesias
Degree: BSc in Telecommunication Technologies and Services Engineering
Institution: School of Engineering and Architecture, University of Zaragoza (2023)
