# Data Analysis Toolkit for Food and Nutrition Sciences 🦛

Welcome to the **Data Analysis Toolkit for Food and Nutrition Sciences**, a comprehensive resource for MSc students mastering data analysis in nutrition research. This toolkit features 27 Jupyter notebooks across six modules, rendered as interactive HTML tutorials using Quarto. With hippo-themed datasets (🦛), it covers Python basics, data handling, statistical analysis, advanced methods, and qualitative research.

## 🌐 View the Rendered Site

Explore the rendered tutorials at:  
👉 **[https://ggkuhnle.github.io/data-analysis-toolkit-FNS/](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/)**

Highlights include:
- Regression Modelling: [notebooks/data_analysis/regression_modelling.html](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/regression_modelling.html)
- Logistic and Survival Analysis: [notebooks/data_analysis/04_logistic_and_survival.html](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/04_logistic_and_survival.html)
- Syllabus: [syllabus.html](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/syllabus.html)

## 📚 About the Toolkit

This toolkit guides you through:
- **Infrastructure**: Setting up Python, Jupyter, and Quarto.
- **Programming Basics**: Mastering Python syntax and data structures.
- **Data Handling**: Importing, cleaning, and transforming datasets.
- **Data Analysis**: Visualising data and building regression models.
- **Advanced Topics**: Bayesian methods, SQL, and dashboards.
- **Qualitative Research**: Analysing text data.

Datasets include `vitamin_trial.csv`, `hippo_nutrients.csv`, and more, all themed around hippos for fun and relevance.

## 🚀 Get Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ggkuhnle/data-analysis-toolkit-FNS.git
   cd data-analysis-toolkit-FNS
   ```

2. **Set Up Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Install Quarto: [quarto.org](https://quarto.org/docs/get-started/).

3. **Run Notebooks**:
   ```bash
   jupyter notebook notebooks/01_infrastructure/0_getting_started.ipynb
   ```

4. **Render the Site Locally**:
   ```bash
   rm -rf _site/
   quarto render
   ```
   View at `_site/index.html`.

5. **Auto-Rendering**:
   - The site auto-updates on pushes to the `groks-revisions` branch via GitHub Actions.
   - See `.github/workflows/deploy.yml` for details.

## 🧮 Modules

- **Infrastructure**: 5 notebooks, e.g., [Getting Started](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/infrastructure/getting_started.html)
- **Programming Basics**: 5 notebooks, e.g., [Syntax and Variables](https://ggku