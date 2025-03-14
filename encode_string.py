import base64

def encode_base32(s):
    s = base64.b32encode(s.encode()).decode().rstrip('=')
    s = s.lower()
    return s

def decode_base32(s):
    s = s.upper()
    # Se o comprimento já for múltiplo de 8, não adiciona padding
    if len(s) % 8 != 0:
        s += '=' * (8 - len(s) % 8)
    return base64.b32decode(s).decode()
