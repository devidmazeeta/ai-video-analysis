# **How to Install GIT on a Windows Machine (Step-by-Step Guide)**

## **Step 1: Download Git for Windows**
1. Open your web browser and go to the official Git website:  
   👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Click on the **Windows** option to download the Git setup file.

3. On the next page, find the section **"Standalone Installer"**.

4. Click on **"64-bit Git for Windows Setup"** to download the latest `.exe` installer.

5. Once the download is complete, proceed with the **installation steps** mentioned earlier.  

---

## **Step 2: Run the Git Installer**
1. Once the `.exe` file is downloaded (e.g., `Git-2.x.x-64-bit.exe`), go to your **Downloads** folder.
2. Double-click the downloaded file to run the installer.

---

## **Step 3: Install Git**
1. **User Account Control (UAC) Prompt:**  
   If prompted by Windows, click **Yes** to allow the installer to make changes.

2. **Git Setup Wizard:**  
   The Git Setup Wizard will open. Click **Next** to continue.

3. **Choose Installation Location:**  
   - By default, Git is installed in `C:\Program Files\Git\`.  
   - You can change the location if needed. Otherwise, click **Next**.

4. **Select Components:**  
   - The default components are fine for most users.  
   - Recommended selections:
     - ✅ **Git Bash**
     - ✅ **Git GUI**
     - ✅ **Git LFS (Large File Support)**
     - ✅ **Associate .git files with default editor**
   - Click **Next**.

5. **Choose Default Editor for Git:**  
   - Select your preferred text editor for Git.  
   - Default: **Vim** (Not user-friendly for beginners).  
   - Recommended: **Notepad++** or **Visual Studio Code** (if installed).
   - Click **Next**.

6. **Adjust Your PATH Environment:**  
   - Select **"Git from the command line and also from 3rd-party software"**  
   - This allows Git to be used from both the command line and PowerShell.  
   - Click **Next**.

7. **Choose HTTPS Transport Backend:**  
   - Select **"Use the OpenSSL library"** (recommended).  
   - Click **Next**.

8. **Configure Line Ending Conversions:**  
   - Windows users: **"Checkout as-is, Commit as-is"**.  
   - Click **Next**.

9. **Choose Terminal Emulator for Git Bash:**  
   - **MinTTY (default terminal)** is recommended.  
   - Click **Next**.

10. **Choose Default Git Pull Behavior:**  
    - Leave it as **"Default (fast-forward or merge)"**.  
    - Click **Next**.

11. **Enable Credential Manager:**  
    - Select **"Git Credential Manager"** (recommended).  
    - Click **Next**.

12. **Enable Extra Options:**  
    - You can enable experimental options if needed, but defaults are fine.  
    - Click **Install**.

---

## **Step 4: Wait for Installation to Complete**
- The installer will now extract files and install Git on your system.
- Once the installation is complete, click **Finish**.

---

## **Step 5: Verify Git Installation**
1. Open **Command Prompt (cmd)** or **PowerShell**.
2. Type the following command and press **Enter**:
   ```
   git --version
   ```
3. If Git is installed correctly, you will see an output similar to:
   ```
   git version 2.x.x
   ```

---

## **Step 6: Configure Git (First-Time Setup)**
1. Set up your username:
   ```
   git config --global user.name "Your Name"
   ```
2. Set up your email:
   ```
   git config --global user.email "your-email@example.com"
   ```
3. Verify configuration:
   ```
   git config --list
   ```
   - This should display your configured username and email.

---

## **Step 7: (Optional) Install a GUI for Git**
If you prefer a graphical user interface:
- You can install **GitHub Desktop**: [https://desktop.github.com/](https://desktop.github.com/)
- Other GUI tools: **GitKraken, SourceTree, SmartGit**.

---

## **Step 8: Restart Your Computer (Recommended)**
After installation, restart your computer to apply system-wide changes.

---

### **🎉 Git is now installed and ready to use!**
You can use Git via:
- **Git Bash** (for Unix-style commands)
- **Command Prompt (cmd)**
- **PowerShell**
- **GUI tools (optional)**

---
