import Character_basic_data

api_key = "live_454c2b1ff9fd60b4ab2ee265c9f236ba3dfb7f486da0b6c3f76999ce002754e2efe8d04e6d233bd35cf2fabdeb93fb0d"
character_name = "리마"

character_data = Character_basic_data.get_character_data(character_name, api_key)
character_nickname = character_data.get('character_name')
print(character_nickname)