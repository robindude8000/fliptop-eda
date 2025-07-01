# FlipTop Battle League EDA 🎤📊

This is an exploratory data analysis (EDA) project focused on the **FlipTop Battle League**, the Philippines' premier rap battle platform. The goal is to collect data from their official YouTube channel and generate insights and statsheets around:

- Emcees
- Battles
- Number of views
- Upload dates
- Other possible metrics (e.g., like counts, battle duration, comment count)

---

## 🔍 Objectives

- Scrape battle data from FlipTop’s YouTube channel
- Analyze views, upload frequency, and top-performing battles
- Profile emcees based on participation and popularity (views)
- Visualize insights using charts and tables
- Create a reusable dataset for further NLP or ML experiments (will need further study for this one)

---

## 🛠 Tools & Technologies

- **Python**
- **Pandas**
- **YouTube API**
- **Matplotlib / Seaborn / Plotly**
- **Jupyter Notebooks**
- **Git & GitHub**

---

## 📁 Project Structure

```bash
fliptop-eda/
│
├── dataset/                
├───── fliptop_videos.json  # Raw data in json          
├───── fliptop_videos.csv   # Raw data in csv
├── fliptop_eda.ipynb       # Jupyter notebooks for Cleaning, EDA, Graphs, charts, and visualizations 
├── get_videos.py           # Python scripts for scraping      
└── README.md               # Project overview
