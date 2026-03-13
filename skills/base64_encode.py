import sys, base64
text = sys.argv[1]
encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
print(encoded)