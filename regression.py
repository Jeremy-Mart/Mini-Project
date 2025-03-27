import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

def compare_models_aic(model1, model2, name1="Model 1", name2="Model 2"):
    """
    Compares the AIC (Akaike Information Criterion) of two statistical models
    and prints their values along with their provided names.

    Parameters
    ----------
    model1 : statsmodels result object
        The first fitted model to compare.

    model2 : statsmodels result object
        The second fitted model to compare.

    name1 : str, optional
        Name to display for the first model. Default is "Model 1".

    name2 : str, optional
        Name to display for the second model. Default is "Model 2".

    Returns
    -------
    dict
        Dictionary with AIC values for both models:
        {
            name1: aic_value1,
            name2: aic_value2
        }

    Prints
    ------
    - AIC value of each model with its name.
    - Which model has the lower (better) AIC.
    """
    aic1 = model1.aic
    aic2 = model2.aic

    print(f"AIC - {name1}: {aic1:.2f}")
    print(f"AIC - {name2}: {aic2:.2f}")

    if aic1 < aic2:
        print(f"→ {name1} has a lower AIC and is preferred.")
    elif aic2 < aic1:
        print(f"→ {name2} has a lower AIC and is preferred.")
    else:
        print("→ Both models have the same AIC.")

def likelihood_ratio_test(model1, model2, name1="Model 1", name2="Model 2"):
    """
    Performs a Likelihood Ratio Test (LRT) to compare two nested statistical models.

    Parameters
    ----------
    model1 : statsmodels result object
        The simpler (nested) model, e.g., Poisson regression.

    model2 : statsmodels result object
        The more complex model, e.g., Negative Binomial regression.

    name1 : str, optional
        Display name for model1 (restricted model). Default is "Model 1".

    name2 : str, optional
        Display name for model2 (full model). Default is "Model 2".

    Returns
    -------
    dict
        A dictionary with:
        {
            "LR_statistic": float,
            "degrees_of_freedom": int,
            "p_value": float
        }

    Prints
    ------
    - Likelihood ratio test statistic.
    - Degrees of freedom.
    - p-value from chi-squared distribution.
    - Conclusion about model comparison.
    """
    
    lr_stat = 2 * (model2.llf - model1.llf)
    df_diff = (model2.df_model + 1) - model1.df_model  # model2 has 1 extra param (e.g., alpha in NB)

    p_value = stats.chi2.sf(lr_stat, df_diff)

    print(f"Likelihood Ratio Test: '{name1}' vs. '{name2}'")
    print(f"→ LR Statistic: {lr_stat:.2f}")
    print(f"→ Degrees of Freedom: {df_diff}")
    print(f"→ p-value: {p_value:.5f}")

    if p_value < 0.05:
        print(f"→ '{name2}' significantly improves model fit over '{name1}' (p < 0.05).")
    else:
        print(f"→ No significant improvement; '{name1}' is sufficient.")


def compute_pseudo_r2(model, model_name="Model"):
    """
    Computes pseudo R² statistics (McFadden's R² and Cragg & Uhler's R²) for a fitted model.

    Parameters
    ----------
    model : statsmodels result object
        The fitted model (e.g., Negative Binomial, Poisson) from statsmodels.

    model_name : str, optional
        Name of the model for labeling purposes. Default is "Model".

    Returns
    -------
    pd.DataFrame
        A DataFrame with pseudo R² metrics:
        - r2ML: Maximum Likelihood pseudo R² (McFadden's R²)
        - r2CU: Cragg & Uhler's pseudo R²

    Prints
    ------
    - A nicely formatted table of R² values.
    """
    llh = model.llf  
    llh_null = model.null_deviance / -2  

    r2_ml = 1 - (llh_null / llh)  
    r2_cu = r2_ml / (1 - (llh_null / model.nobs)) 

    pseudo_r2_results = pd.DataFrame({
        "Model": [model_name, model_name],
        "Metric": ["r2ML", "r2CU"],
        "Value": [r2_ml, r2_cu]
    })
    
    return pseudo_r2_results

def compute_vif(df, features, add_constant=True):
    """
    Computes the Variance Inflation Factor (VIF) for a set of independent variables
    to diagnose multicollinearity in a regression model.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the features.

    features : list of str
        List of column names (independent variables) for which to calculate VIF.

    add_constant : bool, optional
        Whether to include a constant (intercept term) in the calculation.
        Default is True.

    Returns
    -------
    pd.DataFrame
        A DataFrame with each variable and its corresponding VIF value.

    Prints
    ------
    - Table of VIF values per variable.
    """
    X = df[features].copy()

    if add_constant:
        X = sm.add_constant(X)

    vif_data = pd.DataFrame({
        "Variable": X.columns,
        "VIF": [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    })

    return vif_data
