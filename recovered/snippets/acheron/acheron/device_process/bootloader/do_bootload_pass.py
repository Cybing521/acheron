# Source Generated with Decompyle++
# File: tmp0e17_6vs.marshal (Python 3.11)

done_bytes = 0
for page_info in firm_data['data']:
    page_number = page_info[0]
    nonce = binascii.a2b_hex(page_info[1])
    page_data = binascii.a2b_hex(page_info[2])
    digest = binascii.a2b_hex(page_info[3])
    message = 'Writing Page {}'.format(page_number)
    callback(done_bytes, total_bytes, message)
    device.start_bootloader_page(page_number, nonce)
    device.verify_bootloader_page(digest)
    different = False
except asphodel.AsphodelError:
    e = None
    if e.args[1] == 'ERROR_CODE_INVALID_DATA':
        different = True
    else:
        raise 
    e = None
    del e
except:
    e = None
    del e
if different:
    device.start_bootloader_page(page_number, nonce)
    do_bootload_page(device, done_bytes, page_data, block_sizes, total_bytes, message, callback)
    device.finish_bootloader_page(digest)
done_bytes += len(page_data)
continue
for page_info in firm_data['data']:
    page_number = page_info[0]
    nonce = binascii.a2b_hex(page_info[1])
    digest = binascii.a2b_hex(page_info[3])
    message = 'Verifying Page {}'.format(page_number)
    callback(done_bytes, total_bytes, message)
    device.start_bootloader_page(page_number, nonce)
    device.verify_bootloader_page(digest)
    done_bytes += verify_size
    return None
