import os
import base64
import sys
import shutil

filename = '../prog/main.py'
filedir = '../prog'
chmod = 711

main_py = 'aW1wb3J0IHN5cwppbXBvcnQgb3MKCmZpbGVuYW1lID0gJ25hbWVzLnR4dCcKczNjcjN0X2ZpbGVuYW1lID0gJy4uL25ldmVyL2V2ZXIvb3Blbi90aGlzL2ZvbGRlci9wcm9nX2xpbWl0cy5pbmknCgppZiBub3Qgb3MucGF0aC5leGlzdHMoZmlsZW5hbWUpOgogICAgZiA9IG9wZW4oZmlsZW5hbWUsICd3KycpCiAgICBmLmNsb3NlKCkKd2l0aCBvcGVuIChzM2NyM3RfZmlsZW5hbWUsICdyKycpIGFzIGwsIG9wZW4oZmlsZW5hbWUsICdyKycpIGFzIGQ6CiAgICBsaW1pdCA9IGludChsLnJlYWRsaW5lKCkpCiAgICBjdXJyZW50ID0gaW50KGwucmVhZGxpbmUoKSkKICAgIGlmIGN1cnJlbnQgPCBsaW1pdDoKICAgICAgICBuYW1lID0gc3RyKGlucHV0KCdFbnRlciB5b3VyIEZ1bGwgbmFtZTogJykpCiAgICAgICAgZGF0YSA9IGQucmVhZCgpCiAgICAgICAgaWYgbmFtZSBpbiBkYXRhLnNwbGl0bGluZXMoKToKICAgICAgICAgICAgcHJpbnQoJ1lvdXIgbmFtZTogJXMgaXMgYWxyZWFkeSBlbnRlcmVkIGluIHRoZSBsaXN0JyAlbmFtZSkKICAgICAgICBlbHNlOgogICAgICAgICAgICBkLndyaXRlKG5hbWUgKyAnXG4nKQogICAgICAgICAgICBwcmludCgnWW91ciBuYW1lOiAlcyBpcyBhZGRlZCB0byB0aGUgbGlzdCcgJW5hbWUpCiAgICAgICAgY3VycmVudCArPSAxCiAgICAgICAgbC5zZWVrKGxlbihzdHIobGltaXQpKSsxKQogICAgICAgIGwud3JpdGUoc3RyKGN1cnJlbnQpKQogICAgICAgIHByaW50KCdZb3VyIHByb2dyYW0gdXNhZ2UgbGltaXQgaXMgJWQsIHlvdXIgY3VycmVudCB1c2FnZSBpcyAlZCcgJSAobGltaXQsY3VycmVudCkpCiAgICBlbHNlOgogICAgICAgIHByaW50ICgnWW91ciB0cmlhbCBwZXJpb2QgaXMgb3ZlciwgcGxlYXNlIGJ1eSBmdWxsIHZlcnNpb24gb3IgZGVsZXRlIHRoZSBwcm9ncmFtJykKICAgICAgICBzeXMuZXhpdCgwKQ=='

s3cr3t_filename = '../never/ever/open/this/folder/prog_limits.ini'
s3cr3t_filedir = '../never/ever/open/this/folder'
s3cr3t_data = '10\n0'
s3cr3t_chmod = 700

if not os.path.exists(filename):
    install = str(input('Do you want to install the program y/n? '))
    if install.lower() == 'y' or install.lower() == 'yes':
        if not os.path.exists(s3cr3t_filename):
            os.makedirs(s3cr3t_filedir)
            with open(s3cr3t_filename, 'w+') as l:
                l.write(s3cr3t_data)
        os.system('chmod -R %d %s' %(s3cr3t_chmod,s3cr3t_filedir))
        os.makedirs(filedir)
        with open(filename, 'w+') as f:
            base64_message = main_py
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            f.write(message)
        shutil.copy(__file__, filedir)
        os.system('chmod -R %d %s' %(chmod,filedir))
        print('Program successfully installed.')
    else:
        sys.exit(0)
else:
    uninstall = str(input('Do you want to uninstall the program y/n? '))
    if uninstall.lower() == 'y' or uninstall.lower() ==  'yes':
        shutil.rmtree(filedir, ignore_errors = True)
        print('Program successfully unistalled.')
    else:
        sys.exit(0)