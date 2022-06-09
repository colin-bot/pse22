class Chat:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.latest_message_id = 0
        self.message_list = []

    def create_message(self, user_id, time, message):
        self.message_list.append(
            (time, self.latest_message_id, user_id, message)
        )
        self.latest_message_id += 1
        # Sorteer message_list

    def get_dictionary(self):
        return {self.chat_id: self.message_list}
