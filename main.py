from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from pyzbar.pyzbar import decode
from PIL import Image as PILImage
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.modalview import ModalView


class ScannerWindow(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.8, 0.8)
        self.auto_dismiss = True

        # Layout pour la fenêtre de scan
        layout = BoxLayout(orientation='vertical', padding=10)

        # Ajout d'un explorateur de fichiers
        self.file_chooser = FileChooserIconView()
        layout.add_widget(self.file_chooser)

        # Bouton pour scanner l'image sélectionnée
        scan_button = Button(
            text='Scanner l\'image sélectionnée',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1)
        )
        scan_button.bind(on_press=self.scan_image)
        layout.add_widget(scan_button)

        # Bouton pour fermer la fenêtre
        close_button = Button(
            text='Fermer',
            size_hint=(1, 0.2),
            background_color=(0.7, 0.3, 0.2, 1)
        )
        close_button.bind(on_press=self.dismiss)
        layout.add_widget(close_button)

        self.add_widget(layout)

    def scan_image(self, instance):
        selected_path = self.file_chooser.selection
        if selected_path:
            # Charger l'image et scanner les QR codes
            image = PILImage.open(selected_path[0])
            decoded_objects = decode(image)

            if decoded_objects:
                for obj in decoded_objects:
                    data = obj.data.decode('utf-8')
                    print(f"QR Code détecté : {data}")
            else:
                print("Aucun QR Code détecté.")

        else:
            print("Aucune image sélectionnée.")

class MainApp(App):
    def build(self):
        # Créer un layout vertical
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ajouter un titre
        title = Label(
            text='Gestion de Stock',
            size_hint=(1, 0.2),
            font_size='24sp'
        )
        layout.add_widget(title)

        # Créer les trois boutons
        btn_entree = Button(
            text='Entrée',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.7, 0.3, 1)  # Vert
        )
        btn_entree.bind(on_press=self.on_entree_press)

        btn_sortie = Button(
            text='Sortie',
            size_hint=(1, 0.2),
            background_color=(0.7, 0.3, 0.2, 1)  # Rouge
        )
        btn_sortie.bind(on_press=self.on_sortie_press)

        btn_inventaire = Button(
            text='Inventaire',
            size_hint=(1, 0.2),
            background_color=(0.2, 0.3, 0.7, 1)  # Bleu
        )
        btn_inventaire.bind(on_press=self.on_inventaire_press)

        # Ajouter les boutons au layout
        layout.add_widget(btn_entree)
        layout.add_widget(btn_sortie)
        layout.add_widget(btn_inventaire)

        return layout

    def on_entree_press(self, instance):
        # Ouvrir la fenêtre de scan
        scanner = ScannerWindow()
        scanner.open()

    def on_sortie_press(self, instance):
        print("Bouton Sortie cliqué")

    def on_inventaire_press(self, instance):
        print("Bouton Inventaire cliqué")


if __name__ == '__main__':
    MainApp().run()
