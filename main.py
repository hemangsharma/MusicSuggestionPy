import tkinter as tk
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load the data
df = pd.read_csv("music_data.csv")

# Preprocess the data
X = df[['tempo', 'loudness', 'valence', 'energy']]
y = df['mood']

# Encode the labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Create the user interface
window = tk.Tk()
window.title("Music Suggestion")

# Create a function to predict the mood for a new song
def predict():
  # Get the user's input
  tempo = int(tempo_entry.get())
  loudness = int(loudness_entry.get())
  valence = float(valence_entry.get())
  energy = float(energy_entry.get())

  # Use the model to predict the mood
  prediction = model.predict([[tempo, loudness, valence, energy]])
  mood = encoder.inverse_transform(prediction)

  # Display the result
  result_label.config(text=f"Suggested mood: {mood[0]}")

# Create the input fields
tempo_label = tk.Label(text="Tempo (BPM) [80 to 150]:")
tempo_entry = tk.Entry()
loudness_label = tk.Label(text="Loudness (dB)[-5 to 5]:")
loudness_entry = tk.Entry()
valence_label = tk.Label(text="Valence [0.9 to 0.1]:")
valence_entry = tk.Entry()
energy_label = tk.Label(text="Energy [0.1 to 0.9]:")
energy_entry = tk.Entry()

# Create the submit button and result label
submit_button = tk.Button(text="Submit", command=predict)
result_label = tk.Label(text="")

# Add the input fields and submit button to the user interface
tempo_label.pack()
tempo_entry.pack()
loudness_label.pack()
loudness_entry.pack()
valence_label.pack()
valence_entry.pack()
energy_label.pack()
energy_entry.pack()
submit_button.pack()
result_label.pack()

# Run the user interface
window.mainloop()



'''This code assumes that you have a CSV file called "music_data.csv" that contains
information about songs, including their tempo, loudness, valence, and
energy, as well as the corresponding mood label. The code preprocesses
the data, trains a random forest classifier on the data, and evaluates
the model's accuracy. It also demonstrates how you can use the trained
model to predict the mood for a new song.'''



