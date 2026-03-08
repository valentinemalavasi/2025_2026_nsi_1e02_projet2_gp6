import matplotlib.pyplot as plt

def graphique_evolution(ax, data, type_graph):
    annees = data["annee"].astype(int).tolist()
    valeurs = data["nombre"].tolist()

    if type_graph == "Courbes":
        ax.plot(annees, valeurs, marker="o", color="red")
        for x, y in zip(annees, valeurs):
            ax.annotate(f"{y:,}", (x, y), textcoords="offset points",
                        xytext=(0, 10), ha="center")
    else:
        ax.bar(annees, valeurs, color="green")
        for i, v in enumerate(valeurs):
            ax.text(annees[i], v + max(valeurs)*0.01, f"{v:,}", ha="center")

    ax.set_title("Évolution des crimes")
    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre de crimes")
    ax.grid(axis="y", alpha=0.3)
    plt.xticks(annees, rotation=45)
    plt.tight_layout()

def graphique_repartition(ax, data, type_graph):
    labels = data["indicateur"].tolist()
    valeurs = data["nombre"].tolist()

    if type_graph == "Camembert":
        ax.pie(valeurs, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.set_title("Répartition des crimes")
    else:
        ax.bar(range(len(labels)), valeurs, color="green")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right")
        ax.set_title("Top 10 des crimes")
        ax.grid(axis="y", alpha=0.3)

        for i, v in enumerate(valeurs):
            ax.text(i, v + max(valeurs)*0.01, f"{v:,}", ha="center")

    plt.tight_layout()