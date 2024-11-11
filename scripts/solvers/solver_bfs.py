from collections import deque
from scripts.solvers.solver import Solver

# Definindo as direções de movimento
DIRECTIONS = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]  # cima, baixo, esquerda, direita

MAX_STEPS = 10000000


class BFSSolver(Solver):
    def __init__(self, player, level, timer, SOLVER_DELAY):
        super().__init__(player, level, timer, SOLVER_DELAY)
        self.path = self.calculate_solution()
        print(self.path)
        self.path_to_movements()
        #super().show_movements()

    def solve_level(self):
        if not self.solution_tried:
            self.calculate_solution()
            super().show_movements()
            return True
        else:
            if self.was_solved:
                print(1)
                super().show_movements()
                return True
            else:
                print('NO SOLUTION FOUND')
                return False

    def calculate_solution(self):
        self.solution_tried = True
        count = 0

        boxes, goals = self.find_box_goals_positions(self.level)
        initial_state = ((len(self.level.matrix) - self.player.position.y - 1, self.player.position.x), tuple(boxes))
        queue = deque([(initial_state, [])])  # Armazena o estado atual e o caminho percorrido
        visited = set([initial_state])  # Armazena estados visitados

        while queue and count < MAX_STEPS:
            count += 1
            (player, boxes), path = queue.popleft()

            # Verifica se o nível está resolvido
            if self.is_solved(boxes, goals):
                self.was_solved = True
                return path  # Retorna o caminho necessário para resolver o nível

            # Tenta todos os movimentos possíveis
            for dr, dc, move in DIRECTIONS:
                new_player = (player[0] + dr, player[1] + dc)
                if not self.is_valid(new_player, self.level):
                    continue

                # Verifica se o movimento empurra uma caixa
                if new_player in boxes:
                    new_box = (new_player[0] + dr, new_player[1] + dc)

                    # Verifica se a nova posição da caixa é válida
                    if not self.is_valid(new_box, self.level) or new_box in boxes:
                        continue

                    # Novo estado ao empurrar a caixa
                    new_boxes = tuple(new_box if box == new_player else box for box in boxes)
                    new_state = (new_player, new_boxes)
                else:
                    # Novo estado sem empurrar uma caixa
                    new_state = (new_player, boxes)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_player]))  # Adiciona o novo estado e o caminho atualizado

        return None  # Retorna None se nenhum caminho for encontrado


    def find_box_goals_positions(self, level):
        boxes = []
        goals = []

        for r, row in enumerate(level.matrix):
            for c, cell in enumerate(row):
                if cell == "$":
                    boxes.append((r, c))
                elif cell == ".":
                    goals.append((r, c))
            print()

        return boxes, goals

    def path_to_movements(self):
        if self.was_solved:
            pos = (len(self.level.matrix) - self.player.position.y - 1, self.player.position.x)
            path = self.path.copy()
            while path:
                for dr, dc, move in DIRECTIONS:
                    if pos[0] + dr == path[0][0] and pos[1] + dc == path[0][1]:
                        self.movements.append(move)
                        pos = (pos[0] + dr,  pos[1] + dc)
                        path.pop(0)
                        break
            print(self.movements)

    # Função para verificar se o nível está resolvido (todas as caixas nos alvos)
    def is_solved(self, boxes, targets):
        return all(box in targets for box in boxes)

    # Função para verificar se uma posição é válida (dentro do nível e sem paredes)
    def is_valid(self, pos, level):
        r, c = pos
        return 0 <= r < len(level.matrix) and 0 <= c < len(level.matrix[0]) and level.matrix[r][c] != "#"

