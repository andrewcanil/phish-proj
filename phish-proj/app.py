import streamlit as st
import email
import re
import requests
import pandas as pd

def extract_ips(text):
    # Regex for standard IPv4
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # Regex for standard and compressed IPv6
    ipv6_pattern = r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b|\b(?:[A-Fa-f0-9]{1,4}:)*:[A-Fa-f0-9]{1,4}\b'
    
    ipv4_matches = re.findall(ipv4_pattern, text)
    ipv6_matches = re.findall(ipv6_pattern, text)
    
    return ipv4_matches + ipv6_matches

# Cache results for 24 hours to protect API limits
@st.cache_data(ttl=86400, show_spinner=False) 
def get_geolocation(ip):
    # Using a free IP geolocation API
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response.get('status') == 'success':
            return response['lat'], response['lon'], response['country']
    except:
        pass
    return None, None, None

# Helper function to color-code the dataframe
def color_trust(val):
    if val == 'Low (Potential Spoof)':
        return 'color: #ff4b4b' # Streamlit Red
    elif val == 'High (Provider)':
        return 'color: #00cc96' # Streamlit Green
    return ''

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
        # Enumerate gives us the index to track the hop order (top to bottom)
        for hop_index, header in enumerate(received_headers):
            ips = extract_ips(header)
            for ip in ips:
                # Filter out private/local IPv4 and IPv6 addresses
                local_prefixes = ('10.', '192.168.', '127.', '172.', '::1', 'fe80:', 'fc00:', 'fd00:')
                if not ip.startswith(local_prefixes):
                    lat, lon, country = get_geolocation(ip)
                    if lat and lon:
                        # Simple Trust Heuristic: The first 2 hops (top of the header) are usually your own provider
                        trust_level = "High (Provider)" if hop_index < 2 else "Low (Potential Spoof)"
                        
                        locations.append({
                            "Hop": hop_index + 1, 
                            "Trust Level": trust_level,
                            "IP": ip, 
                            "Country": country,
                            "lat": lat, 
                            "lon": lon
                        })
        
        if locations:
            df = pd.DataFrame(locations)
            
            # Apply color coding to the DataFrame
            styled_df = df[['Hop', 'Trust Level', 'IP', 'Country']].style.map(color_trust, subset=['Trust Level'])
            st.dataframe(styled_df, use_container_width=True)
            
            # Automatically plots the lat/lon on a world map
            st.map(df) 
        else:
            st.warning("No public IP routes found to map.")
