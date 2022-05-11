import Model
import GameGui
import GameController


def main():
    model = Model.Model()
    view = GameGui.View()
    game = GameController.Controller(model, view)
    game.start_game()


if __name__ == "__main__":
    main()
