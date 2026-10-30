import http.server
import json
import os
import shutil
import urllib.parse
import re

PORT = 8000
TARGET_FILE = 'gemini-code-1793329826677.html'
DATA_FILE = 'signature-data.json'
BACKUP_FILE = 'signature-editor.html.bak'

os.makedirs(os.path.dirname(TARGET_FILE) if os.path.dirname(TARGET_FILE) else '.', exist_ok=True)

DEFAULT_DATA = {
    "salutation": "Trân trọng/Best Regards,",
    "name": "Trần Khánh Linh",
    "title": "(Ms.)",
    "position_vn": "Trưởng phòng Cung ứng",
    "position_en": "Head of Procurement",
    "company_vn": "CÔNG TY CỔ PHẦN BILCO",
    "company_en": "Bilco Joint Stock Company",
    "address": "Số M1-25, KĐT Vinhomes Grand Park, Đường Phước Thiện, Phường Long Bình, Thành phố Hồ Chí Minh, Việt Nam.",
    "website": "www.bilco.com.vn",
    "hotline": "+84 933 77 63 88",
    "mobile": "+84 934 74 91 91",
    "email": "linhtk@bilco.com.vn",
    "logo_url": "https://i.pinimg.com/236x/4b/8f/26/4b8f265201569bbcf13f76127a5c0277.jpg"
}

def clean_phone(phone_str):
    if not phone_str:
        return ""
    return re.sub(r'[^\d+]', '', phone_str)

def generate_signature_html(data):
    salutation = (data.get("salutation") or DEFAULT_DATA["salutation"]).strip()
    name = (data.get("name") or DEFAULT_DATA["name"]).strip()
    title = (data.get("title") or "").strip()
    position_vn = (data.get("position_vn") or data.get("position") or DEFAULT_DATA["position_vn"]).strip()
    position_en = (data.get("position_en") or DEFAULT_DATA["position_en"]).strip()
    company_vn = (data.get("company_vn") or data.get("company") or DEFAULT_DATA["company_vn"]).strip()
    company_en = (data.get("company_en") or DEFAULT_DATA["company_en"]).strip()
    address = (data.get("address") or DEFAULT_DATA["address"]).strip()
    website = (data.get("website") or DEFAULT_DATA["website"]).strip()
    hotline = (data.get("hotline") or DEFAULT_DATA["hotline"]).strip()
    mobile = (data.get("mobile") or data.get("phone") or DEFAULT_DATA["mobile"]).strip()
    email = (data.get("email") or DEFAULT_DATA["email"]).strip()
    logo_url = (data.get("logo_url") or DEFAULT_DATA["logo_url"]).strip()

    website_url = website if website.startswith(('http://', 'https://')) else f'https://{website}'
    hotline_clean = clean_phone(hotline)
    mobile_clean = clean_phone(mobile)
    maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(address)}"

    name_display = name
    if title:
        title_clean = title if title.startswith('(') else f'({title})'
        name_display = f'{name} <span style="font-weight: bold; font-size: 14px; color: #54381e;">{title_clean}</span>'

    position_parts = []
    if position_vn:
        position_parts.append(f'<span style="font-style: italic; font-weight: bold; color: #54381e;">{position_vn}</span>')
    if position_en:
        position_parts.append(f'<span style="font-style: italic; font-weight: normal; color: #54381e;">{position_en}</span>')
    position_html = " | ".join(position_parts)

    company_parts = []
    if company_vn:
        company_parts.append(f'<strong style="font-weight: bold; letter-spacing: 0.3px; color: #54381e;">{company_vn}</strong>')
    if company_en:
        company_parts.append(f'<span style="font-style: italic; color: #54381e;">{company_en}</span>')
    company_html = " | ".join(company_parts)

    contact_row1_parts = []
    if website:
        contact_row1_parts.append(f'<strong style="color: #333333;">Website:</strong> <a href="{website_url}" target="_blank" style="color: #0b5cab; text-decoration: underline; font-family: \'Times New Roman\', Times, serif;">{website}</a>')
    if hotline:
        contact_row1_parts.append(f'<strong style="color: #333333;">Hotline:</strong> <a href="tel:{hotline_clean}" style="color: #333333; text-decoration: none; font-family: \'Times New Roman\', Times, serif;">{hotline}</a>')
    contact_row1_html = " | ".join(contact_row1_parts)

    contact_row2_parts = []
    if mobile:
        contact_row2_parts.append(f'<strong style="color: #333333;">Mobile:</strong> <a href="tel:{mobile_clean}" style="color: #333333; text-decoration: none; font-family: \'Times New Roman\', Times, serif;">{mobile}</a>')
    if email:
        contact_row2_parts.append(f'<strong style="color: #333333;">Email:</strong> <a href="mailto:{email}" style="color: #0b5cab; text-decoration: underline; font-style: italic; font-family: \'Times New Roman\', Times, serif;">{email}</a>')
    contact_row2_html = " | ".join(contact_row2_parts)

    html = f'''<div style="font-family: 'Times New Roman', Times, serif; font-size: 13px; color: #333333; line-height: 1.4;">
  {f'<p style="font-family: \'Times New Roman\', Times, serif; font-size: 13px; font-style: italic; color: #333333; margin: 0 0 14px 0; padding: 0;">{salutation}</p>' if salutation else ''}
  <table cellpadding="0" cellspacing="0" border="0" style="font-family: 'Times New Roman', Times, serif; font-size: 13px; line-height: 1.4; border-collapse: collapse;">
    <tr>
      <!-- CỘT 1: LOGO BILCO -->
      <td valign="middle" align="center" style="padding: 0 18px 0 0; border-right: 1.5px solid #54381e; vertical-align: middle; text-align: center; width: 140px;">
        <a href="{website_url}" target="_blank" style="text-decoration: none; display: inline-block;">
          <img src="{logo_url}" alt="BILCO" width="130" style="display: block; border: 0; width: 130px; height: auto; max-width: 130px;" />
        </a>
      </td>
      
      <!-- CỘT 2: THÔNG TIN CÁ NHÂN & CÔNG TY -->
      <td valign="top" style="padding: 0 0 0 18px; vertical-align: top;">
        <!-- HỌ TÊN VÀ CHỨC DANH -->
        <table cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td style="font-family: 'Times New Roman', Times, serif; font-size: 15px; font-weight: bold; color: #54381e; line-height: 1.2;">
              {name_display}
            </td>
          </tr>
          {f'<tr><td style="font-family: \'Times New Roman\', Times, serif; font-size: 13px; color: #54381e; padding-top: 3px; padding-bottom: 10px; line-height: 1.2;">{position_html}</td></tr>' if position_html else ''}
        </table>

        <!-- THÔNG TIN DOANH NGHIỆP & LIÊN HỆ -->
        <table cellpadding="0" cellspacing="0" border="0" style="font-family: 'Times New Roman', Times, serif; font-size: 12px; color: #333333; line-height: 1.5;">
          {f'<tr><td style="font-family: \'Times New Roman\', Times, serif; font-size: 13px; color: #54381e; padding-bottom: 4px;">{company_html}</td></tr>' if company_html else ''}
          {f'<tr><td style="font-family: \'Times New Roman\', Times, serif; padding-bottom: 3px; color: #333333;"><strong style="color: #333333;">Địa chỉ/Address:</strong> <a href="{maps_url}" target="_blank" rel="noopener noreferrer" title="Xem trên Google Maps" style="color: #333333; text-decoration: none; font-style: italic; font-family: \'Times New Roman\', Times, serif;"><span style="color: #333333; text-decoration: none; font-style: italic;">{address}</span></a></td></tr>' if address else ''}
          {f'<tr><td style="font-family: \'Times New Roman\', Times, serif; padding-bottom: 3px; color: #333333;">{contact_row1_html}</td></tr>' if contact_row1_html else ''}
          {f'<tr><td style="font-family: \'Times New Roman\', Times, serif; color: #333333;">{contact_row2_html}</td></tr>' if contact_row2_html else ''}
        </table>
      </td>
    </tr>
  </table>
</div>'''
    return html

class SignatureHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        clean_path = urllib.parse.urlparse(self.path).path
        if clean_path in ("/", "/index.html", "/signature-editor.html"):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            file_to_open = "index.html" if os.path.exists("index.html") else "signature-editor.html"
            with open(file_to_open, "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        elif clean_path in ("/favicon.ico", "/favicon.png", "/qr-donate.jpg"):
            target_path = clean_path.lstrip("/")
            if os.path.exists(target_path):
                self.send_response(200)
                content_type = "image/jpeg" if target_path.endswith((".jpg", ".jpeg")) else ("image/png" if target_path.endswith(".png") else "image/x-icon")
                self.send_header("Content-type", content_type)
                self.end_headers()
                with open(target_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Not found")
        elif clean_path == "/api/signature":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            if os.path.exists(TARGET_FILE):
                with open(TARGET_FILE, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            else:
                default_html = generate_signature_html(DEFAULT_DATA)
                self.wfile.write(default_html.encode("utf-8"))
        elif clean_path == "/api/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            saved_data = DEFAULT_DATA.copy()
            if os.path.exists(DATA_FILE):
                try:
                    with open(DATA_FILE, "r", encoding="utf-8") as f:
                        saved_data.update(json.load(f))
                except Exception:
                    pass
            self.wfile.write(json.dumps(saved_data, ensure_ascii=False).encode("utf-8"))
        else:
            self.send_error(404, "Not found")

    def do_POST(self):
        clean_path = urllib.parse.urlparse(self.path).path
        if clean_path == "/api/save":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode("utf-8"))
                sig_html = generate_signature_html(data)
                
                with open(TARGET_FILE, "w", encoding="utf-8") as f:
                    f.write(sig_html)
                
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                shutil.copy2(TARGET_FILE, BACKUP_FILE)
                
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "Lưu chữ ký thành công!"}, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "message": str(e)}, ensure_ascii=False).encode("utf-8"))
        else:
            self.send_error(404, "Not found")

if __name__ == "__main__":
    if not os.path.exists(TARGET_FILE) or not os.path.exists(DATA_FILE):
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(generate_signature_html(DEFAULT_DATA))
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_DATA, f, ensure_ascii=False, indent=2)

    with http.server.HTTPServer(("", PORT), SignatureHandler) as httpd:
        print("Server running at: http://localhost:" + str(PORT))
        print("Target file: " + TARGET_FILE)
        print("Open browser at: http://localhost:8000")
        httpd.serve_forever()
