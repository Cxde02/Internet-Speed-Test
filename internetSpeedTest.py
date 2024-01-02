import speedtest

# Create a Speedtest object
st = speedtest.Speedtest()

# Download speed in Mbps
download_speed = st.download() / 1000000
print("Download Speed:", f"{download_speed:.2f} Mbps")

# Upload speed in Mbps
upload_speed = st.upload() / 1000000
print("Upload Speed:", f"{upload_speed:.2f} Mbps")
