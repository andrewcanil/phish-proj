# 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Frontend Framework:** Streamlit  
- **Data Processing:** Pandas, Regex (`re`), Python `email` library  
- **External API:** ip-api (for IP Geolocation)  

---

# 🚀 Run Locally

## 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

## 2️⃣ Install Dependencies

Make sure you have **Python 3.x** installed. Then install the required libraries:

```bash
pip install -r requirements.txt
```

*(If requirements.txt is not available, manually install: streamlit, pandas, requests, etc.)*

## 3️⃣ Start the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser at:

```
http://localhost:8501
```

---

# 📖 How to Use

1. Open any suspicious email in your inbox (e.g., Gmail).  
2. Click the **three-dot menu** and select **"Show original"** or **"View raw message"**.  
3. Copy the entire block of raw text.  
4. Paste the text into the **Phish-Catch** input box.  
5. Click **"Analyze Header"**.  
6. Review the **authentication scorecard** and the **interactive map** to determine the email's legitimacy.

---

# 🔮 Future Enhancements

- 🤖 **Machine Learning Integration**  
  Train a model to classify phishing probability based on specific header anomalies.

- 🌐 **Domain Reputation Check**  
  Integrate the VirusTotal API to automatically flag known malicious IP addresses.

- 📄 **Export to PDF**  
  Allow users to download a formal forensic report of the analyzed email.

---

# ⚠️ Disclaimer

This tool relies on public IP routing. Internal network hops (e.g., `10.x.x.x`, `192.168.x.x`) are intentionally filtered out as they cannot be geographically mapped.

---

# 📜 License

Distributed under the **MIT License**.
