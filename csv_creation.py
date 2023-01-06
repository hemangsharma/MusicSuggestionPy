import pandas as pd

# Create a dictionary with the data
data = {'tempo': [100, 120, 150, 140, 130, 110, 90],
        'loudness': [-5, -3, -1, 0, 2, 3, 5],
        'valence': [0.2, 0.5, 0.8, 0.7, 0.6, 0.4, 0.1],
        'energy': [0.5, 0.7, 0.9, 0.8, 0.7, 0.5, 0.3],
        'mood': ['sad', 'happy', 'happy', 'happy', 'happy', 'sad', 'sad']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("music_data.csv", index=False)


'''This code will create a DataFrame containing the song data, and will
save the DataFrame to a CSV file called "music_data.csv". The file will
contain columns for the tempo, loudness, valence, energy, and mood of
each song.'''
