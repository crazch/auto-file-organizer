# 📂 Auto File Organizer

The **Auto File Organizer** is a personal Python scripting project designed to help users organize their files efficiently based on file types and folders.

> ⚠️ **Disclaimer:** This project is still in the very early stages (around 2% complete). Think of it as a prototype duct-taped together, actively under development and not production-ready.

---

## 🔍 5W1H Breakdown

### 1. What is it for?
To automatically organize messy folders by categorizing files into structured directories based on their file types.

### 2. Who is it for?
Anyone who frequently downloads or works with a lot of files and wants to keep their system organized. (See **"How to Use"** below for usage instructions.)

### 3. Why was it made?
To solve a repetitive, everyday problem — organizing files manually. This project automates that process and serves as a way to practice and demonstrate my Python skills.

### 4. Where was it made?
This project is built from scratch by a self-taught developer

### 5. When was it started?
- Initial planning began: **July 27, 2025**
- Development started: **August 1, 2025**

### 6. How does it work?
See the **"Design"** and **"How to Use"** sections below.

---

## 🛠️ Design (Early Stage Prototype)

The script executes user-defined commands by scanning a specific folder path provided via a variable or input. It checks for various file extensions in the target directory and moves each file to its corresponding folder (Images, Documents, Archives, etc.). If the folder doesn’t exist, it will be created automatically.

#### 📥 Example Workflow:
- **Input:** `~/Downloads`
- **Process:** Scans files like `.txt`, `.py`, `.zip`, `.jpg`, etc.
- **Output:** Files are moved to categorized folders like `Documents`, `Scripts`, `Images`, `Archives`, etc.

> 🚧 Note: This logic is still very basic and will be improved as development continues.

---

## ▶️ How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/crazch/auto-file-organizer.git
cd file-organizer
```

### 2. Run the script
```bash
python main.py
```
### 3. When Prompted:
Enter the full path of the folder you want to organize, for example:

```bash
C:\Users\YourName\Downloads
# or on Linux/macOS
~/Downloads
```

### 4. The script will:
- Scan all files in the specified folder.
- Create subfolders (Images, Documents, Archives, etc.).
- Move files into their respective folders.

---

## 📎 Requirements
- Python 3.8+
- Works on Windows, Linux, and macOS (in theory and testing in progress).
- Educational use only at this stage.

## ⚠️ Notes
- The project is still under heavy development.
- Code quality is experimental and intentionally rough, duct-taped together for learning purposes.
- Pull requests, feedback, and suggestions are welcome

## 🚧 Upcoming Goals
- Add file extension mappings via config file.
- Allow user-defined folder rules.
- Add logging and error handling.
- Build a GUI (optional, in later stages).

---

> Made with ☕, Python, and the determination of a self-taught coder.