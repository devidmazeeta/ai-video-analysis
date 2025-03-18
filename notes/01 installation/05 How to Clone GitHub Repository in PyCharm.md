# **How to Clone GitHub Repository in Pycharm (Step-by-Step Guide)**

### **Steps to Clone the GitHub Repository in PyCharm on Windows**

#### **Step 1: Open PyCharm**
1. **Launch PyCharm** on your Windows machine.
2. **Go to the Welcome Screen**:
   - If PyCharm opens with a project, go to **File > Close Project** to return to the welcome screen.

#### **Step 2: Clone the Repository**
1. **Select "Get from VCS"**  
   - On the welcome screen, click **"Get from Version Control"**.  
   - If you're inside a project, go to **File > New Project from Version Control**.

2. **Choose Git as the Version Control System**  
   - Under **Version Control**, select **Git**.

3. **Enter the GitHub Repository URL**  
   - In the **URL field**, enter:  
     ```
     https://github.com/devidmazeeta/ai-video-analysis.git
     ```
   
4. **Choose a Local Directory**  
   - In the **Directory field**, specify the folder where you want to store the cloned repository.

5. **Click "Clone"**  
   - PyCharm will download the repository files.

#### **Step 3: Authenticate GitHub (If Required)**
- If prompted, enter your **GitHub username and password** or **use a Personal Access Token (PAT)**.
- If using **GitHub authentication via PyCharm**, sign in through the GitHub login window.

#### **Step 4: Open and Set Up the Project**
1. **Once cloned, PyCharm will prompt to open the project** → Click **Yes**.
2. **Configure Python Interpreter**:
   - Go to **File > Settings > Project: ai-video-analysis > Python Interpreter**.
   - Select an existing interpreter or **create a new virtual environment**.

3. **Install Dependencies (If Required)**:
   - Open **Terminal** in PyCharm and run:
     ```sh
     pip install -r requirements.txt
     ```

#### **Step 5: Verify Git Integration**
1. **Check Git Setup**:
   - Go to **File > Settings > Version Control**.
   - Ensure that **Git** is enabled for the project.

2. **Verify Repository Status**:
   - Open **Terminal** in PyCharm and run:
     ```sh
     git status
     ```
   - If successful, it should show the current branch and any changes.

---
