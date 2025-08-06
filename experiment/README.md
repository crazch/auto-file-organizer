# File Organizer Project

Proyek File Organizer adalah proyek pribadi Python scripting yang dibuat untuk memudahkan user mengorganisir file berdasarkan type dan folder.

--

## Peraturan // Rules
1. Prohibited use of AI (ChatGPT, Copilot, etc.) is strictly enforced **during the development process**.
   - This includes writing functions, logic, or generating code snippets.
   - AI assistance is permitted for **project planning, README writing, and structural feedback only**.
2. You can only Google, read official documentation and suffer,
3. Every code block **must** have structured comment describing what, when, why, where, how it behave.
4. No Blind Copy-Pasting
> You are not allowed to copy-paste any code unless you can explain every line in writing or to a rubber duck.
5. Daily Commit or Journal Rule
>Every session must end with either:
>A Git commit
>A DEVLOG.md note explaining what was done, blocked, and next steps.

--

## Planning
### 5W1H
1. What is it for?
Proyek ini dibuat untuk user yang ingin mengorganisir file dengan rapi dan terstruktur berdasarkan file type dan folder.

2. Who is it made for?
Proyek ini bisa digunakan oleh siapa saja (Baca **How** dibawah untuk petunjuk penggunaan).

3. Why is it made?
Proyek ini saya buat untuk menyelesaikan masalah sehari-hari yang repetitif dan mengotomatisasikan pola-polanya, dan proyek ini menunjukkan dan melatih skill Python saya.

4. Where is it made?
Proyek ini dibangun murni dari self-taught developer.

5. When is it made?
Proyek ini masuk tahap perencanaan pada tanggal 27 Juli 2025 dan development pada 1 Agustus 2025.

--

## Designing
### Raw design
script akan mengeksekusi perintah user melalui file-path yang sudah ditentukan di dalam variabel,
script akan melakukan scan untuk setiap ekstensi/tipe file didalam folder yang sudah ditentukan dan memindahkan setiap file ke masing-masing folder yang bersangkutan, jika folder tidak ditemukan maka otomatis akan dibuat.
Contoh Input/Output:
Input: ~/Downloads
Proses: Scan txt, py, zip, rar, jpg, 
Output: File tersebut dipindahkan ke folder bersangkutan.

### Raw Pseudocode
```
BUAT dictionary untuk setiap folder dan file bersangkutan,
BUAT variabel file-path
JIKA file-path ditemukan MAKA scan semua jenis ekstensi DAN
pindahkan file ke folder yang bersangkutan 
JIKA folder tidak ditemukan MAKA buat folder sesuai dengan file type
JIKA file-path DAN file type tidak ditemukan MAKA return selesai dan berikan berapa file dipindahkan
```

--

## Future Planning
[ ] - Buat GUI

--

## How to use it?

1. Clone Repository:
```bash
git clone https://github.com/crazch/file-organizer.git
cd file-organizer
Run the Script:
```
2. Run The Script
```python
python main.py
```

2. When prompted, enter the full path to the folder you want to organize:
```
~/Download
```

3. When prompted, enter the full path to the folder you want to organize:
```bash
Example: C:\Users\YourName\Downloads
```

4. The script will:

- Scan all files in the folder.

- Create folders like Images, Documents, Archives, etc.

- Move files into their corresponding folders.

--

Note: Python 3.8+ is required. This script is for educational and personal use only.