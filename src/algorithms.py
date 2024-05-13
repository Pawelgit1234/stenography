from stegano import lsb
import hashlib

def get_key(raw_key: str) -> int:
    m = hashlib.sha256()
    m.update(raw_key.encode())
    return m.hexdigest().count("a")

def encode_with_key(input_path, output_path, message, key):
    file = lsb.hide(input_path, message, shift=get_key(key))
    file.save(output_path)

def encode_without_key(input_path, output_path, message):
    file = lsb.hide(input_path, message)
    file.save(output_path)

def decode_with_key(path, key):
    msg = lsb.reveal(path, shift=get_key(key))
    return msg

def decode_without_key(path):
    msg = lsb.reveal(path)
    return msg