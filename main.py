"""
JSON dosyasını Excel dosyasına çeviren basit bir script.
Kullanım: python main.py <json_dosyasi_yolu>
"""
import pandas as pd
import json
import sys
import os

def json_to_excel(json_path, output_path='output/converted.xlsx'):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Eğer data list of dict değilse, listeye çevir
        if not isinstance(data, list):
            data = [data]
        
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_excel(output_path, index=False)
        abs_path = os.path.abspath(output_path)
        print(f"✅ Excel dosyası başarıyla oluşturuldu!\nDosya yolu: {abs_path}")
    except FileNotFoundError:
        print(f"❌ JSON dosyası bulunamadı: {json_path}")
    except json.JSONDecodeError:
        print(f"❌ JSON dosyası okunurken hata oluştu. Lütfen dosyanın geçerli bir JSON olduğundan emin olun.")
    except Exception as e:
        print(f"❌ Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ Kullanım: python main.py <json_dosyasi_yolu>")
    else:
        json_path = sys.argv[1]
        json_to_excel(json_path)
