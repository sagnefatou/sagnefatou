import json
import tkinter as tk

# 🔹 Fonction pour charger les questions du quiz
def load_quiz_data(file_path):
    """Charge les données du quiz depuis un fichier JSON."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)  # Lire le fichier JSON
            return data if isinstance(data, list) else []  # Vérifier que les données sont bien une liste
    except Exception as e:
        print(f"❌ Erreur de chargement du fichier JSON : {e}")
        return []  # Retourner une liste vide en cas d'erreur

# 🔹 Classe Quiz pour suivre le score et la progression
class Quiz:
    def __init__(self, questions):
        """Initialisation du quiz avec suivi du score et de la progression"""
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.total_questions = len(questions)

    def next_question(self):
        """Passer à la question suivante"""
        self.current_question_index += 1

    def update_score(self, correct):
        """Mettre à jour le score"""
        if correct:
            self.score += 1

    def quiz_finished(self):
        """Vérifier si le quiz est terminé"""
        return self.current_question_index >= self.total_questions

# 🔹 Classe FishQuiz pour afficher le quiz avec Tkinter
class FishQuiz:
    def __init__(self, root, file_path):
        """Initialisation du quiz avec interface graphique"""
        self.root = root  
        self.file_path = file_path  

        # Charger les données du quiz
        questions_data = load_quiz_data(file_path)
        if not questions_data:
            self.label_error = tk.Label(self.root, text="⚠️ Erreur: Impossible de charger le quiz!", font=("Arial", 12), fg="red")
            self.label_error.pack()
            return

        self.quiz = Quiz(questions_data)  # Création du quiz avec les questions
        self.setup_ui()

    def setup_ui(self):
        """Configuration de l’interface utilisateur"""
        self.label_question = tk.Label(self.root, text="", font=("Arial", 14))
        self.label_question.pack()

        # Variable pour stocker la réponse sélectionnée
        self.selected_option = tk.StringVar()
        
        # Boutons radio pour les réponses
        self.radio_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("Arial", 12))
            self.radio_buttons.append(btn)
            btn.pack()

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback_label.pack()

        self.btn_submit = tk.Button(self.root, text="Valider", command=self.check_answer, font=("Arial", 12))
        self.btn_submit.pack()

        self.update_ui()

    def update_ui(self):
        """Mettre à jour l'affichage de la question et des options"""
        self.feedback_label.config(text="")  # Réinitialiser le feedback
        if not self.quiz.quiz_finished():
            question_info = self.quiz.questions[self.quiz.current_question_index]
            self.label_question.config(text=question_info["question"])
            
            for i, option in enumerate(question_info["options"]):
                self.radio_buttons[i].config(text=option, value=option)  # Mettre à jour les textes des boutons radio
        else:
            self.show_results()

    def compare_answer(self):
        """Comparer la réponse sélectionnée avec la bonne réponse"""
        selected_option = self.selected_option.get()
        
        if selected_option:
            correct_answer = self.quiz.questions[self.quiz.current_question_index]["answer"]
            if selected_option == correct_answer:
                self.feedback_label.config(text="✅ Bonne réponse!", fg="green")
                self.quiz.update_score(True)  # Met à jour le score
            else:
                self.feedback_label.config(text=f"❌ Mauvaise réponse! La bonne réponse était : {correct_answer}", fg="red")

            # Passer à la question suivante après un court délai
            self.root.after(1000, self.next_question)

    def check_answer(self):
        """Vérifier et comparer la réponse"""
        self.compare_answer()

    def next_question(self):
        """Passer à la question suivante après un délai"""
        self.quiz.next_question()
        self.update_ui()

    def show_results(self):
        """Afficher le score final"""
        self.label_question.config(text=f"🎉 Quiz terminé! Score: {self.quiz.score}/{self.quiz.total_questions}")
        for btn in self.radio_buttons:
            btn.pack_forget()
        self.btn_submit.pack_forget()
        self.feedback_label.config(text="")

# 🔹 Lancer l'interface graphique
if __name__ == "__main__":
    root = tk.Tk()
    root.title("FishEasy Quiz")
    quiz = FishQuiz(root, "quiz_questions.json")  
    root.mainloop()