import tkinter as tk
from tkinter import ttk
import requests

class RecipeApp:
    def __init__(self, root):
        self.root = root
        root.title("Recipe App")

        # Options de saison
        self.season_label = tk.Label(root, text="Choisissez la saison :")
        self.season_label.pack()

        self.season_combobox = ttk.Combobox(root, values=["Hiver", "Printemps", "Été", "Automne"])
        self.season_combobox.pack()

        # Options de type de plat
        self.type_label = tk.Label(root, text="Choisissez le type de plat :")
        self.type_label.pack()

        self.type_combobox = ttk.Combobox(root, values=["Salé", "Sucré"])
        self.type_combobox.pack()

        # Options de restrictions alimentaires
        self.restrictions_label = tk.Label(root, text="Choisissez vos restrictions alimentaires :")
        self.restrictions_label.pack()

        self.restrictions_entry = tk.Entry(root)
        self.restrictions_entry.pack()

        # Bouton pour obtenir les recettes
        get_recipes_button = tk.Button(root, text="Obtenir les recettes", command=self.get_recipes)
        get_recipes_button.pack(pady=10)

        # Zone de texte défilante pour afficher les recettes
        self.recipes_text = tk.Text(root, width=60, height=10)
        self.recipes_text.pack(pady=10)

    def get_recipes(self):
        # Récupérer les options choisies par l'utilisateur
        selected_season = self.season_combobox.get()
        selected_type = self.type_combobox.get()
        restrictions = self.restrictions_entry.get()

        # Appeler l'API (remplace avec ton URL et tes paramètres)
        api_url = "https://api.example.com/recipes"
        params = {
            "season": selected_season,
            "type": selected_type,
            "restrictions": restrictions
        }

        response = requests.get(api_url, params=params)

        # Vérifier si la requête a réussi (statut code 200)
        if response.status_code == 200:
            # Convertir la réponse en format JSON
            recipes = response.json()["recipes"]

            # Afficher les recettes dans la zone de texte défilante
            self.recipes_text.delete(1.0, tk.END)  # Effacer le texte précédent
            for recipe in recipes:
                self.recipes_text.insert(tk.END, f"{recipe['name']}\n{recipe['instructions']}\n\n")
        else:
            error_message = f"Erreur lors de la requête. Code d'erreur : {response.status_code}"
            self.recipes_text.delete(1.0, tk.END)
            self.recipes_text.insert(tk.END, error_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
