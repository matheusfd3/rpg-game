import random

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
  
  def attack(self, target):
    damage = random.randint(self.get_level() * 2, self.get_level() * 4)
    target.receive_damage(damage)
    print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")

  def receive_damage(self, damage):
    self.__health -= damage
    if self.__health < 0:
      self.__health = 0
class Hero(Character):
  def __init__(self, name, health, level, skill) -> None:
    super().__init__(name, health, level)
    self.__skill = skill

  def get_skill(self):
    return self.__skill
  
  def show_info(self):
    return f"{super().show_info()}\nSkill: {self.get_skill()}\n"
  
  def special_attack(self, target):
    damage = random.randint(self.get_level() * 5, self.get_level() * 8)
    target.receive_damage(damage)
    print(f"{self.get_name()} usou a habilidade especial {self.get_skill()} em {target.get_name()} e causou {damage} de dano!")
  
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
    self.enemy = Enemy(name="Morcego", health=80, level=5, kind="Voador")
  
  def start_battle(self):
    """ Fazer a gestão da batalha em turnos """
    print("Iniciando batalha!")
    while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
      print("\nDetalhes dos Personagens:")
      print(self.hero.show_info())
      print(self.enemy.show_info())

      input("Pressione Enter para atacar...")
      choice = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")

      if choice == "1":
        self.hero.attack(self.enemy)
      elif choice == "2":
        self.hero.special_attack(self.enemy)
      else:
        print("Escolha inválida. Escolha novamente.")

      if self.enemy.get_health() > 0:
        self.enemy.attack(self.hero)

    if self.hero.get_health() > 0:
      print("\nParabéns, você venceu a batalha!")
    else:
      print("\nVocê foi derrotado!")

game = Game()
game.start_battle()