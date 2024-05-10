from stegano import lsb

def encode_with_key(input_path, output_path, message, key):
    file = lsb.hide(input_path, message, key)
    file.save(output_path)

def encode_without_key(input_path, output_path, message):
    file = lsb.hide(input_path, message)
    file.save(output_path)

def decode_with_key(path, key):
    file = lsb.reveal(path, key)
    return file

def decode_without_key(path):
    file = lsb.reveal(path)
    return