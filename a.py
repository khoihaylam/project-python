import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Đánh Bóng")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Tọa độ và kích thước của bóng và thanh đánh bóng
ball_x, ball_y = width // 2, height // 2
ball_radius = 10
ball_speed_x, ball_speed_y = 5, 5

paddle_width, paddle_height = 10, 60
paddle1_x, paddle1_y = 0, height // 2 - paddle_height // 2
paddle2_x, paddle2_y = width - paddle_width, height // 2 - paddle_height // 2
paddle_speed = 7

# Điểm số
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)


# Hàm vẽ bóng
def draw_ball(x, y):
    pygame.draw.circle(screen, white, (x, y), ball_radius)


# Hàm vẽ thanh đánh bóng
def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))


# Hàm vẽ điểm số
def draw_score(score1, score2):
    score_display = font.render(f"{score1} - {score2}", True, white)
    screen.blit(score_display, (width // 2 - 30, 10))


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Di chuyển thanh đánh bóng của người chơi
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed

    # Di chuyển thanh đánh bóng của máy
    if paddle2_y + paddle_height // 2 < ball_y and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed
    elif paddle2_y + paddle_height // 2 > ball_y and paddle2_y > 0:
        paddle2_y -= paddle_speed

    # Di chuyển bóng
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Xử lý va chạm với tường trên và dưới
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y

    # Xử lý va chạm với thanh đánh bóng
    if (
        paddle1_x <= ball_x - ball_radius <= paddle1_x + paddle_width
        and paddle1_y <= ball_y <= paddle1_y + paddle_height
    ) or (
        paddle2_x <= ball_x + ball_radius <= paddle2_x + paddle_width
        and paddle2_y <= ball_y <= paddle2_y + paddle_height
    ):
        ball_speed_x = -ball_speed_x

    # Xử lý khi bóng đi ra khỏi màn hình (ghi điểm)
    if ball_x - ball_radius <= 0:
        score2 += 1
        ball_x, ball_y = width // 2, height // 2

    if ball_x + ball_radius >= width:
        score1 += 1
        ball_x, ball_y = width // 2, height // 2

    # Vẽ đối tượng
    screen.fill(black)
    draw_ball(ball_x, ball_y)
    draw_paddle(paddle1_x, paddle1_y)
    draw_paddle(paddle2_x, paddle2_y)
    draw_score(score1, score2)

    # Hiển thị màn hình
    pygame.display.flip()

    # Đặt tốc độ khung hình
    pygame.time.Clock().tick(60)
