import os
import json


DATA_FILE = "data.json"
data = None


def init():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            file.write(json.dumps([]))


def load():
    with open(DATA_FILE) as file:
        global data
        data = json.load(file)


def save():
    with open(DATA_FILE, "w") as file:
        file.write(json.dumps(data, indent=4))


init()
load()


def get_subscriptions():
    servers = {}
    for item in data:
        servers[item["server_id"]] = item["active"]
    return servers


def get_server_index(guild_id):
    index = 0
    while index < len(data):
        if data[index]["server_id"] == guild_id:
            return index
        index = index + 1
    return -1


def add_server(name, id):
    if get_server_index(id) >= 0:
        return "The server is already registered."
    data.append(
        {
            "name": name,
            "server_id": id,
            "active": True,
        }
    )
    save()
    return id


def edit_server(id, active):
    index = get_server_index(id)
    if index == -1:
        return "No server found with this id."
    data[index]["active"] = active
    save()
    return id


def remove_server(id):
    index = get_server_index(id)
    if index == -1:
        return "No server found with this id."
    data.pop(index)
    save()
    return id


def set_welcome_channel_id(guild_id, channel_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["welcome_channel_id"] = channel_id
        save()
        return channel_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_welcome_channel_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["welcome_channel_id"]
    except Exception as e:
        return None


def set_free_games_channel_id(guild_id, channel_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["free_games_channel_id"] = channel_id
        save()
        return channel_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_free_games_channel_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["free_games_channel_id"]
    except Exception as e:
        return None


def set_free_games_role_id(guild_id, role_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["free_games_role_id"] = role_id
        save()
        return role_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_free_games_role_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["free_games_role_id"]
    except Exception as e:
        return None


def set_dst_role_id(guild_id, role_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["dst_role_id"] = role_id
        save()
        return role_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_dst_role_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["dst_role_id"]
    except Exception as e:
        return None


def set_epic_games_names(guild_id, games):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["epic_games"] = games
        save()
        return games
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_epic_games_names(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["epic_games"]
    except Exception as e:
        return []


def set_klei_links(guild_id, links):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["klei_links"] = links
        save()
        return links
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_klei_links(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["klei_links"]
    except Exception as e:
        return []


def set_member_count_channel_id(guild_id, channel_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["member_count_channel_id"] = channel_id
        save()
        return channel_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_member_count_channel_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["member_count_channel_id"]
    except Exception as e:
        return None


def set_role_message_id(guild_id, message_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["set_role_message_id"] = message_id
        save()
        return message_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_role_message_id(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["set_role_message_id"]
    except Exception as e:
        return None


def set_role_emoji(guild_id, emoji_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."
        data[index]["set_role_emoji"] = emoji_id
        save()
        return emoji_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_role_emoji(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["set_role_emoji"]
    except Exception as e:
        return None


def add_yt_notif_rule(guild_id, yt_channel_id, discord_channel_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."

        if not data[index].get("yt_notif_rules"):
            data[index]["yt_notif_rules"] = {}

        rules = data[index]["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id in rules:
            if rules[yt_channel_id]["discord_channel_id"] == discord_channel_id:
                return "This rule already exists."
            else:
                rules[yt_channel_id]["discord_channel_id"] = discord_channel_id
                save()
                return "Updated."

        rules[yt_channel_id] = {
            "discord_channel_id": discord_channel_id,
            "last_video_id": None,
        }
        save()
        return yt_channel_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def get_yt_notif_rules(guild_id):
    try:
        for item in data:
            if item["server_id"] == guild_id:
                return item["yt_notif_rules"]
    except Exception:
        return None


def set_yt_last_video_id(guild_id, yt_channel_id, video_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."

        if not data[index].get("yt_notif_rules"):
            return "The server has no Youtube notification rules defined."

        rules = data[index]["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id not in rules:
            return "The server has no rules defined for this Youtube channel."

        if rules[yt_channel_id]["last_video_id"] == video_id:
            return "Unchanged."
        else:
            rules[yt_channel_id]["last_video_id"] = video_id
            save()
            return video_id

    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"


def remove_yt_notif_rule(guild_id, yt_channel_id):
    try:
        index = get_server_index(guild_id)
        if index == -1:
            return "No server found with this id."

        if not data[index].get("yt_notif_rules"):
            data[index]["yt_notif_rules"] = {}

        rules = data[index]["yt_notif_rules"]
        yt_channel_id = str(yt_channel_id)

        if yt_channel_id not in rules:
            return "No rule is set for this Youtube channel."

        data[index]["yt_notif_rules"].pop(yt_channel_id)
        save()
        return yt_channel_id
    except Exception as e:
        print(e)
        return f"Error happened: {str(e)}"
