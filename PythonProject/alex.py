from random import randint
import pygame
import time

pygame.init()

diff_modes = ["Easy 🟢", "Medium 🟠", "Hard 🔴"]

difficulty = input("Enter difficulty: \n1 - Easy 🟢\n2 - Medium 🟠\n3 - Hard 🔴")

while not (difficulty == "1" or difficulty == "2" or difficulty == "3"):
    difficulty = input("Enter difficulty: \n1 - Easy 🟢\n2 - Medium 🟠\n3 - Hard 🔴")

difficulty = int(difficulty)

diff_value = difficulty - 1

print("Difficulty set:", diff_modes[diff_value])

back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_RED = (139, 0, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)

diff_time = [20, 15, 10]
diff_cards = [4, 6, 8]

cards = []
num_cards = diff_cards[diff_value]
score = 0
x = 70

max_time = diff_time[diff_value] + 1

start_time = time.time()

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 26)
    cards.append(new_card)
    x = x + 100

score_text = Label(60, 90, 150, 30, back)
score_text.set_text(f"SCORE: {score}", 30, DARK_BLUE)
score_text.draw(10, 10)

time_label = Label(60, 60, 150, 30, back)
time_label.set_text(f"TIME: {max_time}", 30, DARK_BLUE)
time_label.draw(10, 10)

restart_button = None

done = False
wait = 0
last_number = max_time

while not done:
    remaining_time = int(-(time.time() - start_time - max_time))

    # print("-")

    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].color(GREEN)
                        score += 1
                    else:
                        cards[i].color(RED)
                        score -= 1
                    cards[i].fill()
                    score_text.set_text(f"SCORE: {score}", 30, DARK_BLUE)
                    score_text.draw(10, 10)

    if last_number == 0:
        # done = True

        time_label.set_text(f"GAME OVER!", 30, RED)
        time_label.draw(10, 10)

        restart_button = Label(200, 300, 90, 40, RED)
        restart_button.outline(DARK_RED, 5)
        restart_button.set_text("RESTART", 26)
        restart_button.draw(7, 10)

        # pygame.quit()

    if last_number != remaining_time:
        last_number = remaining_time
        time_label.set_text(f"TIME: {remaining_time}", 30, DARK_BLUE)
        time_label.draw(10, 10)

    pygame.display.update()

    clock.tick(40)

# while True:
# for event in pygame.event.get():
#   print(".")
#    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#        x, y = event.pos
#        if restart_button.collidepoint(x, y):
#            restart_button.draw(0,0)
#    time.sleep(0.1)