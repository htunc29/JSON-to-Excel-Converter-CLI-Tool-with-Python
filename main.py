"""
JSON dosyasını Excel dosyasına çeviren basit bir script.
Kullanım: python main.py <json_dosyasi_yolu>
"""
import pandas as pd
import json
import sys
import os
import traceback

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
except Exception:
    tk = None
    filedialog = None
    messagebox = None

def json_to_excel(json_path, output_path='output/converted.xlsx'):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
      
        if not isinstance(data, list):
            data = [data]
        
        df = pd.DataFrame(data)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_excel(output_path, index=False)
        abs_path = os.path.abspath(output_path)
        print(f"✅ Harika Excel dosyası başarıyla oluşturuldu!\n 📁 Dosya yolu: {abs_path}")
        return abs_path
    except FileNotFoundError:
        print(f"❌😢 JSON dosyası bulunamadı: {json_path}")
        raise
    except json.JSONDecodeError:
        print(f"❌😢 JSON dosyasını okurken hata oluştu. Lütfen dosyanın geçerli bir JSON olduğundan emin olun.")
        raise
    except Exception as e:
        print(f"❌🤷 Beklenmeyen bir hata oluştu: {e}")
        traceback.print_exc()
        raise


def launch_gui():
    if tk is None:
        print("❌ GUI başlatılamadı: tkinter bulunamadı.")
        return

    window = tk.Tk()
    window.title("JSON ➜ Excel Dönüştürücü")
    window.geometry("520x220")

    lbl_in = tk.Label(window, text="JSON Dosyası:")
    lbl_in.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    in_var = tk.StringVar()
    ent_in = tk.Entry(window, textvariable=in_var, width=50)
    ent_in.grid(row=0, column=1, padx=10, pady=10, sticky="we")

    def select_in():
        path = filedialog.askopenfilename(title="JSON dosyası seçin", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if path:
            in_var.set(path)

    btn_in = tk.Button(window, text="Seç", command=select_in)
    btn_in.grid(row=0, column=2, padx=10, pady=10)

    lbl_out = tk.Label(window, text="Çıktı (xlsx):")
    lbl_out.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    out_var = tk.StringVar(value=os.path.join("output", "converted.xlsx"))
    ent_out = tk.Entry(window, textvariable=out_var, width=50)
    ent_out.grid(row=1, column=1, padx=10, pady=10, sticky="we")

    def select_out():
        initialdir = os.path.abspath("output")
        os.makedirs(initialdir, exist_ok=True)
        path = filedialog.asksaveasfilename(title="Çıktı dosyası", defaultextension=".xlsx", initialdir=initialdir, filetypes=[("Excel", "*.xlsx")])
        if path:
            out_var.set(path)

    btn_out = tk.Button(window, text="Seç", command=select_out)
    btn_out.grid(row=1, column=2, padx=10, pady=10)

    status_var = tk.StringVar(value="Hazır")
    lbl_status = tk.Label(window, textvariable=status_var, fg="gray")
    lbl_status.grid(row=3, column=0, columnspan=3, padx=10, pady=(5, 0), sticky="w")

    def run_convert():
        src = in_var.get().strip()
        dst = out_var.get().strip()
        if not src:
            messagebox.showwarning("Uyarı", "Lütfen bir JSON dosyası seçin.")
            return
        if not dst:
            messagebox.showwarning("Uyarı", "Lütfen çıktı dosyası yolunu girin.")
            return
        try:
            status_var.set("Dönüştürülüyor...")
            window.update_idletasks()
            abs_path = json_to_excel(src, dst)
            status_var.set("Tamamlandı")
            messagebox.showinfo("Başarılı", f"Excel oluşturuldu:\n{abs_path}")
        except Exception as e:
            status_var.set("Hata")
            messagebox.showerror("Hata", f"Dönüştürme sırasında hata: {e}")

    btn_convert = tk.Button(window, text="Dönüştür", command=run_convert)
    btn_convert.grid(row=2, column=1, padx=10, pady=15, sticky="e")

    window.columnconfigure(1, weight=1)
    window.mainloop()

if __name__ == "__main__":
    args = sys.argv[1:]

    if "--gui" in args or len(args) == 0:
        launch_gui()
        sys.exit(0)

    json_path = None
    output_path = 'output/converted.xlsx'

    for i, a in enumerate(args):
        if not a.startswith('-') and json_path is None:
            json_path = a
        if a == "--output" and i + 1 < len(args):
            output_path = args[i + 1]

    if not json_path:
        print("⚠️ Dikkat Kullanım Bu şekilde: python main.py <json_dosyasi_yolu> [--output ozel.xlsx] veya --gui")
        sys.exit(1)

    json_to_excel(json_path, output_path)
