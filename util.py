import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")

       
def countplot_viz(
    df,
    xcolumn,
    xlabel,
    ylabel,
    title,
    hue=None,
    fontsize_label=16,
    fontsize_title=20,
    fontsize_text=12,
    rotation=45,
    figsize_x=12,
    figsize_y=5,
    palette="viridis",
):
    """
    This function gets a Python Pandas dataframe and visualizes a countplot.
    :param df: Dataframe to be analyze
    :param xcolumn: This column designates the x axis column.
    :param xlabel: It designates the name of the x axis column.
    :param ylabel: It designates the name of the y axis column.
    :param title: This column designates the name of the graph.
    :param hue: Name of variables in `data` or vector data, optional Inputs for plotting long-form data.
    :param fontsize_label: It designates label size.
    :param fontsize_title: It designates title size.
    :param rotation: It designates rotation of graphs.
    :param palette: It designates colors of graphs.
    :return: This function doesn't return anything.
    """
    plt.figure(figsize=(figsize_x,figsize_y))
    
    g = sns.countplot(x=xcolumn, data=df, hue=hue, palette=palette, order = df[xcolumn].value_counts().iloc[:15].index)
    g.set_title(title, fontsize=19)
    g.set_xlabel(xlabel, fontsize=17)
    g.set_ylabel(ylabel, fontsize=17)
    g.set_xticklabels(g.get_xticklabels(), rotation=40, ha="right")
    plt.tight_layout()
    for p in g.patches:
        height = p.get_height()
        g.text(
            p.get_x() + p.get_width() / 2.0,
            height + 1,
            "{:1}".format(height),
            ha="center",
            fontsize=fontsize_text,
        )    
    if hue != None:
        g.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0)  

        
def distplot_viz(
    data,
    column,
    separate_column,
    condition_1,
    condition_2,
    label1,
    label2,
    title,
    color1=None,
    color2=None,
):
    """
    Gets a Python Pandas dataframe and visualize displot by a column's conditions. It shows density of column.
    :param data: Dataframe to be analyze
    :param column: This column is for showing data distribution.
    :param separate_column: this colum is for creating histogram by a column's conditions.
    :param condition_1: It designates condition of separate column.
    :param condition_2: It designates condition of separate column.
    :param label1: It designates label by condition_1.
    :param label2: It designates label by condition_2.
    :param title: It designates title for graph.
    :param color1: It designates color for condition_1.
    :param color2: It designates color for condition_2.
    :return: This function doesn't return anything.
    """

    plt.figure(figsize=(15, 5))
    sns.distplot(
        data[data[separate_column] == condition_1][column],
        hist=False,
        kde=True,
        kde_kws={"shade": True, "linewidth": 3},
        label=label1,
    )
    sns.distplot(
        data[data[separate_column] == condition_2][column],
        hist=False,
        kde=True,
        kde_kws={"shade": True, "linewidth": 3},
        label=label2,
    )
    plt.title(title, fontsize=17)
    plt.xlabel(column, fontsize=15)
    plt.ylabel("Density", fontsize=15)
    plt.legend()

    
def countplot_pointplot_viz(
    data,
    filter_list,
    xcolumn,
    ycolumn,
    ycolumn_point,
    xlabel,
    ylabel,
    title,
    hue=None,
    fontsize_label=16,
    fontsize_title=20,
    fontsize_text=12,
    rotation=45,
    figsize_x=12,
    figsize_y=5,
    palette="mako",
):
    """
    This function gets a Python Pandas dataframe and visualize a countplot and a pointplot.
    :param data: Dataframe to be analyze
    :param filter_list: It takes conditions for filtering. 
    :param xcolumn: This column designates x axis column.
    :param ycolumn: This column separetes data by its conditions at countplot. 
    :param ycolumn_point: This column separetes data by its conditions at pointplot. 
    :param xlabel: It designates name of x axis column.
    :param ylabel: It designates name of y axis column.
    :param title: This column designates name of graph.
    :param hue: Name of variables in `data` or vector data, optional Inputs for plotting long-form data.
    :param fontsize_label: It designates label size.
    :param fontsize_title: It designates title size.
    :param rotation: It designates rotation of graph.
    :param palette: It designates colors of graph.
    :return: This function doesn't return anything.
    """    
    
    plt.figure(figsize=(figsize_x,figsize_y)) 
    
    filter_list = filter_list
    df2 = data[data[ycolumn].isin(filter_list)]
    order = df2[xcolumn].value_counts().index

    ax1 = sns.countplot(
        x=xcolumn, hue=ycolumn, data=df2, hue_order=filter_list, palette=palette
    )
    for p in ax1.patches:
        height = p.get_height()
        ax1.text(
            p.get_x() + p.get_width() / 2.0,
            height + 3,
            "{:1}".format(height),
            ha="center",
            fontsize=fontsize_text,
        )
    ax1.set_title(title, fontsize=19)
    ax1.set_xlabel(xlabel, fontsize=17)
    ax1.set_ylabel(ylabel, fontsize=17)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
    
    ax2 = ax1.twinx()
    sns.pointplot(x=xcolumn, y=ycolumn_point, data=df2, ax=ax2)

    
    
