<!-- Centered Project Title -->
<div align="center">

<img src="/PUP Logo.png" alt="PUP Logo" width="150" style="border-radius: 8px;"/>

<div align="center">
  <h1><b><i>Academic</i> Analytics <i>Lite</i></b></h1>

  <!-- Badges -->
<div align="center">
  <img src="https://img.shields.io/badge/Language-Python-%23FF0000?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Status-Active-white?style=for-the-badge&logoColor=red" alt="Status Badge"/>
  <img src="https://img.shields.io/badge/Version-1.0-%23FF0000?style=for-the-badge&logoColor=white" alt="Version Badge"/>
  <img src="https://img.shields.io/badge/Status-Optimized-white?style=for-the-badge&logo=github&logoColor=red" alt="Status Optimized Badge"/>
</div>

<hr style="width:60%; margin:20px auto;">

<!-- Table of Contents -->
<h2 align="center"> Table of Contents</h2>

<div align="center">
  <table cellpadding="10" cellspacing="0" border="2" style="border-collapse: collapse;">
    <tr>
      <td align="center"><a href="#about">About</a></td>
      <td align="center"><a href="#objectives">Objectives</a></td>
      <td align="center"><a href="#features">Features</a></td>
      <td align="center"><a href="#prerequisites">Prerequisites</a></td>
      <td align="center"><a href="#installation">Installation</a></td>
      <td align="center"><a href="#complexity">Complexity</a></td>
      <td align="center"><a href="#csv">CSV</a></td>
      <td align="center"><a href="#team">Team</a></td>
    </tr>
  </table>
</div>

<hr style="width:60%; margin:25px auto;">

<!-- About Section -->
<h2 id="about" align="center">About</h2>
<p align="center" style="width:80%; margin:auto;">
  <b>PUP Academic Analytics Lite</b> is a lightweight analytics tool designed to process and evaluate student academic performance efficiently using Python and modular data structures.
</p>

<!-- Objectives Section -->
<hr style="width:60%; margin:25px auto;">

<!-- Objectives Section -->
<h2 id="objectives" align="center">Objectives</h2>

<div align="center">
  <table>
    <tr>
      <td>
        <ul>
          <li>Develop a structured system for managing student data.</li>
          <li>Enhance instructors’ decision-making using analytics.</li>
          <li>Automate report generation for academic performance.</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

<hr style="width:60%; margin:25px auto;">

<!-- Features Section -->
<h2 id="features" align="center">🧩 Features</h2>

<div align="center">
  <table width="85%" style="border-collapse: collapse; text-align: left; margin: auto;">
    <tr>
      <!-- INGEST MODULE -->
      <td style="vertical-align: top; padding: 15px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:10px;">📥 Ingest Module</h3>
        <ul style="margin-top: 5px; line-height: 1.6;">
          <li>Read CSV files and validate required fields</li>
          <li>Parse numeric scores safely</li>
          <li>Organize students by section</li>
        </ul>
        <br><br><br>
      </td>
      <!-- TRANSFORM MODULE -->
      <td style="vertical-align: top; padding: 15px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:10px;">⚙️ Transform Module</h3>
        <ul style="margin-top: 5px; line-height: 1.6;">
          <li>Compute quiz averages</li>
          <li>Apply weighted grades (configurable via <code>config.json</code>)</li>
          <li>Determine final letter grades</li>
          <li>Assign student status: Pass / At-Risk / Fail / Incomplete</li>
          <li>Supports selecting, projecting, sorting, inserting, and deleting students</li>
        </ul>
      </td>
    </tr>
    <tr>
      <!-- ANALYZE MODULE -->
      <td style="vertical-align: top; padding: 15px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:10px;">📊 Analyze Module</h3>
        <ul style="margin-top: 5px; line-height: 1.6;">
          <li>Extract scores by category (quiz, midterm, final, overall grade)</li>
          <li>Compute weighted means, standard deviations, percentiles, and outliers</li>
          <li>Generate histograms and normal distributions (saved as PNG)</li>
          <li>Compare multiple sections visually by category</li>
        </ul>
        <br>
      </td>
      <!-- REPORTS MODULE -->
      <td style="vertical-align: top; padding: 15px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:10px;">🧾 Reports Module</h3>
        <ul style="margin-top: 5px; line-height: 1.6;">
          <li>Export CSV reports per section or for all sections</li>
          <li>Export list of At-Risk students</li>
          <li>Print summaries in the terminal</li>
          <li>File outputs organized into a <code>reports</code> folder</li>
        </ul>
        <br><br>
      </td>
    </tr>
  </table>
