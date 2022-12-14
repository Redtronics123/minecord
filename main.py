from nextcord.ext import commands
import os
import json


class Minecord(commands.Bot):
    def __init__(self):
        super().__init__()

    def main(self):

        # bot requirements
        with open("config.json", "r") as f:
            config = json.load(f)
            token: str = config["token"]

        self.remove_command("help")
        self.intents.all()
        print("Config loaded")

        for directory_commands in os.listdir("src/commands"):
            for file_commands in os.listdir(f"src/commands/{directory_commands}"):
                if file_commands.endswith(".py"):
                    self.load_extension(f"src.commands.{directory_commands}.{file_commands[:-3]}")

        for directory_listeners in os.listdir("src/listeners"):
            for file_listeners in os.listdir(f"src/listeners/{directory_listeners}"):
                if file_listeners.endswith(".py"):
                    self.load_extension(f"src.listeners.{directory_listeners}.{file_listeners[:-3]}")

        for directory_tasks in os.listdir("src/tasks"):
            for file_tasks in os.listdir(f"src/tasks/{directory_tasks}"):
                if file_tasks.endswith(".py"):
                    self.load_extension(f"src.tasks.{directory_tasks}.{file_tasks[:-3]}")
        print("Extensions loaded")

        self.run(token)


if __name__ == "__main__":
    Minecord().main()