def countplot_pointplot_viz_top15(
    data,
    filter_list,
    xcolumn,
    ycolumn,
    ycolumn_point,
    xlabel,
    ylabel,
    title,
    hue=None,
    fontsize_label=16,
    fontsize_title=20,
    fontsize_text=12,
    rotation=45,
    figsize_x=12,
    figsize_y=5,
    palette="mako",
):
    """
    This function gets a Python Pandas dataframe and visualize a countplot and a pointplot.
    :param data: Dataframe to be analyze
    :param filter_list: It takes conditions for filtering. 
    :param xcolumn: This column designates x axis column.
    :param ycolumn: This column separetes data by its conditions at countplot. 
    :param ycolumn_point: This column separetes data by its conditions at pointplot. 
    :param xlabel: It designates name of x axis column.
    :param ylabel: It designates name of y axis column.
    :param title: This column designates name of graph.
    :param hue: Name of variables in `data` or vector data, optional Inputs for plotting long-form data.
    :param fontsize_label: It designates label size.
    :param fontsize_title: It designates title size.
    :param rotation: It designates rotation of graph.
    :param palette: It designates colors of graph.
    :return: This function doesn't return anything.
    """    
    
    plt.figure(figsize=(figsize_x,figsize_y)) 
    
    filter_list = filter_list
    df2 = data[data[ycolumn].isin(filter_list)]
    order = df2[xcolumn].value_counts().index

    ax1 = sns.countplot(
        x=xcolumn, hue=ycolumn, data=df2, hue_order=filter_list, palette=palette, order = data[xcolumn].value_counts().iloc[:15].index
    )
    for p in ax1.patches:
        height = p.get_height()
        ax1.text(
            p.get_x() + p.get_width() / 2.0,
            height + 3,
            "{:1}".format(height),
            ha="center",
            fontsize=fontsize_text,
        )
    ax1.set_title(title, fontsize=19)
    ax1.set_xlabel(xlabel, fontsize=17)
    ax1.set_ylabel(ylabel, fontsize=17)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
    
    ax2 = ax1.twinx()
    sns.pointplot(x=xcolumn, y=ycolumn_point, data=df2, ax=ax2, order = data[xcolumn].value_counts().iloc[:15].index)
    
    
def df_descriptive_statistics(df, column_list):
    """
    This function gets a Python Pandas dataframe and list of columns to visualize descriptive statistics about those columns.
    :param df: Dataframe to be analyze
    :param column_list: List of columns to filter out only numeric columns to use in the fuction"
    :return: This function doesn't return anything.
    """
    try:
        dummy_df = df[column_list].copy()
        print(dummy_df.describe(),
        )
        print("")
        print(f"Mode: \n", dummy_df.mode())
        print("")
    except Exception as e:
        print("Error at df_descriptive_statistics function: ", str(e))


        
def fraud_ratio_calculator_for_two_categoric_variables(
    df, categoric_column_1, categoric_column_2
):
    """
    This function gets a Python Pandas dataframe about results of two categoric varibles. 
    :param df: Dataframe to be analyze.
    :param categoric_column_1:Categoric column to calculation.
    :param categoric_column_2:Categoric column to calculation.
    :return:df.
    """
    df_main = (
        df.groupby(by=[categoric_column_1, categoric_column_2])["EVENT_LABEL_"]
        .count()
        .reset_index()
        .copy()
    )
    df_fraud = (
        df[df["EVENT_LABEL_"] == 1]
        .groupby(by=[categoric_column_1, categoric_column_2])["EVENT_LABEL_"]
        .count()
        .reset_index()
        .copy()
    )
    df_merged = pd.merge(
        df_main,
        df_fraud,
        how="left",
        on=[categoric_column_1, categoric_column_2],
        suffixes=("_all", "_fraud"),
    ).fillna(0)
    df_merged["EVENT_LABEL_fraud_ratio"] = (
        df_merged["EVENT_LABEL__fraud"] / df_merged["EVENT_LABEL__all"]
    )
    return df_merged


def fraud_ratio_calculator_for_numeric_categoric_variables(
    df, categoric_column_1, numeric_variable
):
    """
    This function gets a Python Pandas dataframe about results of two categoric varibles. 
    :param df: Dataframe to be analyze.
    :param categoric_column_1:Categoric column to calculation.
    :param categoric_column_2:Categoric column to calculation.
    :param numeric_variable:Numeric column to calculation.
    :return:df.
    """
    df_main = (
        df.groupby(by=[categoric_column_1])[numeric_variable]
        .sum()
        .reset_index()
        .copy()
    )
    df_fraud = (
        df[df["EVENT_LABEL_"] == 1]
        .groupby(by=[categoric_column_1])[numeric_variable]
        .sum()
        .reset_index()
        .copy()
    )
    df_merged = pd.merge(
        df_main,
        df_fraud,
        how="left",
        on=[categoric_column_1],
        suffixes=("_total", "_fraud"),
    ).fillna(0)

    numeric_total = numeric_variable + "_total"
    fraud_total = numeric_variable + "_fraud"

    df_merged["numeric_fraud_ratio"] = df_merged[fraud_total] / df_merged[numeric_total]

    return df_merged