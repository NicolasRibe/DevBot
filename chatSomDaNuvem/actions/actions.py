from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionFornecerSuporte(Action):
    def name(self) -> str:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain) -> list:
        problema = tracker.get_slot("problema")
        
        if problema == "acesso":
            dispatcher.utter_message(text="Parece que você está tendo problemas para acessar sua conta. Vamos tentar uma solução. Tente redefinir sua senha no link abaixo: [https://accounts.spotify.com/pt-BR/password-reset].")
        elif problema == "plano":
            dispatcher.utter_message(text="Se deseja mudar seu plano, temos algumas opções disponíveis. Você pode conferir os planos [aqui](https://www.spotify.com/br-pt/premium/).")
        elif problema == "aplicativo":
            dispatcher.utter_message(text="Lamento saber que o aplicativo não está funcionando. Tente fechar e reabrir o aplicativo. Se o problema persistir, acesse o link do nosso suporte [https://support.spotify.com/br-pt/].")
        elif problema == "abre":
            dispatcher.utter_message(text="Siga o passo a passo: 1- Feche o aplicativo; 2- Reinicie o celular; Após reiniciar tente abrir novamente;")
        elif problema == "fecha":
             dispatcher.utter_message(text="Siga o passo a passo: 1- Feche o aplicativo; 2- Reinicie o celular; Após reiniciar tente abrir novamente;")
        else:
            dispatcher.utter_message(text="Parece que seu problema é um pouco mais complexo. Vou encaminhá-lo para um atendente humano para que ele possa ajudar melhor. Um momento, por favor...")

        return []
