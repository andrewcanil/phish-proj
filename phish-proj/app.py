import streamlit as st
import email
import re
import requests
import pandas as pd

def extract_ips(text):
    # Regex to find standard IPv4 addresses
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)

def get_geolocation(ip):
    # Using a free IP geolocation API
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            return response['lat'], response['lon'], response['country']
    except:
        pass
    return None, None, None

st.title("Phish-Catch: Email Header Analyzer")

# User Input
raw_header = st.text_area("Paste Raw Email Header Here:", height=200)

if st.button("Analyze Header"):
    if raw_header:
        # Parse the header
        msg = email.message_from_string(raw_header)
        
        st.subheader("1. Authentication Results")
        auth_results = msg.get("Authentication-Results", "Not Found")
        st.code(auth_results)
        
        st.subheader("2. Routing Map (Received Hops)")
        received_headers = msg.get_all("Received", [])
        
        locations = []
        for header in received_headers:
            ips = extract_ips(header)
            for ip in ips:
                # Filter out private/local IPs
                if not ip.startswith(('10.', '192.168.', '127.', '172.')):
                    lat, lon, country = get_geolocation(ip)
                    if lat and lon:
                        locations.append({"lat": lat, "lon": lon, "IP": ip, "Country": country})
        
        if locations:
            df = pd.DataFrame(locations)
            st.dataframe(df[['IP', 'Country']])
            st.map(df) # Automatically plots the lat/lon on a world map!
        else:
            st.warning("No public IP routes found to map.")