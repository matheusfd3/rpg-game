class Character:
  def __init__(self, name, health, level) -> None:
    self.__name = name
    self.__health = health
    self.__level = level

  def get_name(self):
    return self.__name
  
  def get_health(self):
    return self.__health
  
  def get_level(self):
    return self.__level
  
  def show_info(self):
    return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"
  
class Hero(Character):
  def __init__(self, name, health, level, skill) -> None:
    super().__init__(name, health, level)
    self.__skill = skill

  def get_skill(self):
    return self.__skill
  
  def show_info(self):
    return f"{super().show_info()}\nSkill: {self.get_skill()}\n"
  
class Enemy(Character):
  def __init__(self, name, health, level, kind) -> None:
    super().__init__(name, health, level)
    self.__kind = kind

  def get_kind(self):
    return self.__kind
  
  def show_info(self):
    return f"{super().show_info()}\nKind: {self.get_kind()}\n"
  
hero = Hero(name="Herói", health=100, level=5, skill="Super Força")
print(hero.show_info())
enemy = Enemy(name="Morcego", health=50, level=3, kind="Voador")
print(enemy.show_info())