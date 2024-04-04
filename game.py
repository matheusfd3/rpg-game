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
  
class Game:
  """ Classe orquestradora do jogo """

  def __init__(self) -> None:
    self.hero = Hero(name="Herói", health=100, level=5, skill="Super Força")
    self.enemy = Enemy(name="Morcego", health=50, level=3, kind="Voador")
  
  def start_battle(self):
    """ Fazer a gestão da batalha em turnos """
    print("Iniciando batalha!")
    while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
      print("\nDetalhes dos Personagens:")
      print(self.hero.show_info())
      print(self.enemy.show_info())

      input("Pressione Enter para atacar...")
      choice = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

game = Game()
game.start_battle()