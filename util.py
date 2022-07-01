import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")

def sessions_final_df_cleaning(sessions_final_df,channel_list):
    """
    This function gathers a list from the user to parse the data frame to include the given channels.
    :param channel_list: Channel list object to be parsed
    :return: Dataframe
    """
    sessions_final_df_correct_channels = sessions_final_df[
        sessions_final_df["channel"].isin(channel_list)
    ].copy()

    del sessions_final_df_correct_channels["Unnamed: 0"]

    return sessions_final_df_correct_channels

       
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

        
def countplot_viz_unlimit(
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
    
    g = sns.countplot(x=xcolumn, data=df, hue=hue, palette=palette,  order = df[xcolumn].value_counts().index)
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

    
