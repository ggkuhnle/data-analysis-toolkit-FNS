# Data Analysis Toolkit for Food and Nutrition Sciences 🦛

Welcome to the **Data Analysis Toolkit for Food and Nutrition Sciences**, designed for MSc students in Food and Nutrition Sciences. This repository provides 26 Jupyter notebooks, datasets, and Quarto-rendered tutorials to master data analysis, from Python basics to advanced Bayesian modelling and qualitative text analysis.

Our hippo-themed toolkit (🦛) uses nutrition-inspired examples, like hippo diet logs, to make learning engaging and relevant. Whether you're analysing nutrient intakes or exploring food preferences, this toolkit equips you with skills for research projects like the National Diet and Nutrition Survey (NDNS).

## 📚 Repository Structure

The toolkit is organised into six modules under `notebooks/`. Datasets are stored in `notebooks/*/data/`. Rendered HTML tutorials will be generated in `_site/notebooks/` after running `quarto render`.

- **notebooks/01_infrastructure/**: Set up your data science environment (5 notebooks).
  - Dataset: `notebooks/01_infrastructure/data/hippo_diets.csv` (50 rows, calories/protein).
- **notebooks/02_programming_basics/**: Learn Python fundamentals (5 notebooks).
  - No datasets required.
- **notebooks/03_data_handling/**: Master data importing, cleaning, and transformation (5 notebooks).
  - Dataset: `notebooks/03_data_handling/data/hippo_nutrients.csv` (100 rows, nutrient intakes).
- **notebooks/04_data_analysis/**: Perform statistical analysis and visualisation (5 notebooks).
  - Dataset: `notebooks/04_data_analysis/data/vitamin_trial.csv` (200 rows, vitamin D trial data).
- **notebooks/05_advanced/**: Explore advanced topics like Bayesian methods and SQL (5 notebooks).
  - Datasets: `notebooks/05_advanced/data/large_food_log.csv` (500 rows, meal nutrients), `notebooks/03_data_handling/data/hippo_nutrients.csv`.
- **notebooks/06_qualitative/**: Analyse qualitative data (2 notebooks).
  - Dataset: `notebooks/06_qualitative/data/food_preferences.txt` (50 lines, survey responses).

Additional files:
- `index.qmd`: Homepage for the Quarto site.
- `syllabus.qmd`: Detailed module breakdown.
- `requirements.txt`: Python dependencies.
- `_quarto.yml`: Quarto configuration.
- `_site/`: Currently contains outdated HTMLs; clear before re-rendering.

**Note**: The `_site/` directory contains HTMLs from a previous version. Delete `_site/` and run `quarto render` to generate fresh tutorials.

## 🚀 Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ggkuhnle/data-analysis-toolkit-FNS.git
   cd data-analysis-toolkit-FNS
   ```

2. **Install Dependencies**:
   Install Python 3.9+ and dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Install Quarto: [quarto.org/docs/get-started](https://quarto.org/docs/get-started).

3. **Run Notebooks**:
   Use Jupyter or Colab:
   ```bash
   jupyter notebook notebooks/01_infrastructure/0_getting_started.ipynb
   ```
   Or upload to [colab.research.google.com](https://colab.research.google.com/).

4. **Render the Site**:
   Clear outdated HTMLs:
   ```bash
   rm -rf _site/
   ```
   Render:
   ```bash
   quarto render
   ```
   View at `_site/index.html` or deploy to GitHub Pages.

## 📊 Viewing Tutorials

After rendering, tutorials will be in `_site/notebooks/` (e.g., `_site/notebooks/data_handling/importing_data.html`). The syllabus maps notebooks to their HTML outputs.

## 🧮 Learning Path

Start with `notebooks/01_infrastructure/` for setup, then progress through programming, data handling, analysis, advanced methods, and qualitative research. Each notebook includes exercises and comments for learning.

## 🦛 Why Hippos?

Hippos make data analysis fun! Datasets like `hippo_nutrients.csv` use hippo-themed examples to keep you engaged.

## 🤝 Contributing

Fork the repo, create a branch, and submit a pull request:
```bash
git checkout -b my-feature
git commit -m "Add new feature"
git push origin my-feature
```

## 📬 Contact

For issues, open a GitHub issue or contact [your.email@example.com](mailto:your.email@example.com).

Happy analysing, and may your data be as robust as a hippo! 🦛🚀

---

*Repository maintained by [Your Name]. Licensed under MIT.*