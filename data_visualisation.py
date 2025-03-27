import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_accidents_by_day(
    df,
    day_col,
    value_col,
    title="Number of Accidents per Day of the Week",
    xlabel="Day of the Week",
    ylabel="Total Number of Accidents",
    day_order=None
):
    """
    Plots a bar chart showing the total number of accidents per day of the week.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data to plot.

    day_col : str
        The name of the column containing the day of the week (e.g., "Lundi", "Mardi", etc.).

    value_col : str
        The name of the column containing the numeric values to aggregate (e.g., accident counts).

    title : str, optional
        Title of the plot. Default is "Number of Accidents per Day of the Week".

    xlabel : str, optional
        Label for the x-axis. Default is "Day of the Week".

    ylabel : str, optional
        Label for the y-axis. Default is "Total Number of Accidents".

    day_order : list of str, optional
        A list specifying the order of the days to display on the x-axis.
        If None, defaults to ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"].

    Returns
    -------
    None
        Displays a seaborn bar plot.
    """
    if day_order is None:
        day_order = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    
    day_counts = df.groupby(day_col, as_index=False)[value_col].sum()
    
    day_counts[day_col] = pd.Categorical(day_counts[day_col], categories=day_order, ordered=True)
    day_counts = day_counts.sort_values(day_col)
    
    plt.figure(figsize=(10, 5))
    sns.barplot(data=day_counts, x=day_col, y=value_col, color="steelblue")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_avg_accidents_weekday_vs_weekend(
    df,
    day_col,
    value_col,
    binary_col="Weekend",
    weekend_days=None,
    colors=None,
    title="Average Number of Accidents per Day (Weekdays vs. Weekends)",
    xlabel="Type of Day",
    ylabel="Average Number of Accidents"
):
    """
    Plots a bar chart comparing the average number of accidents on weekdays versus weekends.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the accident data.

    day_col : str
        The name of the column representing the day of the week.

    value_col : str
        The name of the column containing the accident count or metric to average.

    binary_col : str, optional
        Name of the new column to be created that categorizes days as "Weekday" or "Weekend".
        Default is "Weekend".

    weekend_days : list of str, optional
        List of day names considered as weekends (e.g., ["Samedi", "Dimanche"]).
        If None, defaults to ["Samedi", "Dimanche"].

    colors : list of str, optional
        A list of two colors used for the bars in the plot.
        Default is ["#E0897E", "#63B7C3"].

    title : str, optional
        Title of the plot. Default is "Average Number of Accidents per Day (Weekdays vs. Weekends)".

    xlabel : str, optional
        Label for the x-axis. Default is "Type of Day".

    ylabel : str, optional
        Label for the y-axis. Default is "Average Number of Accidents".

    Returns
    -------
    None
        Displays a seaborn bar plot comparing average accidents between weekdays and weekends.
    """
    if weekend_days is None:
        weekend_days = ["Samedi", "Dimanche"]
    if colors is None:
        colors = ["#E0897E", "#63B7C3"] 
    
    df = df.copy()
    
    # We create a binary "Weekend"/"Weekday" column
    df.loc[:, binary_col] = df[day_col].apply(lambda x: "Weekend" if x in weekend_days else "Weekday")
    
    # We group by day and the binary column
    day_grouped = df.groupby([day_col, binary_col], as_index=False)[value_col].sum()
    
    # We finally compute the average per type of day
    avg_accidents = day_grouped.groupby(binary_col, as_index=False)[value_col].mean()
    avg_accidents.rename(columns={value_col: "Average_Accidents"}, inplace=True)
    
    plt.figure(figsize=(8, 5))
    sns.barplot(data=avg_accidents, x=binary_col, y="Average_Accidents", hue=binary_col, palette=colors)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def plot_accidents_by_road_type(
    df,
    road_col,
    value_col,
    title="Most Common Road Type for Accidents",
    xlabel="Road Type",
    ylabel="Total Number of Accidents",
    color="tomato"
):
    """
    Plots a bar chart showing the total number of accidents by road type,
    along with the proportion of accidents each road type represents.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing accident data.

    road_col : str
        Name of the column representing road type descriptions.

    value_col : str, optional
        Name of the column representing the number of accidents.

    title : str, optional
        Title of the plot. Default is "Most Common Road Type for Accidents".

    xlabel : str, optional
        Label for the x-axis. Default is "Road Type".

    ylabel : str, optional
        Label for the y-axis. Default is "Total Number of Accidents".

    color : str, optional
        Color of the bars in the plot. Default is "tomato".

    Returns
    -------
    None
        Displays a bar chart of accident counts per road type.
    """
    
    road_counts = df.groupby(road_col, as_index=False)[value_col].sum()
    road_counts = road_counts.sort_values(by=value_col, ascending=False)
    road_counts["Proportion"] = road_counts[value_col] / road_counts[value_col].sum()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=road_counts, x=road_col, y=value_col, color=color)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def plot_accidents_by_hour(
    df,
    hour_col,
    value_col,
    title="Accident Distribution by Hour",
    xlabel="Hour of the Day",
    ylabel="Total Number of Accidents",
    color="steelblue"
):
    """
    Plots a bar chart showing the distribution of accidents by hour of the day.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing accident data.

    hour_col : str
        Name of the column representing the hour of the day (1 to 24).

    value_col : str
        Name of the column representing the number of accidents.

    title : str, optional
        Title of the plot. Default is "Accident Distribution by Hour".

    xlabel : str, optional
        Label for the x-axis. Default is "Hour of the Day".

    ylabel : str, optional
        Label for the y-axis. Default is "Total Number of Accidents".

    color : str, optional
        Bar color. Default is "steelblue".

    Returns
    -------
    None
        Displays a bar chart of total accidents per hour.
    """
    
    hourly_accidents = df.groupby(hour_col, as_index=False)[value_col].sum()

    plt.figure(figsize=(10, 5))
    sns.barplot(
        data=hourly_accidents,
        x=hour_col,
        y=value_col,
        color=color,
        edgecolor="black"
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(ticks=range(1, 25), labels=range(1, 25))
    plt.tight_layout()
    plt.show()

def plot_accidents_by_light_condition(
    df,
    light_col,
    value_col,
    title="Accidents by Light Condition",
    colors=None
):
    """
    Plots a pie chart showing the distribution of accidents by light condition.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing accident data.

    light_col : str
        Name of the column representing light conditions (e.g., daylight, night, etc.).

    value_col : str
        Name of the column representing the number of accidents.

    title : str, optional
        Title of the chart. Default is "Accidents by Light Condition".

    colors : list of str, optional
        List of custom colors for the pie chart segments.
        If None, default matplotlib colors are used.

    Returns
    -------
    None
        Displays a pie chart showing the proportion of accidents under each light condition.
    """

    light_counts = df.groupby(light_col, as_index=False)[value_col].sum()

    light_counts["Proportion"] = light_counts[value_col] / light_counts[value_col].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(
        light_counts[value_col],
        labels=light_counts[light_col],
        autopct="%1.1f%%",
        startangle=90,
        colors=colors)

    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_accident_severity_by_light_condition(
    df,
    light_col,
    severity_cols=None,
    accident_type_mapping=None,
    colors=None,
    title="Proportion of accident types by light conditions",
    xlabel="Lighting condition",
    ylabel="Proportion of accidents (%)"
):
    """
    Plots a stacked bar chart showing the proportion of accident severities by lighting condition.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing accident data.

    light_col : str, 
        Column representing lighting conditions.

    severity_cols : list of str, optional
        List of columns representing accident severity types.
        If None, uses:
            ["MS_ACCT_WITH_DEAD", "MS_ACCT_WITH_MORY_INJ",
             "MS_ACCT_WITH_SERLY_INJ", "MS_ACCT_WITH_SLY_INJ"]

    accident_type_mapping : dict, optional
        Dictionary to rename severity column names for clearer plot labels.
        If None, a default mapping is applied.

    colors : list of str, optional
        List of colors to use for each severity type in the stacked bar chart.

    title : str, optional
        Title of the plot.

    xlabel : str, optional
        Label for the x-axis.

    ylabel : str, optional
        Label for the y-axis.

    Returns
    -------
    None
        Displays a stacked bar chart showing severity proportions by light condition.
    """
    if severity_cols is None:
        severity_cols = [
            "MS_ACCT_WITH_DEAD", "MS_ACCT_WITH_MORY_INJ",
            "MS_ACCT_WITH_SERLY_INJ", "MS_ACCT_WITH_SLY_INJ"
        ]

    if accident_type_mapping is None:
        accident_type_mapping = {
            "MS_ACCT_WITH_DEAD": "Fatal accidents",
            "MS_ACCT_WITH_MORY_INJ": "Accidents with fatal injuries (30 days)",
            "MS_ACCT_WITH_SERLY_INJ": "Accidents with serious injuries",
            "MS_ACCT_WITH_SLY_INJ": "Accidents with minor injury"
        }

    if colors is None:
        colors = ["#55B4AE", "#94A653", "#E68363", "#C78FF0"]

    severity_light = df.groupby(light_col, as_index=False)[severity_cols].sum()
    severity_light = severity_light.melt(
        id_vars=[light_col],
        value_vars=severity_cols,
        var_name="Accident_Type",
        value_name="Count")
    severity_light["Total_Accidents"] = severity_light.groupby(light_col)["Count"].transform("sum")
    severity_light["Proportion"] = severity_light["Count"] / severity_light["Total_Accidents"]
    severity_light["Accident_Type"] = severity_light["Accident_Type"].replace(accident_type_mapping)

    # We create a pivot for plotting.
    severity_pivot = severity_light.pivot(
        index=light_col, columns="Accident_Type", values="Proportion")

    plt.figure(figsize=(10, 6))
    severity_pivot.plot(kind="bar", stacked=True, color=colors, edgecolor="black", figsize=(10, 6))

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Accident Type")
    plt.tight_layout()
    plt.show()