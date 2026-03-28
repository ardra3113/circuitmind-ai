import qrcode

# 🔗 Paste your ngrok link here
url = "https://abcd1234.ngrok.io"

# Generate QR
qr = qrcode.make(url)

# Save image
qr.save("circuitmind_qr.png")

print("✅ QR Code Generated Successfully!")