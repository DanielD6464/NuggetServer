import json
import requests


resp = requests.get('https://api.macvendors.com/FC-A1-3E-2A-1C-3')
data = resp.json()
print(data)



# <?php
#   $mac_address = "FC:FB:FB:01:FA:21";

#   $url = "https://api.macvendors.com/" . urlencode($mac_address);
#   $ch = curl_init();
#   curl_setopt($ch, CURLOPT_URL, $url);
#   curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
#   $response = curl_exec($ch);
#   if($response) {
#     echo "Vendor: $response";
#   } else {
#     echo "Not Found";
#   }
# ?>