</div>


<hr style="width:50%; margin:25px auto;">


<!-- Prerequisites Section -->
<div align="center">
  <h3 id="prerequisites">⚙️ Prerequisites</h3>
</div>


<div align="center">
  <table style="width: 500px; border-collapse: collapse; margin-top: 30px;">
    <tr>
      <td>
        <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" width="70px" alt="Python"/>
      </td>
      <td>
        <strong>Python 3.10 or higher</strong> - Required to run the application
        <br/>
        <code>python --version</code> to check if installed
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code" width="70px" alt="VS Code"/>
      </td>
      <td>
        <strong>VS Code or any Python editor</strong> - Recommended for editing the project
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://img.shields.io/badge/Git-orange?style=for-the-badge&logo=git" width="70px" alt="Git"/>
      </td>
      <td>
        <strong>Git</strong> - Optional, for cloning the repository
        <br/>
        Alternative: Download ZIP from GitHub
      </td>
    </tr>
  </table>
</div>

<hr style="width:50%; margin:25px auto;">

<!-- Installation Section -->
<div align="center">
  <h3 id="installation">📥 Installation Steps</h3>
</div>


<div align="center">
  <table style="width: 600px; border-collapse: collapse; margin-top: 30px;">
    <tr>
      <td>1️⃣</td>
      <td>
        <strong>Get the code</strong>
        <pre><code>git clone https://github.com/j3yzi/PUP-Academic-Analytics-Lite.git</code></pre>
      </td>
    </tr>
    <tr>
      <td align="center">2️⃣</td>
      <td>
        <strong>Navigate to project folder</strong>
        <pre><code>cd PUP-Academic-Analytics-Lite</code></pre>
      </td>
    </tr>
    <tr>
      <td align="center">3️⃣</td>
      <td>
        <strong>Run the program</strong>
        <pre><code>python main.py</code></pre>
      </td>
    </tr>
  </table>
</div>

<hr style="width:60%; margin:25px auto;">

<!-- Complexity Section -->
<h2 id="complexity" align="center">🧮 Complexity Analysis</h2>

<p align="center" style="width:80%; margin:auto; margin-bottom:20px;">
  The table below shows the estimated time and space complexities of each core module in <b>Academic Analytics Lite</b>.
  These values describe how the system performs as the number of student records (<code>n</code>) increases.
</p>

<div align="center">
  <table width="90%" cellpadding="10" cellspacing="0" border="2" style="border-collapse: collapse; text-align: center;">
    <tr style="background-color:#f5f5f5;">
      <th>Module</th>
      <th>Main Functionality</th>
      <th>Dominant Operation</th>
      <th>Time Complexity</th>
      <th>Space Complexity</th>
    </tr>
    <tr>
      <td>📥 <b>Ingest</b></td>
      <td>Read CSV, validate fields, and handle malformed rows</td>
      <td>File scanning & validation loop</td>
      <td><code>O(n)</code></td>
      <td><code>O(n)</code></td>
    </tr>
    <tr>
      <td>🧩 <b>Array Operations</b></td>
      <td>Select, project, insert, delete, and sort student records</td>
      <td>Sorting (e.g., quicksort or mergesort)</td>
      <td><code>O(n log n)</code></td>
      <td><code>O(n)</code></td>
    </tr>
    <tr>
      <td>📊 <b>Analytics</b></td>
      <td>Compute weighted grades, distributions, percentiles, outliers</td>
      <td>Multiple passes through data</td>
      <td><code>O(n)</code> – <code>O(n log n)</code></td>
      <td><code>O(n)</code></td>
    </tr>
    <tr>
      <td>🧾 <b>Reports</b></td>
      <td>Print summaries, export per-section CSVs, and generate “At-Risk” lists</td>
      <td>Sequential write operations</td>
      <td><code>O(n)</code></td>
      <td><code>O(1)</code></td>
    </tr>
    <tr>
      <td>⚙️ <b>Configuration</b></td>
      <td>Load JSON settings (weights, thresholds, folder paths)</td>
      <td>JSON parsing</td>
      <td><code>O(k)</code> (k = number of keys)</td>
      <td><code>O(k)</code></td>
    </tr>
    <tr>
      <td>🧪 <b>Testing</b></td>
      <td>Unit tests, type hints, and performance timing</td>
      <td>Test suite execution</td>
      <td><code>O(n)</code> per test group</td>
      <td><code>O(1)</code></td>
    </tr>
  </table>
