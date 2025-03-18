# **How to Install PyCharm on a Windows Machine (Step-by-Step Guide)**

### **Step 1: Download PyCharm**
1. Open your web browser and visit the official PyCharm website:
   🔗 [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
2. Choose between:
   - **Professional** (Paid, for web and scientific development)
   - **Community** (Free, for standard Python development)
3. Click **Download** under the version you want.

---

### **Step 2: Run the Installer**
1. Navigate to the **Downloads** folder.
2. Double-click the downloaded **`pycharm-community-<version>.exe`** file.

---

### **Step 3: Start the Installation**
1. Click **Next** in the **PyCharm Setup Wizard**.
2. Select the installation directory (default: `C:\Program Files\JetBrains\PyCharm Community Edition`).
3. Click **Next**.

---

### **Step 4: Configure Installation Options**
1. **Add Desktop Shortcut**
   - Check **"Create Desktop Shortcut"** (64-bit recommended).

2. **Update PATH Variable**
   - Check **"Add launchers dir to the PATH"** (optional).

3. **Create File Associations**
   - Check **“.py”** to associate Python files with PyCharm.

4. Click **Next**.

---

### **Step 5: Choose the Start Menu Folder**
1. Keep the default setting (`JetBrains`).
2. Click **Install**.

---

### **Step 6: Complete Installation**
1. Wait for the installation to finish.
2. Check **"Run PyCharm Community Edition"**.
3. Click **Finish**.

---

### **Step 7: Configure PyCharm (First Launch)**
1. Choose the **UI theme** (Light/Dark).
2. Click **Next** and review default settings.
3. Click **Start using PyCharm**.

---

### **Step 8: Locate Python Interpreter**
1. Open **PyCharm**.
2. Click **New Project**.
3. In the **New Project** window, locate the **Python Interpreter** section.
4. Click **Add Interpreter** → **Existing Interpreter**.
5. Browse and select your installed **Python.exe** file.
   - Default location (if installed via Python installer):
     ```
     C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\python.exe
     ```
   - If installed via Anaconda:
     ```
     C:\Users\YourUsername\anaconda3\python.exe
     ```
6. Click **OK** to set the interpreter.

---

### **Step 9: Verify Installation**
1. Click **New Project** → Select Python Interpreter.
2. Write and run a simple Python program:
   ```python
   print("Hello, PyCharm!")
   ```
3. If the output appears correctly, PyCharm is successfully configured.

---

### **Step 10: Install Required Plugins (Optional)**
- Go to **File** → **Settings** → **Plugins**.
- Search for useful plugins like **Python Extended** or **Markdown Support**.

---
