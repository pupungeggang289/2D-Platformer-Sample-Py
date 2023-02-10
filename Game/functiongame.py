import var

def player_move():
    # Gravity apply
    predicted_x = var.World.Player.x
    predicted_y = var.World.Player.y

    row = int(predicted_y / 40)
    column = int(predicted_x / 40)

    if var.Input.Key.left == True:
        predicted_x -= var.World.Player.speed / var.FPS

    if var.Input.Key.right == True:
        predicted_x += var.World.Player.speed / var.FPS

    # Left Wall
    for i in range(-2, 3):
        for j in range(-2, 3):
            if row + i >= 0 and row + i < 15 and column + j >= 0 and column + j < 20:
                if var.World.wall[row + i][column + j] == 1:
                    right_line = [40 * (column + j) + 40, 40 * (row + i), 40 * (column + j) + 40, 40 * (row + i) + 40]
                    if predicted_x > right_line[0] and predicted_x < right_line[0] + 16 and predicted_y > right_line[1] - 16 and predicted_y < right_line[3] + 16:
                        predicted_x = right_line[0] + 16

    if predicted_x < 16:
        predicted_x = 16

    if predicted_x > 784:
        predicted_x = 784

    # Right Wall
    for i in range(-2, 3):
        for j in range(-2, 3):
            if row + i >= 0 and row + i < 15 and column + j >= 0 and column + j < 20:
                if var.World.wall[row + i][column + j] == 1:
                    left_line = [40 * (column + j), 40 * (row + i), 40 * (column + j), 40 * (row + i) + 40]
                    if predicted_x > left_line[0] - 16 and predicted_x < left_line[0] and predicted_y > left_line[1] - 16 and predicted_y < left_line[3] + 16:
                        predicted_x = left_line[0] - 16

    var.World.Player.ground = False
    predicted_y += var.World.Player.velocity_y / var.FPS

    # Floor
    for i in range(-2, 3):
        for j in range(-2, 3):
            if row + i >= 0 and row + i < 15 and column + j >= 0 and column + j < 20:
                if var.World.wall[row + i][column + j] == 1:
                    top_line = [40 * (column + j), 40 * (row + i), 40 * (column + j) + 40, 40 * (row + i)]
                    if predicted_x > top_line[0] - 16 and predicted_x < top_line[2] + 16 and predicted_y > top_line[1] - 16 and predicted_y < top_line[3]:
                        predicted_y = top_line[1] - 16
                        var.World.Player.velocity_y = 0
                        var.World.Player.ground = True
                        var.World.Player.jump = 1

    if predicted_y < 16:
        predicted_y = 16

    if predicted_y > 584:
        predicted_y = 584

    if var.World.Player.ground == False:
        if var.World.Player.velocity_y + var.World.gravity / var.FPS <= var.World.Player.terminal_speed:
            var.World.Player.velocity_y += var.World.gravity / var.FPS
        else:
            var.World.Player.velocity_y = var.World.Player.terminal_speed

    var.World.Player.x = predicted_x
    var.World.Player.y = predicted_y

def jump():
    var.World.Player.velocity_y = var.World.Player.jump_power