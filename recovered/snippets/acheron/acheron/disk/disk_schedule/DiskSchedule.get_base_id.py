# Source Generated with Decompyle++
# File: tmp3jju007n.marshal (Python 3.11)

json_string = self.model_dump_json()
hash_object = hashlib.sha256(json_string.encode())
return 'ds-' + hash_object.hexdigest()
