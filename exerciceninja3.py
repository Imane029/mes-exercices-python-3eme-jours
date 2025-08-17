class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  # Historique des appels
        self.messages = []      # Historique des messages

    def call(self, other_phone):
        """Simuler un appel et l’enregistrer"""
        call_str = f"{self.phone_number} a appelé {other_phone.phone_number}"
        print(call_str)
        self.call_history.append(call_str)

    def show_call_history(self):
        """Afficher l’historique des appels"""
        if not self.call_history:
            print("Aucun appel enregistré.")
        else:
            print("Historique des appels :")
            for call in self.call_history:
                print(f"- {call}")

    def send_message(self, other_phone, content):
        """Envoyer un message"""
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        print(f"Message envoyé à {other_phone.phone_number} : {content}")

    def show_outgoing_messages(self):
        """Afficher les messages envoyés"""
        outgoing = [m for m in self.messages if m["from"] == self.phone_number]
        if not outgoing:
            print("Aucun message envoyé.")
        else:
            print("Messages envoyés :")
            for msg in outgoing:
                print(f"À {msg['to']} : {msg['content']}")

    def show_incoming_messages(self):
        """Afficher les messages reçus"""
        incoming = [m for m in self.messages if m["to"] == self.phone_number]
        if not incoming:
            print("Aucun message reçu.")
        else:
            print("Messages reçus :")
            for msg in incoming:
                print(f"De {msg['from']} : {msg['content']}")

    def show_messages_from(self, number):
        """Afficher les messages d’un numéro spécifique"""
        filtered = [m for m in self.messages if m["from"] == number]
        if not filtered:
            print(f"Aucun message de {number}.")
        else:
            print(f"Messages de {number} :")
            for msg in filtered:
                print(f"- {msg['content']}")


# --- Test du code ---
phone1 = Phone("0612345678")
phone2 = Phone("0698765432")

# Test appels
phone1.call(phone2)
phone1.call(phone2)
phone1.show_call_history()

print("\n")

# Test messages
phone1.send_message(phone2, "Salut, ça va ?")
phone1.send_message(phone2, "RDV demain à 10h.")
phone2.send_message(phone1, "Oui ça va, merci !")

print("\n--- Historique des messages ---")
phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from("0698765432")
