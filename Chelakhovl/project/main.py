import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class BJJTraining:
    """Represents a Brazilian Jiu-Jitsu training session."""
    def __init__(self, training_type, techniques, coach_notes):
        self.timestamp = datetime.datetime.now()
        self.training_type = training_type
        self.techniques = techniques
        self.coach_notes = coach_notes


class BJJTrainingTrackerGUI:
    """GUI application for tracking Brazilian Jiu-Jitsu training sessions."""
    def __init__(self, root):
        self.root = root
        self.root.title("BJJ Training Tracker")
        self.trainings = []

        self.create_widgets()

    def create_widgets(self):
        """Create and layout GUI widgets."""
        self.training_type_label = tk.Label(self.root, text="Training Type:")
        self.training_type_combobox = ttk.Combobox(self.root,
                                                   values=["Adult Gi", "Adult No-Gi", "Kids Gi", "Kids No-Gi"])

        self.techniques_label = tk.Label(self.root, text="Techniques:")
        self.techniques_entry = tk.Entry(self.root)

        self.coach_notes_label = tk.Label(self.root, text="Coach Notes:")
        self.coach_notes_entry = tk.Entry(self.root)

        self.record_button = tk.Button(self.root, text="Record Training", command=self.record_training)
        self.modify_button = tk.Button(self.root, text="Modify Training", command=self.modify_training)

        self.display_button = tk.Button(self.root, text="View Training History", command=self.display_trainings)

        self.delete_button = tk.Button(self.root, text="Delete Training", command=self.delete_training)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entry_fields)

        self.training_type_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.training_type_combobox.grid(row=0, column=1, padx=10, pady=5)

        self.techniques_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.techniques_entry.grid(row=1, column=1, padx=10, pady=5)

        self.coach_notes_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.coach_notes_entry.grid(row=2, column=1, padx=10, pady=5)

        self.modify_button.grid(row=3, column=0, pady=10)
        self.record_button.grid(row=3, column=1, pady=10)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.clear_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=('Time', 'Training Type', 'Techniques', 'Coach Notes'),
                                 show='headings')
        self.tree.grid(row=7, column=0, columnspan=2, pady=10)

        self.tree.heading('Time', text='Time')
        self.tree.heading('Training Type', text='Training Type')
        self.tree.heading('Techniques', text='Techniques')
        self.tree.heading('Coach Notes', text='Coach Notes')

    def record_training(self):
        """Record a new BJJ training session based on user input."""
        training_type = self.training_type_combobox.get()
        techniques = self.techniques_entry.get()
        coach_notes = self.coach_notes_entry.get()

        if not training_type or not techniques or not coach_notes:
            messagebox.showwarning("Warning", "Please fill in all fields.")
            return

        training_entry = BJJTraining(training_type, techniques, coach_notes)
        self.trainings.append(training_entry)
        self.clear_entry_fields()
        messagebox.showinfo("Information", "Training recorded!")

    def modify_training(self):
        """Modify the details of a selected training session."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a training entry to modify.")
            return

        index = self.tree.index(selected_item)
        selected_training = self.trainings[index]

        current_training_type = selected_training.training_type
        current_techniques = selected_training.techniques
        current_coach_notes = selected_training.coach_notes

        modify_window = tk.Toplevel(self.root)
        modify_window.title("Modify Training")

        modify_training_type_label = tk.Label(modify_window, text="New Training Type:")
        modify_training_type_entry = tk.Entry(modify_window)
        modify_training_type_entry.insert(0, current_training_type)

        modify_techniques_label = tk.Label(modify_window, text="New Techniques:")
        modify_techniques_entry = tk.Entry(modify_window)
        modify_techniques_entry.insert(0, current_techniques)

        modify_coach_notes_label = tk.Label(modify_window, text="New Coach Notes:")
        modify_coach_notes_entry = tk.Entry(modify_window)
        modify_coach_notes_entry.insert(0, current_coach_notes)

        save_button = tk.Button(modify_window, text="Save Changes",
                                command=lambda: self.save_changes(index, modify_window,
                                                                  modify_training_type_entry.get(),
                                                                  modify_techniques_entry.get(),
                                                                  modify_coach_notes_entry.get()))

        modify_training_type_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        modify_training_type_entry.grid(row=0, column=1, padx=10, pady=5)

        modify_techniques_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        modify_techniques_entry.grid(row=1, column=1, padx=10, pady=5)

        modify_coach_notes_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        modify_coach_notes_entry.grid(row=2, column=1, padx=10, pady=5)

        save_button.grid(row=3, column=0, columnspan=2, pady=10)

    def save_changes(self, index, modify_window, new_training_type, new_techniques, new_coach_notes):
        """Save changes made during the modification of a training session."""
        modified_training = self.trainings[index]
        modified_training.training_type = new_training_type
        modified_training.techniques = new_techniques
        modified_training.coach_notes = new_coach_notes

        self.tree.item(self.tree.selection(), values=(
            modified_training.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            modified_training.training_type, modified_training.techniques, modified_training.coach_notes))

        modify_window.destroy()

    def clear_entry_fields(self):
        """Clear the entry fields in the GUI."""
        self.training_type_combobox.set('')
        self.techniques_entry.delete(0, tk.END)
        self.coach_notes_entry.delete(0, tk.END)

    def delete_training(self):
        """Delete a selected training session."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a training entry to delete.")
            return

        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected training?")
        if confirmation:
            index = self.tree.index(selected_item)
            del self.trainings[index]
            self.tree.delete(selected_item)
            messagebox.showinfo("Information", "Training deleted.")

    def display_trainings(self):
        """Display the recorded BJJ training sessions in the GUI."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not self.trainings:
            messagebox.showinfo("Information", "You have no recorded trainings yet.")
        else:
            for training in self.trainings:
                timestamp_str = training.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                self.tree.insert('', 'end', values=(
                    timestamp_str, training.training_type, training.techniques, training.coach_notes))


def main():
    """Run the BJJ Training Tracker application."""
    root = tk.Tk()
    app = BJJTrainingTrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
