# Data Analysis Toolkit for Food and Nutrition Sciences 🦛

Welcome to the **Data Analysis Toolkit for Food and Nutrition Sciences**, a comprehensive resource for MSc students mastering data analysis in nutrition research. This toolkit features 27 Jupyter notebooks across six modules, rendered as interactive HTML tutorials using Quarto and hosted on GitHub Pages. Run the notebooks directly in Google Colab with one click! With hippo-themed datasets (🦛), it covers Python basics, data handling, statistical analysis, advanced methods, and qualitative research.

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

3. **Run Notebooks Locally**:
   ```bash
   jupyter notebook notebooks/01_infrastructure/0_getting_started.ipynb
   ```

4. **Run Notebooks in Colab**:
   - Click the "Open in Colab" badges below to run notebooks in the cloud.

5. **Render the Site Locally**:
   ```bash
   rm -rf _site/
   quarto render
   ```
   View at `_site/index.html`.

6. **Auto-Rendering**:
   - The site auto-updates on pushes to the `groks-revisions` branch via GitHub Actions.
   - See `.github/workflows/deploy.yml` for details.

## 🧮 Modules and Notebooks

- **Infrastructure** (5 notebooks):
  - [Getting Started](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/infrastructure/getting_started.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/01_infrastructure/0_getting_started.ipynb)
  - [Python Setup](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/infrastructure/python_setup.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/01_infrastructure/1_python_setup.ipynb)

- **Programming Basics** (5 notebooks):
  - [Syntax and Variables](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/programming_basics/syntax_variables_comments.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/02_programming_basics/2.1_syntax_variables_comments.ipynb)
  - [Control Structures](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/programming_basics/control_structures.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/02_programming_basics/2.2_control_structures.ipynb)

- **Data Handling** (5 notebooks):
  - [Importing Data](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_handling/importing_data.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/03_data_handling/3.1_importing_data.ipynb)
  - [Data Cleaning](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_handling/data_cleaning.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/03_data_handling/3.2_data_cleaning.ipynb)

- **Data Analysis** (6 notebooks):
  - [Distributions and Visualisation](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/distributions_visualisation.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/04_data_analysis/4.1_distributions_visualisation.ipynb)
  - [Correlation Analysis](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/correlation_analysis.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/04_data_analysis/4.3_correlation_analysis.ipynb)
  - [Regression Modelling](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/regression_modelling.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/04_data_analysis/4.5_regression_modelling.ipynb)
  - [Logistic and Survival Analysis](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/data_analysis/04_logistic_and_survival.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/04_data_analysis/4.6_logistic_survival.ipynb)

- **Advanced Topics** (5 notebooks):
  - [Advanced Bayesian Modelling](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/advanced/advanced_bayesian.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/05_advanced/5.1_advanced_bayesian.ipynb)
  - [SQL for Data Analysis](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/advanced/sql_data_analysis.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/05_advanced/5.2_sql_data_analysis.ipynb)

- **Qualitative Research** (2 notebooks):
  - [Text Analysis](https://ggkuhnle.github.io/data-analysis-toolkit-FNS/notebooks/qualitative/text_analysis.html) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/data-analysis-toolkit-FNS/blob/groks-revisions/notebooks/06_qualitative/6.1_text_analysis.ipynb)

## 📊 Why Hippos?

Hippo-themed datasets make learning data analysis fun and relevant to nutrition science!

## 📝 License

Created by [Your Name]. Licensed under MIT.

---

Happy analysing! 🚀