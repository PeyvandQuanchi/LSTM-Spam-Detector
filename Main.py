from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PySide6.QtCore import Qt
from MainMenu_ui import Ui_MainMenu
from Spam_Result_ui import Ui_Result
from Ham_Result_ui import Ui_Form
import tensorflow as tf
import pickle
import sys, os

def resource_path(relative_path: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

with open(resource_path("vectorizer_vocab.pkl"), 'rb') as f:
    vocabulary = pickle.load(f)


model = tf.keras.models.load_model(resource_path('spam_model.h5'))


def fix_text_vectorization_layer(model, vocabulary):

    for layer in model.layers:
        if isinstance(layer, tf.keras.layers.TextVectorization):

            layer.set_vocabulary(vocabulary)
            print("TextVectorization layer fixed with vocabulary")
            break
    else:
        print("No TextVectorization layer found in the model")
    
    return model


model = fix_text_vectorization_layer(model, vocabulary)

def predict_spam(text):
    if not text.strip():
        return (0, 1.0)


    text_tensor = tf.constant([text]) 
    
    prob = model.predict(text_tensor)[0][0]
    
    if prob > 0.5:
        return (1,prob)
    else:
        return (0, 1 - prob)

class Spam_Result_Window(QDialog):
    def __init__(self, parent=None, message=""):
        super().__init__(parent)
        self.ui = Ui_Result()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        if hasattr(self.ui, "label_result"):
            self.ui.label_result.setText(message)


class Ham_Result_Window(QDialog):
    def __init__(self, parent=None, message=""):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        if hasattr(self.ui, "label_result"):
            self.ui.label_result.setText(message)

        

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_check_clicked)




    def on_check_clicked(self):
        text = self.ui.lineEdit.text()
        try:
            result = predict_spam(str(text))
            print(result)
            if (result[0] == 1):
                dlg = Spam_Result_Window(self, "")

            elif (result[0] == 0):
                dlg = Ham_Result_Window(self, "")
            conf_label = getattr(dlg.ui, "Confidence", None)
            if conf_label is not None:
                 if (result[1] > 0.5):
                    conf_label.setText(f"Confidence Level: {result[1]:.2f}")
                 else:
                    conf_label.setText(f"Confidence Level: {1 - result[1]:.2f}")

            dlg.exec()

                
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.ui.lineEdit.setText("")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()