</div>

<p align="center" style="width:75%; margin:auto; margin-top:25px;">
  <b>Overall System Complexity:</b> The end-to-end pipeline operates at approximately 
  <code>O(n log n)</code> time and <code>O(n)</code> space due to sorting and analytical computations.  
  Most stages (Ingest, Analytics, Reports) are linear in complexity, ensuring scalability for large datasets.
</p>


  </table>
</div>



<hr style="width:60%; margin:25px auto;">

<!-- Team Section -->
<h2 id="team" align="center">👥 Team</h2>

<div align="center">
  <table style="width: 80%; border-collapse: collapse; margin-top: 30px;">
    <tr>
      <td align="center">
        <a href="https://github.com/Mxrcymarcmarc" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/Mxrcymarcmarc.png" width="100" style="border-radius: 50%;" alt="Mxrcymarcmarc"/><br/>
          <strong>Mxrcymarcmarc</strong>
        </a><br/>
        Lemuel Marc Celis
      </td>
      <td align="center">
        <a href="https://github.com/Mhean21" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/Mhean21.png" width="100" style="border-radius: 50%;" alt="Mhean21"/><br/>
          <strong>Mhean21</strong>
        </a><br/>
        Mhelby Anne Abundo
      </td>
      <td align="center">
        <a href="https://github.com/CyberFlowHex" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/CyberFlowHex.png" width="100" style="border-radius: 50%;" alt="CyberFlowHex"/><br/>
          <strong>CyberFlowHex</strong>
        </a><br/>
        Janssen Lein Arriola
      </td>
    </tr>
    <tr>
      <td align="center">
        <a href="https://github.com/meiaooo" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/meiaooo.png" width="100" style="border-radius: 50%;" alt="meiaooo"/><br/>
          <strong>meiaooo</strong>
        </a><br/>
        Amylin Franze Flores
      </td>
      <td align="center">
        <a href="https://github.com/adiayouu" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/adiayouu.png" width="100" style="border-radius: 50%;" alt="adiayouu"/><br/>
          <strong>adiayouu</strong>
        </a><br/>
        Bhea Eden Abril
      </td>
      <td align="center">
        <a href="https://github.com/ar-aim" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/ar-aim.png" width="100" style="border-radius: 50%;" alt="ar-aim"/><br/>
          <strong>ar-aim</strong>
        </a><br/>
        Ria May Jacobe
      </td>
    </tr>
  </table>
</div>

<!-- Csv File --->
<hr style="width:60%; margin:25px auto;">

<!-- CSV Section -->
<h2 id="csv" align="center"> CSV Handling</h2>

<div align="center">
  <img src="/csv.png" alt="CSV Pic" width="700" style="margin-top:10px; border-radius:8px;">

<hr style="width:60%; margin:25px auto;">
<details>
  <summary>📁 PUP Academic Analytics Lite (click to expand)</summary>
  <pre>
📁 PUP Academic Analytics Lite/
├── 📄 main.py                      # Main pipeline that runs all modules
│
├── 📁 src/                         # Source code for core logic
│   ├── 📄 ingest.py                # Read CSV files, validate fields, handle bad rows
│   ├── 📄 transform.py             # Compute weighted grades, letter grades, statuses
│   ├── 📄 analyze.py               # Perform statistical computations and distributions
│   ├── 📄 reports.py               # Generate per-section reports and summaries
│   └── 📄 config.json              # Stores weights, thresholds, folder paths
│
├── 📁 data/                        # Input and output datasets
│   ├── 📄 input.csv                # Raw student data
│   └── 📁 reports/                 # Auto-generated report exports (CSV, summary)
│
├── 📁 tests/                       # Unit and performance testing
│   ├── 📄 test_ingest.py           # Tests CSV ingestion and validation
│   ├── 📄 test_transform.py        # Tests computations and grade logic
│   ├── 📄 test_analyze.py          # Tests statistical functions and analytics
│   └── 📄 test_reports.py          # Tests output file generation
│
├── 📁 assets/                      # Supporting materials (charts, images)
│   ├── 📄 histogram.png
│   ├── 📄 distribution.png
│   └── 📄 sample_report.csv
│
├── 📁 docs/                        # Documentation and notes
│
├── 📄 requirements.txt             # Python dependencies (if any)
├── 📄 README.md                    # Project overview and documentation
└── 📄 LICENSE                      # Open-source license (if applicable)
  </pre>
</details>


<!-- File Structure --->

