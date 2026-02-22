🛠️ Tech Stack
Language: Python 3.x

Frontend Framework: Streamlit

Data Processing: Pandas, Regex (re), Python email library

External API: ip-api (for IP Geolocation)

🚀 Run Locally
1. Clone the repository
2. Install dependencies
Make sure you have Python installed. Then, install the required libraries:

3. Start the application
The application will open automatically in your default web browser at http://localhost:8501.

📖 How to Use
Open any suspicious email in your inbox (e.g., Gmail).

Click the three-dot menu and select "Show original" or "View raw message".

Copy the entire block of raw text.

Paste the text into the Phish-Catch input box and click "Analyze Header".

Review the authentication scorecard and the interactive map to determine the email's legitimacy.

🔮 Future Enhancements
Machine Learning Integration: Train a model to classify phishing probability based on specific header anomalies.

Domain Reputation Check: Integrate the VirusTotal API to automatically flag known malicious IP addresses.

Export to PDF: Allow users to download a formal forensic report of the analyzed email.

⚠️ Disclaimer
This tool relies on public IP routing. Internal network hops (e.g., 10.x.x.x, 192.168.x.x) are intentionally filtered out as they cannot be geographically mapped.

📜 License
Distributed under the MIT License.
