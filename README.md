# 📦 Data Analysis Toolkit for Food and Nutritional Sciences

This repository provides a modular, self-guided collection of Python notebooks and Quarto pages to build data skills across the FNS curriculum.

## 🌐 View the Website

You can explore the rendered teaching materials and course structure at:

🔗 [https://ggkuhnle.github.io/data-analysis-toolkit-FNS/](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/)

This Quarto-based site includes:
- Full navigation and section landing pages
- Rendered notebooks and teaching pages
- Consistent updates from this repository



---

## 📘 Proposed Structure for a Three-Year Data Handling & Analysis Course

This structure supports a modular, scalable data course designed to span the undergraduate programme in Nutrition and Food Science (and related disciplines). The focus is on progressive skill-building with integration across academic years and alignment with common applications.

---

### 📁 1. Foundations and Tools *(folder: `infrastructure/`)*
**Objective:** Familiarise students with core tools for data work and reproducible research.

**Topics:**
- What is a data science environment?
- Python vs R vs other tools
- Using Google Colab and Jupyter (including local setup)
- Git and version control
- Installing and managing packages
- Finding help and documentation effectively
- When to use notebooks, scripts, markdown, or Quarto

**Outputs:**
- Notebooks explaining tooling concepts
- Practical "how-to" exercises

---

### 🧱 2. Programming Basics *(folder: `programming_basics/`)*
**Objective:** Teach core Python concepts and conventions with a data-centric focus.

**Topics:**
- Syntax, data types, loops, conditionals
- Functions, object-oriented basics
- Markdown and Quarto for documentation

---

### 🧮 3. Data Handling *(folder: `data_handling/`)*
**Objective:** Acquire, clean, and manage datasets.

**Topics:**
- Data types and formats
- Import/export data
- Cleaning, recoding, reshaping

---

### 📊 4. Data Analysis *(folder: `data_analysis/`)*
**Objective:** Understand and apply statistical testing and modelling.

**Topics:**
- Distributions and transformations
- Parametric and non-parametric testing
- Regression and power analysis
- Visualisation techniques

---

### 🚀 5. Advanced Techniques *(folder: `advanced/`)*
**Objective:** Introduce advanced methods for interested students.

**Topics:**
- Bayesian methods
- Workflow automation
- SQL and cloud database tools
- Dashboards and interactive visualisations

---

## 📂 Repository Layout
```
notebooks/
├── infrastructure/
├── programming_basics/
├── data_handling/
├── data_analysis/
├── advanced/
└── projects/
```

---



## 🧰 Requirements (for Local Use)

If you want to run these notebooks locally using Jupyter:

```bash
pip install -r requirements.txt
```

### Main Python Libraries Used:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `statsmodels`




## 📂 Directory Structure

```
data-analysis-toolkit-FNS/
├── notebooks/
│   ├── infrastructure/
│   ├── programming_basics/
│   ├── data_handling/
│   ├── data_analysis/
│   ├── advanced/
│   └── projects/
├── .github/
│   └── workflows/
│       └── quarto-publish.yml
├── index.qmd
├── _quarto.yml
├── requirements.txt
└── README.md
```




## 📝 License

This material is made available for teaching and academic use.  
You are welcome to adapt and share it **with attribution**.
