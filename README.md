# AMal - Anti-Malware Indicator Feed

## 1. What is AMal?
**A**nti-**Mal**ware (**AMal**) is a community-driven cybersecurity project designed to block and blacklist C2 servers, malware delivery payloads, phishing domains, and malicious web infrastructure.

## 2. How does it work?
We actively analyze malware families (Amadey, DanaBot, etc.) to extract active, online indicators of compromise (IOCs). Additionally, the community can submit verified entries via GitHub Issues or Pull Requests.

## 3. What do we filter?
We target confirmed malicious infrastructure, defacements, and threat hosts.

**Examples:**
* `hxxps://scamwebsite[dot]com/please-fetch-me.exe` (Malware Payload)
* `hxxps://scamwebsite[dot]com/` (Active C2 / Phishing Landing Page)

Legitimate software downloads (e.g., game installers) are never flagged unless verified malicious through detailed analysis. Optional feeds for click-trackers and potentially unwanted programs (PUPs) are also maintained separately.

## 4. How do I use it?
AMal acts as a simple, open JSON API. Send a standard `GET` request to retrieve the full, validated indicator feed:

GET https://raw.githubusercontent.com/dll-cybersecurity/AMal/main/data/indicators.json

## 5. Update Frequency
The IOC list is updated dynamically as new threats are verified by our team and contributors. If you employ custom allowlists, configure your automated integration scripts accordingly.

## 6. How do I contribute?
Public IOCs & Bug Reports: Please submit a new report using the GitHub Issues tab.
Sensitive Disclosures: For confidential submissions or false-positive reports, contact us directly at abuse-report31@proton.me.
Please reserve the contact email strictly for verified security reports.

Stay safe and happy hunting!
