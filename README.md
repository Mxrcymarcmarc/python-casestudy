<!-- Centered Project Title -->
<div align="center">

<img src="/Case Study/PUPLogo.png" alt="PUP Logo" width="100" style="border-radius: 8px;"/>

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
          <p>🔴Develop a structured system for managing student data.</li>
          <p>⚪Enhance instructors’ decision-making using analytics.</li>
          <p>🔴Automate report generation for academic performance.</li>
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
      <td style="vertical-align: top; padding: 10px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:5px;">📥 Ingest Module</h3>
        <br>
        <ul>
   <ul>
  <li>Read CSV files and validate required fields</li><br>
  <li>Parse numeric scores safely</li><br>
  <li>Organize students by section</li>
</ul>
      </td>
      <td style="vertical-align: top; padding: 10px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:5px;">⚙️ Transform Module</h3>
        <ul>
          <li>Compute quiz averages</li>
          <li>Apply weighted grades (configurable via <code>config.json</code>)</li>
          <li>Determine final letter grades</li>
          <li>Assign student status: Pass / At-Risk / Fail / Incomplete</li>
          <li>Supports selecting, projecting, sorting, inserting, and deleting students</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 10px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:5px;">📊 Analyze Module</h3>
        <ul>
          <li>Extract scores by category (quiz, midterm, final, overall grade)</li>
          <li>Compute weighted means, standard deviations, percentiles, and outliers</li>
          <li>Generate histograms and normal distributions (saved as PNG)</li>
          <li>Compare multiple sections visually by category</li>
        </ul>
      </td>
       <td style="vertical-align: top; padding: 10px; border: 1px solid #444;">
        <h3 align="center" style="margin-top:0; margin-bottom:5px;">🧾 Reports Module</h3>
        <ul>
          <li>Export CSV reports per section or for all sections</li>
          <li>Export list of At-Risk students</li>
          <li>Print summaries in the terminal</li>
          <li>File outputs organized into a <code>reports</code> folder</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

<hr style="width:50%; margin:25px auto;">

<hr style="width:50%; margin:25px auto;">

<!-- Prerequisites Section -->
<div align="center">
  <h3>⚙️ Prerequisites</h3>
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
  <h3>📥 Installation Steps</h3>
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

<!-- Team Section -->
<h2 id="team" align="center">👥 Team</h2>

<div align="center">
  <table style="width: 80%; border-collapse: collapse; margin-top: 30px;">
    <tr>
      <td align="center">
        <a href="https://github.com/j3yzi" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/j3yzi.png" width="100" style="border-radius: 50%;" alt="j3yzi"/><br/>
          <strong>John Michael Reyes</strong>
        </a><br/>
        Project Manager
      </td>
      <td align="center">
        <a href="https://github.com/Mxrcymarcmarc" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/Mxrcymarcmarc.png" width="100" style="border-radius: 50%;" alt="Mxrcymarcmarc"/><br/>
          <strong>Marcymar Marquez</strong>
        </a><br/>
        Backend Developer
      </td>
      <td align="center">
        <a href="https://github.com/Mhean21" target="_blank" style="text-decoration: underline;">
          <img src="https://github.com/Mhean21.png" width="100" style="border-radius: 50%;" alt="Mhean21"/><br/>
          <strong>Mhelby Anne Abundo</strong>
        </a><br/>
        Quality Analyst
      </td>
    </tr>
  </table>
</div>

<hr style="width:60%; margin:25px auto;">
