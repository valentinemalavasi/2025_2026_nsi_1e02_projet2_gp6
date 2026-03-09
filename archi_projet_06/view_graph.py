import matplotlib.pyplot as plt

def graphique_evolution(ax, data, type_graph):
    """
    Crée un graphique d'évolution (courbe ou bâton).
    
    Args:
        ax: Axes matplotlib
        data: DataFrame contenant les colonnes 'annee' et 'nombre'
        type_graph: Type de graphique demandé ("Courbes" ou "Barres")
    
    Raises:
        ValueError: Si le type de graphique n'est pas valide
        Exception: Si les données ne peuvent pas être converties
    """
    if type_graph not in ["Courbes", "Barres"]:
        raise ValueError(f"Type de graphique invalide : '{type_graph}'. Doit être 'Courbes' ou 'Barres'.")
    
    try:
        annees = data["annee"].astype(int).tolist()
        valeurs = data["nombre"].tolist()
        
        if not annees or not valeurs:
            raise ValueError("Les données sont vides. Impossible de créer un graphique.")
        
        if type_graph == "Courbes":
            # Affichage en courbe
            ax.plot(annees, valeurs, marker="o", color="red", linewidth=2, markersize=8)
            for x, y in zip(annees, valeurs):
                ax.annotate(f"{y:,}", (x, y), textcoords="offset points",
                            xytext=(0, 10), ha="center")
        else:  # type_graph == "Barres"
            # Affichage en bâton
            ax.bar(annees, valeurs, color="green", edgecolor="black", linewidth=1.5)
            for i, v in enumerate(valeurs):
                ax.text(annees[i], v + max(valeurs)*0.01, f"{v:,}", ha="center")
        
        ax.set_title("Évolution des crimes", fontsize=14, fontweight="bold")
        ax.set_xlabel("Année", fontsize=12)
        ax.set_ylabel("Nombre de crimes", fontsize=12)
        ax.grid(axis="y", alpha=0.3)
        plt.xticks(annees, rotation=45)
        plt.tight_layout()
        
    except KeyError as e:
        raise ValueError(f"Colonne manquante dans les données : {e}")
    except Exception as e:
        raise Exception(f"Erreur lors de la création du graphique d'évolution : {str(e)}")


def graphique_repartition(ax, data, type_graph):
    """
    Crée un graphique de répartition (camembert ou bâton).
    
    Args:
        ax: Axes matplotlib
        data: DataFrame contenant les colonnes 'indicateur' et 'nombre'
        type_graph: Type de graphique demandé ("Camembert" ou "Barres")
    
    Raises:
        ValueError: Si le type de graphique n'est pas valide
        Exception: Si les données ne peuvent pas être converties
    """
    if type_graph not in ["Camembert", "Barres"]:
        raise ValueError(f"Type de graphique invalide : '{type_graph}'. Doit être 'Camembert' ou 'Barres'.")
    
    try:
        labels = data["indicateur"].tolist()
        valeurs = data["nombre"].tolist()
        
        if not labels or not valeurs:
            raise ValueError("Les données sont vides. Impossible de créer un graphique.")
        
        if type_graph == "Camembert":
            # Affichage en camembert
            ax.pie(valeurs, labels=labels, autopct="%1.1f%%", startangle=90)
            ax.set_title("Répartition des crimes", fontsize=14, fontweight="bold")
        else:  # type_graph == "Barres"
            # Affichage en bâton
            ax.bar(range(len(labels)), valeurs, color="green", edgecolor="black", linewidth=1.5)
            ax.set_xticks(range(len(labels)))
            ax.set_xticklabels(labels, rotation=45, ha="right")
            ax.set_title("Top 10 des crimes", fontsize=14, fontweight="bold")
            ax.grid(axis="y", alpha=0.3)
            
            for i, v in enumerate(valeurs):
                ax.text(i, v + max(valeurs)*0.01, f"{v:,}", ha="center")
        
        plt.tight_layout()
        
    except KeyError as e:
        raise ValueError(f"Colonne manquante dans les données : {e}")
    except Exception as e:
        raise Exception(f"Erreur lors de la création du graphique de répartition : {str(e)}")