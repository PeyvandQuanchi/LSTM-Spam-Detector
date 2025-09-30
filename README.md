This project implements a deep learning-based email classifier using TensorFlow and Keras. It utilizes an **LSTM (Long Short-Term Memory)** neural network model to classify emails as **spam** or **not spam**. By leveraging sequential patterns in text, the model accurately predicts whether a given email message is spam or not.

## Key Features

- **Text Preprocessing:**  
  - Uses **TextVectorization** for tokenizing and normalizing the text input. 
  - Transforms words into dense embeddings for effective word representation.
  
- **Deep Learning Model:**  
  - The core of the model is built using an **LSTM** (Long Short-Term Memory) network, which captures long-term dependencies in text sequences.
  - **GlobalMaxPooling** is applied to the output of the LSTM to extract the most important features from the message sequences.

- **User Interface (UI):**  
  - The project includes a **PySide6** Qt-based graphical user interface, making it user-friendly for interacting with the model.
  - The interface allows users to easily input new email text and classify them interactively as **spam** or **not spam**.

- **Prediction Functionality:**  
  - A simple **predict function** is provided, enabling users to classify new email messages by entering text directly into the UI.



## LSTM Network Architecture:
The model is built using the Keras API and includes the following layers:

Embedding Layer: Transforms text into dense word representations.

LSTM Layer: Captures sequential dependencies in the text to identify patterns that differentiate spam from non-spam messages.

GlobalMaxPooling Layer: Reduces the output dimension of the LSTM layer while retaining the most important features.

Dense Layer: Fully connected layer used for final classification (spam or not spam).

## Training:
The model is trained on a labeled dataset of spam and non-spam emails. The dataset is preprocessed, and the text is tokenized before being fed into the LSTM network. Once trained, the model is able to make accurate predictions based on new input messages.

## Usage

Once the application is running, you can interact with it by entering a new email message into the provided text box. The model will predict whether the email is spam or not spam, and the result will be displayed immediately on the UI.


## Dependencies

This project requires the following Python packages:

- TensorFlow

- Keras

- PySide6

- NumPy

<img width="1124" height="783" alt="Main Menu" src="https://github.com/user-attachments/assets/7b4f6e1a-7792-4945-81ea-b8b626e46535" />
<img width="766" height="462" alt="Ham Result" src="https://github.com/user-attachments/assets/1f2984ad-78f4-4727-ad01-8402dc783e4d" />
<img width="766" height="434" alt="Spam Result" src="https://github.com/user-attachments/assets/7cbe2c63-23c8-4a04-b84e-35009ed35933" />




