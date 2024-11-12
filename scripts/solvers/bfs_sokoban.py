from collections import deque

# Definindo as direções de movimento
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # cima, baixo, esquerda, direita

# Função para encontrar a posição do jogador e as caixas no nível
def find_positions(level):
    player_pos = None
    boxes = []
    targets = []

    for r, row in enumerate(level):
        for c, cell in enumerate(row):
            if cell == "@":
                player_pos = (r, c)
            elif cell == "$":
                boxes.append((r, c))
            elif cell == ".":
                targets.append((r, c))

    return player_pos, boxes, targets


# Função para verificar se o nível está resolvido (todas as caixas nos alvos)
def is_solved(boxes, targets):
    return all(box in targets for box in boxes)


# Função para verificar se uma posição é válida (dentro do nível e sem paredes)
def is_valid(pos, level):
    r, c = pos
    return 0 <= r < len(level) and 0 <= c < len(level[0]) and level[r][c] != "#"


# Função principal do solver usando BFS
def solve_sokoban(level):
    # Encontrando as posições iniciais
    player_pos, boxes, targets = find_positions(level)
    initial_state = (player_pos, tuple(boxes))
    queue = deque([(initial_state, [])])  # Armazena o estado atual e o caminho percorrido
    visited = set([initial_state])  # Armazena estados visitados

    while queue:
        (player, boxes), path = queue.popleft()

        # Verifica se o nível está resolvido
        if is_solved(boxes, targets):
            return path  # Retorna o caminho necessário para resolver o nível

        # Tenta todos os movimentos possíveis
        for dr, dc in DIRECTIONS:
            new_player = (player[0] + dr, player[1] + dc)
            if not is_valid(new_player, level):
                continue

            # Verifica se o movimento empurra uma caixa
            if new_player in boxes:
                new_box = (new_player[0] + dr, new_player[1] + dc)

                # Verifica se a nova posição da caixa é válida
                if not is_valid(new_box, level) or new_box in boxes:
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


# Exemplo de uso
level = [
    ["#", "#", "#", "#", "#"],
    ["#", "-", "-", ".", "#"],
    ["#", "-", "$", "-", "#"],
    ["#", "@", "-", "-", "#"],
    ["#", "#", "#", "#", "#"]
]

level = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "-", "-", "-", "-", "-", "-", "-", "-", "#"],
    ["#", "-", "@", "-", "#", "#", "-", "-", "-", "#"],
    ["#", "-", "-", "$", ".", "-", "-", "-", "-", "#"],
    ["#", "#", "#", "-", "-", "-", "#", "#", "#", "#"],
    ["#", "-", "-", "-", "$", "-", "-", "-", "-", "#"],
    ["#", "-", ".", "-", "-", ".", "-", "-", "-", "#"],
    ["#", "-", "-", "-", "-", "-", "-", "-", "-", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

solution = solve_sokoban(level)
if solution:
    print("Caminho para resolver o nível:", solution)
else:
    print("Nenhuma solução encontrada.")
