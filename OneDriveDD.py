import base64
import setting

input_url = setting.onedrive_url

def create_onedrive_directdownload (onedrive_link):
    data_bytes64 = base64.b64encode(bytes(onedrive_link, 'utf-8'))
    data_bytes64_String = data_bytes64.decode('utf-8').replace('/','_').replace('+','-').rstrip("=")
    resultUrl = f"https://api.onedrive.com/v1.0/shares/u!{data_bytes64_String}/root/content"
    print(f"Direct OneDrive Download Link : {resultUrl}")
    return resultUrl

create_onedrive_directdownload(input_url)
