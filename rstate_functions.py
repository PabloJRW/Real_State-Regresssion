import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de distribución de frecuencias
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
def distPlotter(df):

    columnas_numeric = df.select_dtypes(include=['float64', 'int']).columns
    n_cols = df.shape[1]

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 6))
    axes = axes.flat


    for i, colum in enumerate(columnas_numeric):
        sns.histplot(
        data    = df,
        x       = colum,
        stat    = "count",
        kde     = True,
        color   = (list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],
        line_kws= {'linewidth': 2},
        alpha   = 0.3,
        ax      = axes[i]
    )
        axes[i].set_title(colum, fontsize = 12, fontweight = "bold")
        axes[i].tick_params(labelsize = 9)
        axes[i].set_xlabel("")
    
    
    fig.tight_layout()
    plt.subplots_adjust(top = 0.9)
    fig.suptitle('Distribución variables numéricas', fontsize = 15, fontweight = "bold");
